# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.utils import timezone
import hashlib

from .models import Ksiazka
from .models import Adres
from .models import Klienci
from .models import Recenzje
from .models import KsiazkaHasKategoriaSlownik
from .models import KategoriaSlownik
from .models import Wydanie
from .models import NazwaWydawnictwaSlownik
from .models import Recenzje
from .models import Zamowienie
from .models import StatusZamowieniaSlownik
from .models import ZamowienieHasKsiazka

from .forms import UserForm
from .forms import AdresForm
from .forms import UserLoginForm
from .forms import ReviewForm
from .forms import BuyForm

def debug(arg_str):
    f = open('debug.log', 'w')
    #f.truncate()
    f.write(arg_str)
    f.write('\n\n')
    f.close()

def save_id(arg):
    f = open('log.cookie', 'w')
    f.truncate()
    f.write(str(arg))
    f.close()

def read_id():
    f = open('log.cookie', 'r')
    r_id = int(f.read())
    f.close()
    return r_id

def category(request, pk):
    id_category = KategoriaSlownik.objects.filter(kategoria=pk)
    books_tmp = KsiazkaHasKategoriaSlownik.objects.filter(kategoria_slownik_idkategoria=id_category)
    books_list = Ksiazka.objects.filter(idksiazka__in=books_tmp.values('ksiazka_idksiazka')) #nazwaPola__in do wyszukiwania po Querysecie (wiele warunkow)

    if read_id() > 0:
        loged_in = True
    else:
        loged_in = False
    return render(request, 'app_shop/category.html', {'loged_in': loged_in, \
    "category_name": pk, "books_list": books_list})

def books_list(request, loged_in=False):
    books = Ksiazka.objects.all

    if read_id() > 0:
        loged_in = True
    else:
        loged_in = False
    return render(request, 'app_shop/books_list.html', {'books': books, 'loged_in': loged_in})

def book_detail(request, pk):
    book = get_object_or_404(Ksiazka, idksiazka=pk)
    reviews = Recenzje.objects.filter(ksiazka_idksiazka=pk)
    #debug(str(getattr(book,'wydanie_idwydanie')))
    pub_house = getattr(book,'wydanie_idwydanie') #Wydanie.objects.filter(idwydanie=getattr(book,'wydanie_idwydanie')) #getattr(book,'wydanie_idwydanie')
    pub_name = getattr(pub_house, 'nazwa_wydawnictwa_slownik_idnazwa_wyd')
    #debug(review)
    #tmp = review[0].values('klienci_idklient')
    #tmp = review.get_field('klienci_idklient')
    #tmp = getattr(reviews[0], 'klienci_idklient')
    #debug(tmp)
    #review_author = Klienci.objects.filter(login=tmp)
    #if review_author.exists():
    #    review_author=review_author[0].login
    #else:
    #    review_author="Konto nieaktywne"
    #review_author=str(getattr(reviews[0], 'klienci_idklient'))

    tags = KsiazkaHasKategoriaSlownik.objects.filter(ksiazka_idksiazka=pk)

    if read_id() > 0:
        loged_in = True
    else:
        loged_in = False
    return render(request, 'app_shop/book_detail.html', {'loged_in': loged_in, 'user_id': read_id(), 'book': book, \
    'review_exist': reviews.exists(), 'reviews': reviews, \
    'tags_exist': tags.exists(), 'tags': tags,
    'pub_house': pub_house, 'pub_name': pub_name})

def login(request):
    error_msg = " "
    if request.method == 'POST':
        form_usr = UserLoginForm(request.POST)

        if form_usr.is_valid():
            if Klienci.objects.filter(login=form_usr.cleaned_data['login_f'], haslo=hashlib.sha1(form_usr.cleaned_data['haslo_f']).hexdigest()).exists():
                tmp = Klienci.objects.filter(login=form_usr.cleaned_data['login_f']).values('idklient')[0]
                save_id(tmp['idklient'])
                return redirect('/')
            elif Klienci.objects.filter(login=form_usr.cleaned_data['login_f']).exists():
                error_msg = "Zle haslo!"
            else:
                error_msg = "Nieprawidlowy login!"
        else:
            error_msg = "Podaj login i haslo!"
    else:
        form_usr = UserLoginForm()

    if read_id() > 0:
        loged_in = True
    else:
        loged_in = False
    return render(request, 'app_shop/login.html', {'form_usr': form_usr, 'error_msg': error_msg, 'loged_in': loged_in})

def logout(request):
    save_id(0)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))


def sign_up(request):
    error_msg = " "
    if request.method == "POST":
        form_user = UserForm(request.POST, prefix='user')
        form_adres = AdresForm(request.POST, prefix='adress')

        if form_adres.is_valid() and form_user.is_valid():
            adres = form_adres.save(commit=False)
            try:
                obj = Adres.objects.get(miejscowosc=adres.miejscowosc, ulica=adres.ulica, nr_domu=adres.nr_domu, nr_mieszkania=adres.nr_mieszkania, kod_pocztowy=adres.kod_pocztowy,)
            except Adres.DoesNotExist:
                obj = Adres(miejscowosc=adres.miejscowosc, ulica=adres.ulica, nr_domu=adres.nr_domu, nr_mieszkania=adres.nr_mieszkania, kod_pocztowy=adres.kod_pocztowy,)
                obj.save()

            user = form_user.save(commit=False)
            if Klienci.objects.filter(login=user.login).exists():
                error_msg = "Podany login jest już zajęty"
            elif Klienci.objects.filter(email=user.email).exists():
                    error_msg = "Podany email jest juz zajety"
            else:
                user.adres_idadres = obj
                user.haslo = hashlib.sha1(user.haslo).hexdigest()
                user.save()
                login(request)
                return redirect('/')
        else:
            error_msg = "Podaj pola obwiązkowe!"
    else:
        form_user = UserForm()
        debug(str(form_user))
        form_adres = AdresForm()
    return render(request, 'app_shop/sign_up.html', {'form_user': form_user, 'form_adres': form_adres, 'error_msg': error_msg})

def buy(request, pk):
    error_msg = " "
    tmp = Ksiazka.objects.filter(idksiazka=pk)[:1].get()
    if request.method == "POST":
        form_buy = BuyForm(request.POST)
        if form_buy.is_valid():
            tmp1 = form_buy.cleaned_data['ilosc']
            debug(str(tmp1))
            if tmp1 > getattr(tmp, 'ilosc'):
                error_msg = "W magazynie nie ma tak wielu ksiazek!"
            else:
                obj = Zamowienie(wartosc=getattr(tmp, 'cena')*tmp1, data=timezone.now(), \
                status_zamowienia_slownik_idstatus_zamowienia_slownik=StatusZamowieniaSlownik.objects.filter(status='n')[:1].get(), \
                klienci_idklient=Klienci.objects.filter(idklient=read_id())[:1].get())
                obj.save()
                tmp.ilosc = getattr(tmp, 'ilosc') - tmp1
                tmp.save()
                obj1 = ZamowienieHasKsiazka(ilosc=tmp1, zamowienia_idzamowienia=obj, ksiazka_idksiazka=tmp)
                obj1.save()
                return redirect('/')
        else:
            error_msg = "Podaj ile egzemplaży chcesz kupić!"
    else:
        form_buy = BuyForm()
    if read_id() > 0:
        loged_in = True
    else:
        loged_in = False
    #You must be logged in to buy a book
    return render(request,'app_shop/buy.html', { 'loged_in': loged_in, 'error_msg': error_msg, \
    'form_buy': form_buy, 'ilosc': getattr(tmp, 'ilosc'), 'cena': getattr(tmp, 'cena')})

def writereview(request, pk):
    error_msg = " "
    book = Ksiazka.objects.filter(idksiazka=pk)
    if request.method == "POST":
        form_review = ReviewForm(request.POST, prefix='review')

        if form_review.is_valid():
            review = form_review.save(commit=False)
            tmp = Klienci.objects.filter(idklient=read_id())[:1].get()
            obj = Recenzje(tresc=review.tresc, klienci_idklient=tmp, ksiazka_idksiazka=Ksiazka.objects.filter(idksiazka=pk)[:1].get())
            obj.save()
            return redirect('book_detail', pk=pk)
        else:
            error_msg = "Podaj treść recenzji!"
    else:
        form_review = ReviewForm()
    if read_id() > 0:
        loged_in = True
    else:
        loged_in = False
    return render(request, 'app_shop/writereview.html', {'loged_in': loged_in, \
    'book': book, 'form_review': form_review})

def acountdetails(request):
    usr_id = read_id()
    if usr_id > 0:
        usr = Klienci.objects.filter(idklient=usr_id)
        adress = getattr(usr[:1].get(),'adres_idadres')
        reviews = Recenzje.objects.filter(klienci_idklient=usr_id)
        orders = Zamowienie.objects.filter(klienci_idklient=usr_id)
        tmp = ZamowienieHasKsiazka.objects.filter(zamowienia_idzamowienia__in=orders)
        books = Ksiazka.objects.filter(idksiazka__in=tmp.values('ksiazka_idksiazka'))
        #statuses = StatusZamowieniaSlownik.objects.filter(idstatus_zamowienia_slownik__in=orders.values('idstatus_zamowienia_slownik'))
        statuses = StatusZamowieniaSlownik.objects.filter()
        list_ord = zip(orders,books)
        #debug(str(books))

    else:
        return redirect('/')
    return render(request, 'app_shop/my_profile.html', {'loged_in': usr_id, \
    'usr': usr, 'adress': adress, 'reviews': reviews, 'orders': orders, 'books': books, 'list': list_ord, \
    'status1': statuses[:1].get(), 'status2': statuses[1:2].get(), 'status3': statuses[2:3].get(),
    'status3': statuses[2:3].get(), 'status4': statuses[3:4].get(), 'status5': statuses[4:5].get()})

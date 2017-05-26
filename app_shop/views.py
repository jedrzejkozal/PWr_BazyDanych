# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from .models import Ksiazka
from .forms import UserForm
from .forms import AdresForm

def books_list(request):
    books = Ksiazka.objects.all
    return render(request, 'app_shop/books_list.html', {'books': books})

def book_detail(request, pk):
    book = get_object_or_404(Ksiazka, idksiazka=pk)
    return render(request, 'app_shop/book_detail.html', {'book': book})

def login(request):
    return render(request, 'app_shop/login.html', {})

def sign_up(request):
    form1 = UserForm()
    form2 = AdresForm()
    return render(request, 'app_shop/sign_up.html', {'form1': form1, 'form2': form2})

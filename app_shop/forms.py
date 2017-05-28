from django import forms

from .models import Klienci
from .models import Adres
from .models import Recenzje

class UserForm(forms.ModelForm):
    prefix = 'user'

    class Meta:
        model = Klienci
        fields = ('login', 'haslo', 'imie', 'nazwisko','email','telefon',)

class AdresForm(forms.ModelForm):
    prefix = 'adress'

    class Meta:
        model = Adres
        fields = ('miejscowosc','ulica','nr_domu','nr_mieszkania','kod_pocztowy')

class ReviewForm(forms.ModelForm):
    prefix = 'review'

    class Meta:
        model = Recenzje
        fields = ('tresc', 'idrecenzji')

class UserLoginForm(forms.Form):
    login_f = forms.CharField(label='login', max_length=15)
    haslo_f = forms.CharField(label='haslo', max_length=45)

class BuyForm(forms.Form):
    ilosc = forms.IntegerField(label='ilosc')

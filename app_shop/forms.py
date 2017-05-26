from django import forms

from .models import Klienci
from .models import Adres

class UserForm(forms.ModelForm):

    class Meta:
        model = Klienci
        fields = ('login', 'haslo', 'imie', 'nazwisko','email','telefon',)

class AdresForm(forms.ModelForm):

    class Meta:
        model = Adres
        fields = ('miejscowosc','ulica','nr_domu','nr_mieszkania','kod_pocztowy')

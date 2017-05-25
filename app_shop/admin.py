# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *

admin.site.register(Adres)
admin.site.register(KategoriaSlownik)
admin.site.register(Klienci)
admin.site.register(Ksiazka)
admin.site.register(KsiazkaHasKategoriaSlownik)
admin.site.register(NazwaWydawnictwaSlownik)
admin.site.register(Recenzje)
admin.site.register(StatusZamowieniaSlownik)
admin.site.register(Wydanie)
admin.site.register(Zamowienie)
admin.site.register(ZamowienieHasKsiazka)

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Ksiazka

def books_list(request):
    books = Ksiazka.objects.all
    return render(request, 'app_shop/books_list.html', {'books': books})

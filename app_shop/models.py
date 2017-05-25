# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Adres(models.Model):
    idadres = models.AutoField(db_column='idAdres', primary_key=True)  # Field name made lowercase.
    miejscowo_field = models.CharField(db_column='miejscowo\u015b\u0107', max_length=45)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ulica = models.CharField(max_length=20, blank=True, null=True)
    nr_domu = models.CharField(max_length=5)
    nr_mieszkania = models.SmallIntegerField(blank=True, null=True)
    kod_pocztowy = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Adres'


class KategoriaSownik(models.Model):
    idkategoria = models.AutoField(db_column='idKategoria', primary_key=True)  # Field name made lowercase.
    kategoria = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'Kategoria_słownik'


class Klienci(models.Model):
    idklient = models.AutoField(db_column='idKlient', primary_key=True)  # Field name made lowercase.
    login = models.CharField(max_length=15)
    has_o = models.CharField(db_column='has\u0142o', max_length=45)  # Field renamed to remove unsuitable characters.
    imie = models.CharField(max_length=30)
    nazwisko = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    telefon = models.IntegerField(blank=True, null=True)
    adres_idadres = models.ForeignKey(Adres, models.DO_NOTHING, db_column='Adres_idAdres')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Klienci'
        unique_together = (('idklient', 'adres_idadres'),)


class Ksiazka(models.Model):
    idksiazka = models.AutoField(db_column='idKsiazka', primary_key=True)  # Field name made lowercase.
    tytul = models.CharField(max_length=45)
    autor = models.CharField(max_length=45)
    opis = models.TextField(blank=True, null=True)
    ilosc = models.IntegerField()
    cena = models.IntegerField()
    isbn = models.CharField(db_column='ISBN', max_length=20)  # Field name made lowercase.
    wydanie_idwydanie = models.ForeignKey('Wydanie', models.DO_NOTHING, db_column='Wydanie_idWydanie')  # Field name made lowercase.
    wydanie_nazwa_wydawnictwa_s_ownik_idnazwa_wyd = models.ForeignKey('Wydanie', models.DO_NOTHING, db_column='Wydanie_Nazwa_wydawnictwa_s\u0142ownik_idNazwa_wyd')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Ksiazka'
        unique_together = (('idksiazka', 'wydanie_idwydanie', 'wydanie_nazwa_wydawnictwa_s_ownik_idnazwa_wyd'), ('tytul', 'autor'),)


class KsiazkaHasKategoriaSownik(models.Model):
    ksiazka_idksiazka = models.ForeignKey(Ksiazka, models.DO_NOTHING, db_column='Ksiazka_idKsiazka', primary_key=True)  # Field name made lowercase.
    kategoria_s_ownik_idkategoria = models.ForeignKey(KategoriaSownik, models.DO_NOTHING, db_column='Kategoria_s\u0142ownik_idKategoria')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Ksiazka_has_Kategoria_słownik'
        unique_together = (('ksiazka_idksiazka', 'kategoria_s_ownik_idkategoria'),)


class Ksiazki(models.Model):
    idksiazki = models.IntegerField(db_column='idKsiazki', primary_key=True)  # Field name made lowercase.
    tytul = models.CharField(max_length=45)
    autor = models.CharField(max_length=45)
    opis = models.TextField(blank=True, null=True)
    ilosc = models.IntegerField()
    cena = models.IntegerField()
    isbn = models.CharField(db_column='ISBN', max_length=20)  # Field name made lowercase.
    wydanie_idwydanie = models.ForeignKey('Wydanie', models.DO_NOTHING, db_column='Wydanie_idWydanie')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Ksiazki'
        unique_together = (('idksiazki', 'wydanie_idwydanie'), ('tytul', 'autor'),)


class NazwaWydawnictwaSownik(models.Model):
    idnazwa_wyd = models.AutoField(db_column='idNazwa_wyd', primary_key=True)  # Field name made lowercase.
    nazwa_wydawnictwa = models.CharField(db_column='Nazwa_wydawnictwa', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Nazwa_wydawnictwa_słownik'


class Recenzje(models.Model):
    idrecenzji = models.AutoField(primary_key=True)
    tresc = models.TextField()
    klienci_idklient = models.ForeignKey(Klienci, models.DO_NOTHING, db_column='Klienci_idKlient')  # Field name made lowercase.
    ksiazka_idksiazka = models.ForeignKey(Ksiazka, models.DO_NOTHING, db_column='Ksiazka_idKsiazka')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Recenzje'
        unique_together = (('idrecenzji', 'klienci_idklient', 'ksiazka_idksiazka'),)


class StatusZamwieniaSownik(models.Model):
    idstatus_zam_wienia_s_ownik = models.AutoField(db_column='idStatus_zam\xf3wienia_s\u0142ownik', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    status = models.CharField(db_column='Status', max_length=1)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Status_zamówienia_słownik'


class Wydanie(models.Model):
    idwydanie = models.AutoField(db_column='idWydanie', primary_key=True)  # Field name made lowercase.
    rok_wyd = models.DateField(blank=True, null=True)
    miejsce = models.CharField(max_length=20, blank=True, null=True)
    oprawa = models.CharField(max_length=1, blank=True, null=True)
    nazwa_wydawnictwa_s_ownik_idnazwa_wyd = models.ForeignKey(NazwaWydawnictwaSownik, models.DO_NOTHING, db_column='Nazwa_wydawnictwa_s\u0142ownik_idNazwa_wyd')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Wydanie'
        unique_together = (('idwydanie', 'nazwa_wydawnictwa_s_ownik_idnazwa_wyd'),)


class Zamowienie(models.Model):
    idzamowienia = models.AutoField(db_column='idZamowienia', primary_key=True)  # Field name made lowercase.
    warto_field = models.IntegerField(db_column='warto\u015b\u0107')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    data = models.DateField()
    status_zam_wienia_s_ownik_idstatus_zam_wienia_s_ownik = models.ForeignKey(StatusZamwieniaSownik, models.DO_NOTHING, db_column='Status_zam\xf3wienia_s\u0142ownik_idStatus_zam\xf3wienia_s\u0142ownik')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    klienci_idklient = models.ForeignKey(Klienci, models.DO_NOTHING, db_column='Klienci_idKlient')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Zamowienie'
        unique_together = (('idzamowienia', 'status_zam_wienia_s_ownik_idstatus_zam_wienia_s_ownik', 'klienci_idklient'),)


class ZamowienieHasKsiazka(models.Model):
    ilosc = models.IntegerField()
    zamowienia_idzamowienia = models.ForeignKey(Zamowienie, models.DO_NOTHING, db_column='Zamowienia_idZamowienia', primary_key=True)  # Field name made lowercase.
    zamowienia_status_zam_wienia_s_ownik_idstatus_zam_wienia_s_ownik = models.ForeignKey(Zamowienie, models.DO_NOTHING, db_column='Zamowienia_Status_zam\xf3wienia_s\u0142ownik_idStatus_zam\xf3wienia_s\u0142ownik')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    zamowienia_klienci_idklient = models.ForeignKey(Zamowienie, models.DO_NOTHING, db_column='Zamowienia_Klienci_idKlient')  # Field name made lowercase.
    ksiazka_idksiazka = models.ForeignKey(Ksiazka, models.DO_NOTHING, db_column='Ksiazka_idKsiazka')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Zamowienie_has_Ksiazka'
        unique_together = (('zamowienia_idzamowienia', 'zamowienia_status_zam_wienia_s_ownik_idstatus_zam_wienia_s_ownik', 'zamowienia_klienci_idklient', 'ksiazka_idksiazka'),)

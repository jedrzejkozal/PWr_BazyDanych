# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models
from text_unidecode import unidecode


class Adres(models.Model):
    idadres = models.AutoField(db_column='idAdres', primary_key=True)  # Field name made lowercase.
    miejscowosc = models.CharField(max_length=45)
    ulica = models.CharField(max_length=20, blank=True, null=True)
    nr_domu = models.CharField(max_length=5)
    nr_mieszkania = models.SmallIntegerField(blank=True, null=True)
    kod_pocztowy = models.IntegerField()

    def __str__(self):
        data = '%s %s' % (self.miejscowosc, self.nr_domu)
        return unidecode(data)

    class Meta:
        managed = False
        db_table = 'Adres'


class KategoriaSlownik(models.Model):
    idkategoria = models.AutoField(db_column='idKategoria', primary_key=True)
    kategoria = models.CharField(max_length=20)

    def __str__(self):
        data = self.kategoria
        return unidecode(data)

    class Meta:
        managed = False
        db_table = 'Kategoria_slownik'


class Klienci(models.Model):
    idklient = models.AutoField(db_column='idKlient', primary_key=True)
    login = models.CharField(max_length=15)
    haslo = models.CharField(max_length=45)
    imie = models.CharField(max_length=30)
    nazwisko = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    telefon = models.IntegerField(blank=True, null=True)
    adres_idadres = models.ForeignKey(Adres, models.DO_NOTHING, db_column='Adres_idAdres')

    def __str__(self):
        data = self.login
        return unidecode(data)

    class Meta:
        managed = False
        db_table = 'Klienci'
        unique_together = (('idklient', 'adres_idadres'),)


class Ksiazka(models.Model):
    idksiazka = models.AutoField(db_column='idKsiazka', primary_key=True)
    tytul = models.CharField(max_length=45)
    autor = models.CharField(max_length=45)
    opis = models.TextField(blank=True, null=True)
    ilosc = models.IntegerField()
    cena = models.IntegerField()
    isbn = models.CharField(db_column='ISBN', max_length=20)  # Field name made lowercase.
    wydanie_idwydanie = models.ForeignKey('Wydanie', models.DO_NOTHING, db_column='Wydanie_idWydanie')

    def __str__(self):
        data = self.tytul
        return unidecode(data)

    class Meta:
        managed = False
        db_table = 'Ksiazka'
        unique_together = (('idksiazka', 'wydanie_idwydanie'), ('tytul', 'autor'),)


class KsiazkaHasKategoriaSlownik(models.Model):
    ksiazka_idksiazka = models.ForeignKey(Ksiazka, models.DO_NOTHING, db_column='Ksiazka_idKsiazka', primary_key=True)  # Field name made lowercase.
    kategoria_slownik_idkategoria = models.ForeignKey(KategoriaSlownik, models.DO_NOTHING, db_column='Kategoria_slownik_idKategoria')  # Field name made lowercase.

    def __str__(self):
        data = '%s %s' % (self.ksiazka_idksiazka, self.kategoria_slownik_idkategoria)
        return unidecode(data)

    class Meta:
        managed = False
        db_table = 'Ksiazka_has_Kategoria_slownik'
        unique_together = (('ksiazka_idksiazka', 'kategoria_slownik_idkategoria'),)


class NazwaWydawnictwaSlownik(models.Model):
    idnazwa_wyd = models.AutoField(db_column='idNazwa_wyd', primary_key=True)  # Field name made lowercase.
    nazwa_wydawnictwa = models.CharField(db_column='Nazwa_wydawnictwa', max_length=45)  # Field name made lowercase.

    def __str__(self):
        data = self.nazwa_wydawnictwa
        return unidecode(data)

    class Meta:
        managed = False
        db_table = 'Nazwa_wydawnictwa_slownik'


class Recenzje(models.Model):
    idrecenzji = models.AutoField(primary_key=True)
    tresc = models.TextField()
    klienci_idklient = models.ForeignKey(Klienci, models.DO_NOTHING, db_column='Klienci_idKlient')  # Field name made lowercase.
    ksiazka_idksiazka = models.ForeignKey(Ksiazka, models.DO_NOTHING, db_column='Ksiazka_idKsiazka')  # Field name made lowercase.

    def __str__(self):
        data = self.tresc
        return unidecode(data)

    class Meta:
        managed = False
        db_table = 'Recenzje'
        unique_together = (('idrecenzji', 'klienci_idklient', 'ksiazka_idksiazka'),)


class StatusZamowieniaSlownik(models.Model):
    idstatus_zamowienia_slownik = models.AutoField(db_column='idStatus_zamowienia_slownik', primary_key=True)
    status = models.CharField(db_column='Status', max_length=1)

    def __str__(self):
        return self.status

    class Meta:
        managed = False
        db_table = 'Status_zamowienia_slownik'


class Wydanie(models.Model):
    idwydanie = models.AutoField(db_column='idWydanie', primary_key=True)
    rok_wyd = models.DateField(blank=True, null=True)
    miejsce = models.CharField(max_length=20, blank=True, null=True)
    oprawa = models.CharField(max_length=1, blank=True, null=True)
    nazwa_wydawnictwa_slownik_idnazwa_wyd = models.ForeignKey(NazwaWydawnictwaSlownik, models.DO_NOTHING, db_column='Nazwa_wydawnictwa_slownik_idNazwa_wyd')  # Field name made lowercase.

    def __str__(self):
        data = '%s %s' % (self.miejsce, self.rok_wyd)
        return unidecode(data)

    class Meta:
        managed = False
        db_table = 'Wydanie'
        unique_together = (('idwydanie', 'nazwa_wydawnictwa_slownik_idnazwa_wyd'),)


class Zamowienie(models.Model):
    idzamowienia = models.AutoField(db_column='idZamowienia', primary_key=True)
    wartosc = models.IntegerField()
    data = models.DateField()
    status_zamowienia_slownik_idstatus_zamowienia_slownik = models.ForeignKey(StatusZamowieniaSlownik, models.DO_NOTHING, db_column='Status_zamowienia_slownik_idStatus_zamowienia_slownik')  # Field name made lowercase.
    klienci_idklient = models.ForeignKey(Klienci, models.DO_NOTHING, db_column='Klienci_idKlient')

    def __str__(self):
        return self.idzamowienia

    class Meta:
        managed = False
        db_table = 'Zamowienie'
        unique_together = (('idzamowienia', 'status_zamowienia_slownik_idstatus_zamowienia_slownik', 'klienci_idklient'),)


class ZamowienieHasKsiazka(models.Model):
    ilosc = models.IntegerField()
    zamowienia_idzamowienia = models.ForeignKey(Zamowienie, models.DO_NOTHING, db_column='Zamowienia_idZamowienia', primary_key=True)
    ksiazka_idksiazka = models.ForeignKey(Ksiazka, models.DO_NOTHING, db_column='Ksiazka_idKsiazka')

    def __str__(self):
        data =  '%s %s' % (self.zamowienia_idzamowienia, self.ksiazka_idksiazka)
        return unidecode(data)

    class Meta:
        managed = False
        db_table = 'Zamowienie_has_Ksiazka'
        unique_together = (('zamowienia_idzamowienia', 'ksiazka_idksiazka'),)

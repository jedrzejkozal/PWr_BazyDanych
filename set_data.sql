SET FOREIGN_KEY_CHECKS = 0;
TRUNCATE Wydanie;
TRUNCATE Nazwa_wydawnictwa_slownik;
TRUNCATE Kategoria_slownik;
TRUNCATE Ksiazka;
TRUNCATE Ksiazka_has_Kategoria_slownik;
TRUNCATE Adres;
TRUNCATE Klienci;
TRUNCATE Recenzje;
TRUNCATE Status_zamowienia_slownik;
TRUNCATE Zamowienie;
TRUNCATE Zamowienie_has_Ksiazka;
SET FOREIGN_KEY_CHECKS = 1;

INSERT INTO Nazwa_wydawnictwa_slownik (Nazwa_wydawnictwa) VALUES
    ('Amber'), ('PWN'), ('Proszynski i S-ka'),
    ('Znak'),('Bialy Kruk'),('Rebis');

INSERT INTO  Wydanie (rok_wyd, miejsce, oprawa, Nazwa_wydawnictwa_slownik_idNazwa_wyd) VALUES
  ('2016-05-01','Warszawa','t',1),
  ('2015-12-21','Bialystok','m',4);

INSERT INTO Ksiazka (tytul, autor, opis, ilosc, cena, ISBN, Wydanie_idWydanie) VALUES
  ('DecoMorreno','Kakao','Kakako',100,35,'123123',2),
  ('Analiza Matematyczna','Skoczylas',' ',30, 35, '1231224',1),
  ('DjangoBook','Ktostam',NULL,30, 35, '1231466',2);

INSERT INTO Kategoria_slownik (kategoria) VALUES
  ('bestseller'),('kakao'),('matematyka');

INSERT INTO Status_zamowienia_slownik (Status) VALUES
  ('n'), /*niekaktywne - nie ma książek w magazynie*/
  ('a'), /*aktywne*/
  ('g'), /*gotowe do wysylki*/
  ('w'), /*wyslane*/
  ('z'); /*zrealizowane*/

INSERT INTO Adres (miejscowosc, ulica, nr_domu, nr_mieszkania, kod_pocztowy) VALUES
  ('Wroclaw', 'Kamienna', '17a', 3, 91300),
  ('Wies Mala', NULL, '4', 15, 11230),
  ('Piotrkow Trybunalski', 'Slowackiego', '7c', NULL, 97300);

INSERT INTO Klienci (login, haslo, imie, nazwisko, email, telefon, Adres_idAdres) VALUES
  ('zbyszek', '12345', 'Zbigniew', 'Wszywka', 'zbigniew@zbigniew.com.pl', 123456789, 1),
  ('mauryc', 'qwerty', 'Maurycy', 'Myszowski', 'maurycy@maurycy.com', NULL, 2),
  ('ignac', 'haslo', 'Ignacy', 'Wszywka', 'ignacy@zbigniew.com.pl', 123456780, 1),
  ('test', '1234', 'test','test','test',1234, 3);

INSERT INTO Recenzje (tresc, Klienci_idKlient, Ksiazka_idKsiazka) VALUES
  ('Pasjonująca opwowieść o całkach, funkcjach wielu zmiennych i szeregach.', 4, 2),
  ('Super', 4, 2),
  ('Niefajne :(', 4, 2),
  ('Niezbyt dobre', 2, 2),
  ('Dobre kakao', 3, 1);

INSERT INTO Ksiazka_has_Kategoria_słownik (Ksiazka_idKsiazka, Kategoria_słownik_idKategoria) VALUES
  (1, 1), (2,1), (2,3);

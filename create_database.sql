-- MySQL Script generated by MySQL Workbench
-- 05/15/17 18:00:52
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema Ksiegarnia
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema Ksiegarnia
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `Ksiegarnia` DEFAULT CHARACTER SET utf8 ;
USE `Ksiegarnia` ;

-- -----------------------------------------------------
-- Table `Ksiegarnia`.`Adres`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Ksiegarnia`.`Adres` ;

CREATE TABLE IF NOT EXISTS `Ksiegarnia`.`Adres` (
  `idAdres` INT(10) NOT NULL AUTO_INCREMENT,
  `miejscowosc` VARCHAR(45) NOT NULL,
  `ulica` VARCHAR(20) NULL,
  `nr_domu` VARCHAR(5) NOT NULL,
  `nr_mieszkania` SMALLINT UNSIGNED NULL,
  `kod_pocztowy` MEDIUMINT UNSIGNED NOT NULL DEFAULT '99999',
  PRIMARY KEY (`idAdres`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Ksiegarnia`.`Klienci`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Ksiegarnia`.`Klienci` ;

CREATE TABLE IF NOT EXISTS `Ksiegarnia`.`Klienci` (
  `idKlient` INT(10) NOT NULL AUTO_INCREMENT,
  `login` VARCHAR(15) NOT NULL,
  `haslo` VARCHAR(45) NOT NULL,
  `imie` VARCHAR(30) NOT NULL,
  `nazwisko` VARCHAR(30) NOT NULL,
  `email` VARCHAR(30) NOT NULL,
  `telefon` INT UNSIGNED NULL DEFAULT 123456789,
  `Adres_idAdres` INT(10) NOT NULL,
  PRIMARY KEY (`idKlient`, `Adres_idAdres`),
  CONSTRAINT `fk_Klienci_Adres1`
    FOREIGN KEY (`Adres_idAdres`)
    REFERENCES `Ksiegarnia`.`Adres` (`idAdres`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Ksiegarnia`.`Kategoria_slownik`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Ksiegarnia`.`Kategoria_slownik` ;

CREATE TABLE IF NOT EXISTS `Ksiegarnia`.`Kategoria_slownik` (
  `idKategoria` INT NOT NULL AUTO_INCREMENT,
  `kategoria` VARCHAR(20) NOT NULL,
  PRIMARY KEY (`idKategoria`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Ksiegarnia`.`Ksiazka_has_Kategoria_slownik`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Ksiegarnia`.`Ksiazka_has_Kategoria_slownik` ;

CREATE TABLE IF NOT EXISTS `Ksiegarnia`.`Ksiazka_has_Kategoria_slownik` (
  `Ksiazka_idKsiazka` INT NOT NULL,
  `Kategoria_slownik_idKategoria` INT NOT NULL,
  PRIMARY KEY (`Ksiazka_idKsiazka`, `Kategoria_slownik_idKategoria`),
  CONSTRAINT `fk_Ksiazka_has_Kategoria_slownik_Ksiazka1`
    FOREIGN KEY (`Ksiazka_idKsiazka`)
    REFERENCES `Ksiegarnia`.`Ksiazka` (`idKsiazka`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Ksiazka_has_Kategoria_slownik_Kategoria_slownik1`
    FOREIGN KEY (`Kategoria_slownik_idKategoria`)
    REFERENCES `Ksiegarnia`.`Kategoria_slownik` (`idKategoria`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Ksiegarnia`.`Nazwa_wydawnictwa_slownik`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Ksiegarnia`.`Nazwa_wydawnictwa_slownik` ;

CREATE TABLE IF NOT EXISTS `Ksiegarnia`.`Nazwa_wydawnictwa_slownik` (
  `idNazwa_wyd` INT NOT NULL AUTO_INCREMENT,
  `Nazwa_wydawnictwa` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idNazwa_wyd`))
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `Ksiegarnia`.`Wydanie`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Ksiegarnia`.`Wydanie` ;

CREATE TABLE IF NOT EXISTS `Ksiegarnia`.`Wydanie` (
  `idWydanie` INT NOT NULL AUTO_INCREMENT,
  `rok_wyd` DATE NULL,
  `miejsce` VARCHAR(20) NULL,
  `oprawa` CHAR(1) NULL,
  `Nazwa_wydawnictwa_slownik_idNazwa_wyd` INT NOT NULL,
  PRIMARY KEY (`idWydanie`, `Nazwa_wydawnictwa_slownik_idNazwa_wyd`),
  CONSTRAINT `fk_Nazwa_wydawnictwa_slownik_idNazwa_wyd`
    FOREIGN KEY (`Nazwa_wydawnictwa_slownik_idNazwa_wyd`)
    REFERENCES `Ksiegarnia`.`Nazwa_wydawnictwa_slownik` (`idNazwa_wyd`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Ksiegarnia`.`Ksiazka`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Ksiegarnia`.`Ksiazka` ;

CREATE TABLE IF NOT EXISTS `Ksiegarnia`.`Ksiazka` (
  `idKsiazka` INT NOT NULL AUTO_INCREMENT,
  `tytul` VARCHAR(45) NOT NULL,
  `autor` VARCHAR(45) NOT NULL,
  `opis` TEXT NULL,
  `ilosc` TINYINT UNSIGNED NOT NULL,
  `cena` TINYINT UNSIGNED NOT NULL,
  `ISBN` VARCHAR(20) NOT NULL,
  `Wydanie_idWydanie` INT NOT NULL,
  PRIMARY KEY (`idKsiazka`, `Wydanie_idWydanie`),
  CONSTRAINT `fk_Ksiazka_Wydanie1`
    FOREIGN KEY (`Wydanie_idWydanie`)
    REFERENCES `Ksiegarnia`.`Wydanie` (`idWydanie`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Ksiegarnia`.`Recenzje`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Ksiegarnia`.`Recenzje` ;

CREATE TABLE IF NOT EXISTS `Ksiegarnia`.`Recenzje` (
  `idrecenzji` MEDIUMINT NOT NULL AUTO_INCREMENT,
  `tresc` TEXT NOT NULL,
  `Klienci_idKlient` INT NOT NULL,
  `Ksiazka_idKsiazka` INT NOT NULL,
  PRIMARY KEY (`idrecenzji`, `Klienci_idKlient`, `Ksiazka_idKsiazka`),
  CONSTRAINT `fk_Recenzje_Klienci1`
    FOREIGN KEY (`Klienci_idKlient`)
    REFERENCES `Ksiegarnia`.`Klienci` (`idKlient`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Recenzje_Ksiazka1`
    FOREIGN KEY (`Ksiazka_idKsiazka`)
    REFERENCES `Ksiegarnia`.`Ksiazka` (`idKsiazka`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `Ksiegarnia`.`Status_zamowienia_slownik`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Ksiegarnia`.`Status_zamowienia_slownik` ;

CREATE TABLE IF NOT EXISTS `Ksiegarnia`.`Status_zamowienia_slownik` (
  `idStatus_zamowienia_slownik` INT NOT NULL AUTO_INCREMENT,
  `Status` CHAR(1) NOT NULL,
  PRIMARY KEY (`idStatus_zamowienia_slownik`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Ksiegarnia`.`Zamowienie`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Ksiegarnia`.`Zamowienie` ;

CREATE TABLE IF NOT EXISTS `Ksiegarnia`.`Zamowienie` (
  `idZamowienia` INT NOT NULL AUTO_INCREMENT,
  `wartosc` INT NOT NULL,
  `data` DATE NOT NULL,
  `Status_zamowienia_slownik_idStatus_zamowienia_slownik` INT NOT NULL,
  `Klienci_idKlient` INT NOT NULL,
  PRIMARY KEY (`idZamowienia`, `Status_zamowienia_slownik_idStatus_zamowienia_slownik`, `Klienci_idKlient`),
  CONSTRAINT `fk_Zamowienia_Status_zamowienia_slownik1`
    FOREIGN KEY (`Status_zamowienia_slownik_idStatus_zamowienia_slownik`)
    REFERENCES `Ksiegarnia`.`Status_zamowienia_slownik` (`idStatus_zamowienia_slownik`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Zamowienia_Klienci1`
    FOREIGN KEY (`Klienci_idKlient`)
    REFERENCES `Ksiegarnia`.`Klienci` (`idKlient`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Ksiegarnia`.`Zamowienie_has_Ksiazka`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Ksiegarnia`.`Zamowienie_has_Ksiazka` ;

CREATE TABLE IF NOT EXISTS `Ksiegarnia`.`Zamowienie_has_Ksiazka` (
  `ilosc` TINYINT NOT NULL,
  `Zamowienia_idZamowienia` INT NOT NULL,
  `Ksiazka_idKsiazka` INT NOT NULL,
  PRIMARY KEY (`Zamowienia_idZamowienia`, `Ksiazka_idKsiazka`),
  CONSTRAINT `fk_Zamowienia_has_Ksiazka_Zamowienia1`
    FOREIGN KEY (`Zamowienia_idZamowienia`)
    REFERENCES `Ksiegarnia`.`Zamowienie` (`idZamowienia`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Zamowienia_has_Ksiazka_Ksiazka1`
    FOREIGN KEY (`Ksiazka_idKsiazka`)
    REFERENCES `Ksiegarnia`.`Ksiazka` (`idKsiazka`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

/*------------------------------TRIGGERY------------------------------*/
DELIMITER $$
CREATE TRIGGER ustaw_status_zamowienie
  BEFORE INSERT ON Zamowienie
    FOR EACH ROW
      BEGIN
        SET NEW.Status_zamowienia_slownik_idStatus_zamowienia_slownik = 1;
    END$$

DELIMITER ;

/*------------------------------INDEKSY------------------------------*/
CREATE UNIQUE INDEX Ksiazka_index
ON Ksiazka (tytul, autor);


/*------------------------------WIDOKI------------------------------*/
CREATE OR REPLACE VIEW widokKsiazka AS SELECT tytul, autor, cena FROM Ksiazka;
CREATE OR REPLACE VIEW widokKlienci AS SELECT login, imie, nazwisko, email FROM Klienci;
CREATE OR REPLACE VIEW widokZamowienie AS SELECT A.wartosc, A.Status_zamowienia_slownik_idStatus_zamowienia_slownik, A.data, B.login, B.imie, B.nazwisko, B.email FROM Zamowienie A, Klienci B;


/*------------------------------ZABEZPIECZENIA------------------------------*/
SET SQL_MODE = '';
GRANT USAGE ON *.* TO user;

DROP USER admin;
DROP USER klient_zalog;
DROP USER klient_niezalog;
SET SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';
CREATE USER 'admin';
CREATE USER 'klient_zalog';
CREATE USER 'klient_niezalog';

GRANT ALL ON `Ksiegarnia`.* TO 'admin';

GRANT INSERT, SELECT, UPDATE, CREATE, DELETE ON `Ksiegarnia`.`Adres` TO 'klient_zalog';
GRANT INSERT, SELECT, UPDATE, CREATE, DELETE ON `Ksiegarnia`.`Klient` TO 'klient_zalog';
GRANT INSERT, SELECT, UPDATE ON `Ksiegarnia`.`Recenzje` TO 'klient_zalog';
GRANT SELECT ON `Ksiegarnia`.`Ksiazka` TO 'klient_zalog';
GRANT SELECT ON `Ksiegarnia`.`Kategoria_slownik` TO 'klient_zalog';
GRANT SELECT ON `Ksiegarnia`.`Wydanie` TO 'klient_zalog';
GRANT SELECT ON `Ksiegarnia`.`Nazwa_wydawnictwa_slownik` TO 'klient_zalog';
GRANT INSERT, SELECT, UPDATE ON `Ksiegarnia`.`Zamowienie` TO 'klient_zalog';
GRANT SELECT ON `Ksiegarnia`.`Status_zamowienia_slownik` TO 'klient_zalog';

GRANT SELECT ON `Ksiegarnia`.`Recenzje` TO 'klient_niezalog';
GRANT SELECT ON `Ksiegarnia`.`Ksiazka` TO 'klient_niezalog';
GRANT SELECT ON `Ksiegarnia`.`Kategoria_slownik` TO 'klient_zalog';
GRANT SELECT ON `Ksiegarnia`.`Wydanie` TO 'klient_niezalog';
GRANT SELECT ON `Ksiegarnia`.`Nazwa_wydawnictwa_slownik` TO 'klient_niezalog';


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

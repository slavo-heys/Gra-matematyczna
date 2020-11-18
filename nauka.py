from tkinter import *
import tkinter as tk
from tkinter import ttk
import sqlite3
from time import strftime
import random
from PIL import ImageTk, Image

#  Tworzenie bazy i tabel - jeśli nie istnieją
conn = sqlite3.connect('gra.db')
c = conn.cursor()
c.execute(
    """CREATE TABLE IF NOT EXISTS user(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        data text NOT NULL,
        imie text NOT NULL);""")

c.execute(
    """CREATE TABLE IF NOT EXISTS wyniki(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        imie text NOT NULL,
        rodz_gry text NOT NULL,
        dzialan text NOT NULL,
        wyn_pop text NOT NULL,
        wyn_zly text NOT NULL);""")
conn.commit()
conn.close()


class matematyka:
    def __init__(self, master):

        global zdjecie
        zdjecie = ImageTk.PhotoImage(Image.open("dziecko.jpg"))

        #global ramka
        self.punkty = 0
        self.ilGier = 0
        self.wynikPoprawny = 0
        self.wynikZly = 0
        self.ramka = tk.LabelFrame(master, padx=5, pady=5)
        self.ramka.pack(padx=2, pady=2)

        ramka1 = tk.LabelFrame(self.ramka, padx=5, pady=5)
        ramka1.pack()

        ramka2 = tk.LabelFrame(self.ramka, padx=5, pady=5)
        ramka2.pack(padx=10, pady=10)

        ramka3 = tk.LabelFrame(self.ramka, padx=5, pady=5)
        ramka3.pack(padx=10, pady=10)

        self.l = tk.Label(ramka1, image=zdjecie)
        self.l.pack()

        self.l1 = tk.Label(ramka2, text="Jak masz na imię? ",
                           font=("Arial", 15), fg="#4B0082")
        self.l1.grid(row=0, column=0)

        self.imie = StringVar()
        self.entry = tk.Entry(ramka2, textvariable=self.imie,
                              font=("Arial", 20), width=10)
        self.entry.grid(row=0, column=1)

        self.button = tk.Button(ramka2, text="START", font=(
            "Arial", 15), fg="#FF00FF", bg="#4B0082", command=self.usun_ramke)
        self.button.grid(row=0, column=2)

        self.l2 = tk.Label(ramka3, text="""Program \"Moja matematyka\" przeznaczony jest dla dzieci z klas I, II i III szkoły podstawowej. Głownym celem programu 
        jest utrwalanie działań matematycznych z zakresu dodawania, odejmowania, mnożenia i dzielenia. Program jest  w pełni 
        darmowy, z przeznaczeniem do użytku domowego. Jako autor programu chętnie przeczytam o sugestiach i problemach związanych
        z działaniem kodu, adres kontaktowy: ilodz24hd@gmail.com""", font=("Arial", 10), fg="#800080")
        self.l2.pack()

    def usun_ramke(self):
        self.ramka.destroy()
        self.wybor()

    def wybor(self):

        self.ramka = tk.LabelFrame(root, padx=5, pady=5)
        self.ramka.pack(padx=2, pady=2)

        ramka1 = tk.LabelFrame(self.ramka, padx=5, pady=5)
        ramka1.pack()

        ramka2 = tk.LabelFrame(self.ramka, padx=5, pady=5)
        ramka2.pack()

        ramka3 = tk.LabelFrame(self.ramka, padx=5, pady=5)
        ramka3.pack()

        self.linia = tk.Label(ramka1, text="Dokonaj wyboru", font=(
            "Arial", 15, "bold"), fg="#4B0082", padx=15, pady=15)
        self.linia.pack(padx=10)

        self.button = tk.Button(ramka2, text="dodawanie", font=(
            "Arial", 12), fg="#FF00FF", bg="#4B0082", command=self.dodawanie)
        self.button.pack(side=LEFT)

        self.button1 = tk.Button(ramka2, text="odejmowanie", font=(
            "Arial", 12), fg="#FF00FF", bg="#4B0082", command=self.odejmowanie)
        self.button1.pack(side=LEFT)

        self.button2 = tk.Button(ramka2, text="działania matematyczne", font=(
            "Arial", 12), fg="#FF00FF", bg="#4B0082", command=self.dzialania)
        self.button2.pack(side=LEFT)

        self.button3 = tk.Button(ramka2, text="tabela wyników", font=(
            "Arial", 12), fg="#FF00FF", bg="#4B0082", command=self.tabela_wyników)
        self.button3.pack(side=LEFT)

        self.button4 = tk.Button(ramka3, text="zamknij program", font=(
            "Arial", 12), fg="#FF00FF", bg="#4B0082", command=self.zamknij_program)
        self.button4.pack(side=LEFT)

    def zamknij_program(self):
        root.destroy()

# ************************************ dodawanie ***********************************
    def dodawanie(self):
        self.ramka.destroy()

        self.imieUsera = self.imie.get()

        self.x = random.randint(1, 10)
        self.y = random.randint(1, 10)
        self.wynik = self.x + self.y
        self.wynik = str(self.wynik)

        self.ramka = tk.LabelFrame(root, padx=5, pady=5)
        self.ramka.pack(padx=2, pady=2)

        ramka1 = tk.LabelFrame(self.ramka, padx=5, pady=5)
        ramka1.pack()

        ramka2 = tk.LabelFrame(self.ramka, padx=5, pady=5)
        ramka2.pack()

        ramka3 = tk.LabelFrame(self.ramka, padx=5, pady=5)
        ramka3.pack()

        ramka4 = tk.LabelFrame(self.ramka, padx=5, pady=5)
        ramka4.pack()

        self.linia = tk.Label(ramka1, text=self.imieUsera +
                              " ile jest:", font=("Arial", 20), fg="#FF00FF")
        self.linia.pack()

        self.linia1 = tk.Label(ramka2, text=str(
            self.x) + " + " + str(self.y) + " ", font=("Arial", 20), fg="#FF00FF")
        self.linia1.pack(side=LEFT)

        self.wynikUsera = StringVar()

        self.pole = tk.Entry(
            ramka2, textvariable=self.wynikUsera, font=("Arial", 20), width=4)
        self.pole.pack(side=LEFT)

        self.button7 = tk.Button(ramka2, text="sprawdź wynik", font=("Arial", 20), fg="#FF00FF",
                                 bg="#4B0082", command=lambda: self.dodawanie_sprawdzanie(self.wynik, self.imieUsera))
        self.button7.pack(side=LEFT)

    def dodawanie_sprawdzanie(self, wynik, imie):
        self.imieU = imie
        self.wynikGry = wynik
        self.wynikU = self.wynikUsera.get()

        if self.wynikGry == self.wynikU:
            self.ramka.destroy()
            self.punkty += 1
            self.ilGier += 1
            self.wynikPoprawny += 1
            self.ramka = tk.LabelFrame(root, padx=5, pady=5)
            self.ramka.pack()

            ramka1 = tk.LabelFrame(self.ramka, padx=5, pady=5)
            ramka1.pack()

            ramka2 = tk.LabelFrame(self.ramka, padx=5, pady=5)
            ramka2.pack()

            self.linia2 = Label(ramka1, text="Brawo! " + self.imieU+". Masz " +
                                str(self.punkty)+" punkty.", font=("Arial", 15), fg="green")
            self.linia2.pack()

            self.button8 = tk.Button(ramka2, text="graj dalej", font=(
                "Arial", 20), fg="#FF00FF", bg="#4B0082", command=self.dodawanie)
            self.button8.pack(side=LEFT)

            self.button9 = tk.Button(ramka2, text="koniec gry", font=(
                "Arial", 20), fg="#FF00FF", bg="#4B0082", command=lambda: self.zapisz_wynik("dodawanie"))
            self.button9.pack(side=LEFT)

        elif self.wynikUsera == " ":
            self.ramka.destroy()
            self.ramka = tk.LabelFrame(root, padx=5, pady=5)
            self.ramka.pack()

            ramka1 = tk.LabelFrame(self.ramka, padx=5, pady=5)
            ramka1.pack()

            ramka2 = tk.LabelFrame(self.ramka, padx=5, pady=5)
            ramka2.pack()

            self.linia2 = Label(ramka1, text="Oj coś poszło nie tak! Masz " +
                                str(self.punkty)+" punkty.", font=("Arial", 15), fg="red")
            self.linia2.pack()

            self.button8 = tk.Button(ramka2, text="graj dalej", font=(
                "Arial", 20), fg="#FF00FF", bg="#4B0082", command=self.dodawanie)
            self.button8.pack(side=LEFT)

            self.button9 = tk.Button(ramka2, text="koniec gry", font=(
                "Arial", 20), fg="#FF00FF", bg="#4B0082", command=lambda: self.zapisz_wynik("dodawanie"))
            self.button9.pack(side=LEFT)
        else:
            self.ramka.destroy()
            self.punkty -= 1
            self.ilGier += 1
            self.wynikZly += 1

            self.ramka = tk.LabelFrame(root, padx=5, pady=5)
            self.ramka.pack()

            ramka1 = tk.LabelFrame(self.ramka, padx=5, pady=5)
            ramka1.pack()

            ramka2 = tk.LabelFrame(self.ramka, padx=5, pady=5)
            ramka2.pack()

            self.linia2 = Label(ramka1, text="Oj jak mi przykro! Wynik jest zły! " +
                                self.imieU+". Masz "+str(self.punkty)+" punkty.", font=("Arial", 15), fg="red")
            self.linia2.pack()

            self.button8 = tk.Button(ramka2, text="graj dalej", font=(
                "Arial", 20), fg="#FF00FF", bg="#4B0082", command=self.dodawanie)
            self.button8.pack(side=LEFT)

            self.button9 = tk.Button(ramka2, text="koniec gry", font=(
                "Arial", 20), fg="#FF00FF", bg="#4B0082", command=lambda: self.zapisz_wynik("dodawanie"))
            self.button9.pack(side=LEFT)

    def zapisz_wynik(self, metoda):
        conn = sqlite3.connect('gra.db')
        c = conn.cursor()
        c.execute("INSERT INTO wyniki VALUES(NULL, :imie, :rodz_gry, :dzialan, :wyn_pop, :wyn_zly)",
                  {
                      'imie': self.imieU,
                      'rodz_gry': metoda,
                      'dzialan': self.ilGier,
                      'wyn_pop': self.wynikPoprawny,
                      'wyn_zly': self.wynikZly
                  })
        conn.commit()
        conn.close()
        self.usun_ramke()

# ******************************** odejmowanie ***************************
    def odejmowanie(self):
        self.ramka.destroy()

        self.imieUsera = self.imie.get()

        self.x = random.randint(1, 10)
        self.y = random.randint(1, 10)

        if self.x > self.y:
            self.wynik = self.x - self.y
            self.wynik = str(self.wynik)

            self.ramka = tk.LabelFrame(root, padx=5, pady=5)
            self.ramka.pack(padx=2, pady=2)

            ramka1 = tk.LabelFrame(self.ramka, padx=5, pady=5)
            ramka1.pack()

            ramka2 = tk.LabelFrame(self.ramka, padx=5, pady=5)
            ramka2.pack()

            ramka3 = tk.LabelFrame(self.ramka, padx=5, pady=5)
            ramka3.pack()

            ramka4 = tk.LabelFrame(self.ramka, padx=5, pady=5)
            ramka4.pack()

            self.linia = tk.Label(
                ramka1, text=self.imieUsera+" ile jest:", font=("Arial", 20), fg="#FF00FF")
            self.linia.pack()

            self.linia1 = tk.Label(ramka2, text=str(
                self.x) + " - " + str(self.y) + " ", font=("Arial", 20), fg="#FF00FF")
            self.linia1.pack(side=LEFT)

            self.wynikUsera = StringVar()

            self.pole = tk.Entry(
                ramka2, textvariable=self.wynikUsera, font=("Arial", 20), width=4)
            self.pole.pack(side=LEFT)

            self.button7 = tk.Button(ramka2, text="sprawdź wynik", font=(
                "Arial", 20), fg="#FF00FF", bg="#4B0082", command=lambda: self.odejmowanie_sprawdzanie(self.wynik, self.imieUsera))
            self.button7.pack(side=LEFT)
        else:
            self.odejmowanie()

    def odejmowanie_sprawdzanie(self, wynik, imie):
        self.imieU = imie
        self.wynikGry = wynik
        self.wynikU = self.wynikUsera.get()

        if self.wynikGry == self.wynikU:
            self.ramka.destroy()
            self.punkty += 1
            self.ilGier += 1
            self.wynikPoprawny += 1
            self.ramka = tk.LabelFrame(root, padx=5, pady=5)
            self.ramka.pack()

            ramka1 = tk.LabelFrame(self.ramka, padx=5, pady=5)
            ramka1.pack()

            ramka2 = tk.LabelFrame(self.ramka, padx=5, pady=5)
            ramka2.pack()

            self.linia2 = Label(ramka1, text="Brawo! " + self.imieU+". Masz " +
                                str(self.punkty)+" punkty.", font=("Arial", 15), fg="green")
            self.linia2.pack()

            self.button8 = tk.Button(ramka2, text="graj dalej", font=(
                "Arial", 20), fg="#FF00FF", bg="#4B0082", command=self.odejmowanie)
            self.button8.pack(side=LEFT)

            self.button9 = tk.Button(ramka2, text="koniec gry", font=(
                "Arial", 20), fg="#FF00FF", bg="#4B0082", command=lambda: self.zapisz_wynik("dodawanie"))
            self.button9.pack(side=LEFT)

        elif self.wynikUsera == " ":
            self.ramka.destroy()
            self.ramka = tk.LabelFrame(root, padx=5, pady=5)
            self.ramka.pack()

            ramka1 = tk.LabelFrame(self.ramka, padx=5, pady=5)
            ramka1.pack()

            ramka2 = tk.LabelFrame(self.ramka, padx=5, pady=5)
            ramka2.pack()

            self.linia2 = Label(ramka1, text="Oj coś poszło nie tak! Masz " +
                                str(self.punkty)+" punkty.", font=("Arial", 15), fg="red")
            self.linia2.pack()

            self.button8 = tk.Button(ramka2, text="graj dalej", font=(
                "Arial", 20), fg="#FF00FF", bg="#4B0082", command=self.odejmowanie)
            self.button8.pack(side=LEFT)

            self.button9 = tk.Button(ramka2, text="koniec gry", font=(
                "Arial", 20), fg="#FF00FF", bg="#4B0082", command=lambda: self.zapisz_wynik("dodawanie"))
            self.button9.pack(side=LEFT)
        else:
            self.ramka.destroy()
            self.punkty -= 1
            self.ilGier += 1
            self.wynikZly += 1

            self.ramka = tk.LabelFrame(root, padx=5, pady=5)
            self.ramka.pack()

            ramka1 = tk.LabelFrame(self.ramka, padx=5, pady=5)
            ramka1.pack()

            ramka2 = tk.LabelFrame(self.ramka, padx=5, pady=5)
            ramka2.pack()

            self.linia2 = Label(ramka1, text="Oj jak mi przykro! Wynik jest zły! " +
                                self.imieU+". Masz "+str(self.punkty)+" punkty.", font=("Arial", 15), fg="red")
            self.linia2.pack()

            self.button8 = tk.Button(ramka2, text="graj dalej", font=(
                "Arial", 20), fg="#FF00FF", bg="#4B0082", command=self.odejmowanie)
            self.button8.pack(side=LEFT)

            self.button9 = tk.Button(ramka2, text="koniec gry", font=(
                "Arial", 20), fg="#FF00FF", bg="#4B0082", command=lambda: self.zapisz_wynik_odejmowanie("odejmowanie"))
            self.button9.pack(side=LEFT)

    def zapisz_wynik_odejmowanie(self, metoda):
        conn = sqlite3.connect('gra.db')
        c = conn.cursor()
        c.execute("INSERT INTO wyniki VALUES(NULL, :imie, :rodz_gry, :dzialan, :wyn_pop, :wyn_zly)",
                  {
                      'imie': self.imieU,
                      'rodz_gry': metoda,
                      'dzialan': self.ilGier,
                      'wyn_pop': self.wynikPoprawny,
                      'wyn_zly': self.wynikZly
                  })
        conn.commit()
        conn.close()
        self.usun_ramke()

# ****************************** dzialania matematyczne*************************************
    def dzialania(self):
        self.ramka.destroy()

        self.imieUsera = self.imie.get()

        self.x = random.randint(1, 10)
        self.y = random.randint(1, 10)

        if self.y > self.x:
            self.wynik = self.y - self.x
            self.wynik = str(self.wynik)

            self.ramka = tk.LabelFrame(root, padx=5, pady=5)
            self.ramka.pack(padx=2, pady=2)

            ramka1 = tk.LabelFrame(self.ramka, padx=5, pady=5)
            ramka1.pack()

            ramka2 = tk.LabelFrame(self.ramka, padx=5, pady=5)
            ramka2.pack()

            ramka3 = tk.LabelFrame(self.ramka, padx=5, pady=5)
            ramka3.pack()

            ramka4 = tk.LabelFrame(self.ramka, padx=5, pady=5)
            ramka4.pack()

            self.linia = tk.Label(
                ramka1, text=self.imieUsera+" jakiej liczby brakuje?", font=("Arial", 20), fg="#FF00FF")
            self.linia.pack()

            self.linia1 = tk.Label(ramka2, text=str(
                self.x) + " + ? = " + str(self.y), font=("Arial", 20), fg="#FF00FF")
            self.linia1.pack(side=LEFT)

            self.wynikUsera = StringVar()

            self.pole = tk.Entry(
                ramka2, textvariable=self.wynikUsera, font=("Arial", 20), width=4)
            self.pole.pack(side=LEFT)

            self.button7 = tk.Button(ramka2, text="sprawdź wynik", font=(
                "Arial", 20), fg="#FF00FF", bg="#4B0082", command=lambda: self.dzialania_sprawdzanie(self.wynik, self.imieUsera))
            self.button7.pack(side=LEFT)
        else:
            self.dzialania()

    def dzialania_sprawdzanie(self, wynik, imie):
        self.imieU = imie
        self.wynikGry = wynik
        self.wynikU = self.wynikUsera.get()

        if self.wynikGry == self.wynikU:
            self.ramka.destroy()
            self.punkty += 1
            self.ilGier += 1
            self.wynikPoprawny += 1
            self.ramka = tk.LabelFrame(root, padx=5, pady=5)
            self.ramka.pack()

            ramka1 = tk.LabelFrame(self.ramka, padx=5, pady=5)
            ramka1.pack()

            ramka2 = tk.LabelFrame(self.ramka, padx=5, pady=5)
            ramka2.pack()

            self.linia2 = Label(ramka1, text="Brawo! " + self.imieU+". Masz " +
                                str(self.punkty)+" punkty.", font=("Arial", 15), fg="green")
            self.linia2.pack()

            self.button8 = tk.Button(ramka2, text="graj dalej", font=(
                "Arial", 20), fg="#FF00FF", bg="#4B0082", command=self.dzialania)
            self.button8.pack(side=LEFT)

            self.button9 = tk.Button(ramka2, text="koniec gry", font=(
                "Arial", 20), fg="#FF00FF", bg="#4B0082", command=lambda: self.zapisz_wynik("dodawanie"))
            self.button9.pack(side=LEFT)

        elif self.wynikUsera == " ":
            self.ramka.destroy()
            self.ramka = tk.LabelFrame(root, padx=5, pady=5)
            self.ramka.pack()

            ramka1 = tk.LabelFrame(self.ramka, padx=5, pady=5)
            ramka1.pack()

            ramka2 = tk.LabelFrame(self.ramka, padx=5, pady=5)
            ramka2.pack()

            self.linia2 = Label(ramka1, text="Oj coś poszło nie tak! Masz " +
                                str(self.punkty)+" punkty.", font=("Arial", 15), fg="red")
            self.linia2.pack()

            self.button8 = tk.Button(ramka2, text="graj dalej", font=(
                "Arial", 20), fg="#FF00FF", bg="#4B0082", command=self.dzialania)
            self.button8.pack(side=LEFT)

            self.button9 = tk.Button(ramka2, text="koniec gry", font=(
                "Arial", 20), fg="#FF00FF", bg="#4B0082", command=lambda: self.zapisz_wynik("dodawanie"))
            self.button9.pack(side=LEFT)
        else:
            self.ramka.destroy()
            self.punkty -= 1
            self.ilGier += 1
            self.wynikZly += 1

            self.ramka = tk.LabelFrame(root, padx=5, pady=5)
            self.ramka.pack()

            ramka1 = tk.LabelFrame(self.ramka, padx=5, pady=5)
            ramka1.pack()

            ramka2 = tk.LabelFrame(self.ramka, padx=5, pady=5)
            ramka2.pack()

            self.linia2 = Label(ramka1, text="Oj jak mi przykro! Wynik jest zły! " +
                                self.imieU+". Masz "+str(self.punkty)+" punkty.", font=("Arial", 15), fg="red")
            self.linia2.pack()

            self.button8 = tk.Button(ramka2, text="graj dalej", font=(
                "Arial", 20), fg="#FF00FF", bg="#4B0082", command=self.dzialania)
            self.button8.pack(side=LEFT)

            self.button9 = tk.Button(ramka2, text="koniec gry", font=(
                "Arial", 20), fg="#FF00FF", bg="#4B0082", command=lambda: self.zapisz_wynik_dzialania("działania"))
            self.button9.pack(side=LEFT)

    def zapisz_wynik_dzialania(self, metoda):
        conn = sqlite3.connect('gra.db')
        c = conn.cursor()
        c.execute("INSERT INTO wyniki VALUES(NULL, :imie, :rodz_gry, :dzialan, :wyn_pop, :wyn_zly)",
                  {
                      'imie': self.imieU,
                      'rodz_gry': metoda,
                      'dzialan': self.ilGier,
                      'wyn_pop': self.wynikPoprawny,
                      'wyn_zly': self.wynikZly
                  })
        conn.commit()
        conn.close()
        self.usun_ramke()


# ******************************* tabela wyników **********************************


    def tabela_wyników(self):
        self.ramka.destroy()

        self.ramka = tk.LabelFrame(root, padx=5, pady=5)
        self.ramka.pack(padx=2, pady=2)

        ramka1 = tk.LabelFrame(self.ramka, padx=5, pady=5)
        ramka1.pack()

        ramka2 = tk.LabelFrame(self.ramka, padx=5, pady=5)
        ramka2.pack()

        ramka3 = tk.LabelFrame(self.ramka, padx=5, pady=5)
        ramka3.pack()

        self.nap = tk.Label(ramka1, text=" Tabela ostatnich wyników", font=(
            "Arial", 30), fg="#9400D3")
        self.nap.pack()

        self.nap1 = tk.Label(ramka2, text=" lp ",
                             font=("Arial", 15), fg="#8B008B")
        self.nap1.grid(row=0, column=0)

        self.nap2 = tk.Label(ramka2, text=" Imie zawodnika ",
                             font=("Arial", 15), fg="#8B008B")
        self.nap2.grid(row=0, column=1)

        self.nap1 = tk.Label(ramka2, text=" Rodzaj gry ",
                             font=("Arial", 15), fg="#8B008B")
        self.nap1.grid(row=0, column=2)

        self.nap1 = tk.Label(ramka2, text=" Ilość gier ",
                             font=("Arial", 15), fg="#8B008B")
        self.nap1.grid(row=0, column=3)

        self.nap1 = tk.Label(ramka2, text=" Poprawne wyniki ",
                             font=("Arial", 15), fg="#8B008B")
        self.nap1.grid(row=0, column=4)

        self.nap1 = tk.Label(ramka2, text=" Złe wyniki ",
                             font=("Arial", 15), fg="#8B008B")
        self.nap1.grid(row=0, column=5)

        z = 1
        conn = sqlite3.connect('gra.db')
        c = conn.cursor()
        c.execute("SELECT * FROM wyniki ORDER BY id DESC LIMIT 20")
        records = c.fetchall()
        for rect in records:
            tk.Label(ramka2, text=str(rect[0]), font=(
                "Arial", 10), fg="#9400D3").grid(row=z, column=0)

            tk.Label(ramka2, text=str(rect[1]), font=(
                "Arial", 10), fg="#9400D3").grid(row=z, column=1)

            tk.Label(ramka2, text=str(rect[2]), font=(
                "Arial", 10), fg="#9400D3").grid(row=z, column=2)

            tk.Label(ramka2, text=str(rect[3]), font=(
                "Arial", 10), fg="#9400D3").grid(row=z, column=3)

            tk.Label(ramka2, text=str(rect[4]), font=(
                "Arial", 10), fg="#9400D3").grid(row=z, column=4)

            tk.Label(ramka2, text=str(rect[5]), font=(
                "Arial", 10), fg="#9400D3").grid(row=z, column=5)
            z += 1

        self.button5 = tk.Button(ramka3, text="powrót do gry", font=(
            "Arial", 12), fg="#FF00FF", bg="#4B0082", command=self.usun_ramke)
        self.button5.pack(side=LEFT)

        self.button6 = tk.Button(ramka3, text="koniec gry", font=(
            "Arial", 12), fg="#FF00FF", bg="#4B0082", command=self.zamknij_program)
        self.button6.pack(side=LEFT)


def wybor():
    conn = sqlite3.connect('gra.db')
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM user")
    records = c.fetchone()
    row = records[0]
    if row > 0:
        matematyka(root)
    else:
        return


root = tk.Tk()
root.geometry("800x600+100+100")  # rozmiar i położenie okna
root.title("Moja matematyka")  # tytuł okna
root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='abacus.png'))
root.resizable(False, False)  # blokowanie rozmiaru okienka

wybor()  # uruchomienie programu

root.mainloop()

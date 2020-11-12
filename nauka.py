from tkinter import *
import tkinter as tk
from tkinter import ttk
import sqlite3
from time import strftime
import time
import datetime as dt
import random

# *************************************** baza ******************************************************
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

# ******************************** Okno wstepu programu *********************************************


def gra():

    def wynik():

        def wyczysc():

            ram.destroy()
            gra()

        def koniec():
            ram.destroy()
            tamka = tk.LabelFrame(root, padx=0, pady=0)
            tamka.pack(padx=10, pady=10)

            tamka1 = tk.LabelFrame(tamka, padx=10, pady=10)
            tamka1.pack(padx=10, pady=10)

            tamka2 = tk.LabelFrame(tamka, padx=10, pady=10)
            tamka2.pack(padx=10, pady=10)

            tamka3 = tk.LabelFrame(tamka, padx=10, pady=10)
            tamka3.pack(padx=10, pady=10)

            inia = tk.Label(tamka1, text=imieUsera+"! Zdobyłeś " +
                            str(punkty)+" punktów.", font=("Arial", 20), fg="#8B008B")
            inia.pack()

            inia1 = tk.Label(tamka2, text="Poprawne odpowiedzi: " +
                             str(wynikPoprawny)+" razy.", font=("Arial", 20), fg="green")
            inia1.pack()

            inia2 = tk.Label(tamka3, text="Złe odpowiedzi: " +
                             str(wynikZly)+" razy.", font=("Arial", 20), fg="red")
            inia2.pack()

        ra.destroy()
        # wynikUsera=wynikUsera.get()
        wynikUsera2 = str(wynikUsera.get())
        wynikUsera2 = int(wynikUsera2)

        global punkty
        global wynikPoprawny
        global wynikZly

        # ramki
        ram = tk.LabelFrame(root, padx=10, pady=10)
        ram.pack(padx=10, pady=10)

        ram1 = tk.LabelFrame(ram, padx=10, pady=10)
        ram1.pack(padx=10, pady=10, side=TOP)

        ram2 = tk.LabelFrame(ram, padx=10, pady=10)
        ram2.pack(padx=10, pady=10, side=TOP)

        ram3 = tk.LabelFrame(ram, padx=10, pady=10)
        ram3.pack(padx=10, pady=10, side=TOP)

        if wynikUsera2 == wynikProgramu:
            linia = tk.Label(ram1, text="Brawo "+imieUsera +
                             "! Zdobyłeś 1 punkt", font=("Arial", 30), fg="green")
            linia.pack()
            punkty += 1
            wynikPoprawny += 1

        else:
            linia = tk.Label(ram1, text="Oj "+imieUsera +
                             "! Wynik jest błędny", font=("Arial", 30), fg="red")
            linia.pack()
            wynikZly += 1

        button = tk.Button(ram2, text="Zagraj ponownie", font=(
            "Arial", 15), fg="#8B008B", command=wyczysc)
        button.pack()

        button1 = tk.Button(ram3, text="Koniec Gry", font=(
            "Arial", 15), fg="#8B008B", command=koniec)
        button1.pack()

    conn = sqlite3.connect('gra.db')
    c = conn.cursor()
    c.execute("SELECT * FROM user ORDER BY id DESC LIMIT 1")
    records = c.fetchall()
    for rec in records:
        imieUsera = str(rec[2])

    x = random.randint(1, 11)
    y = random.randint(1, 11)
    wynikProgramu = x+y

    # ramki
    ra = tk.LabelFrame(root, padx=10, pady=10)
    ra.pack(padx=10, pady=10, side=TOP)

    ra1 = tk.LabelFrame(ra, padx=10, pady=10)
    ra1.pack(padx=10, pady=10, side=TOP)

    ra2 = tk.LabelFrame(ra, padx=10, pady=10)
    ra2.pack(padx=10, pady=10, side=TOP)

    ra3 = tk.LabelFrame(ra, padx=10, pady=10)
    ra3.pack(padx=10, pady=10, side=TOP)

    wynikUsera = StringVar()

    li = tk.Label(ra1, text=imieUsera+" ile jest?",
                  font=("Arial", 20), fg="#8B008B")
    li.pack()

    li0 = tk.Label(ra2, text=str(x)+" + "+str(y),
                   font=("Arial", 40, "bold"), fg="#8B008B")
    li0.pack()

    li1 = tk.Entry(ra3, textvariable=wynikUsera, font=("Arial", 30), width=4)
    li1.pack()

    bu = tk.Button(ra3, text="Sprawdź wynik", font=(
        "Arial", 20), fg="#8B008B", command=wynik)
    bu.pack()


def start():
    # zapisz użytkownika i przejdz dalej
    def zapisz():
        date = strftime('%D')
        hour = strftime('%T')
        czas = date+"  "+hour
        conn = sqlite3.connect('gra.db')
        c = conn.cursor()
        c.execute("INSERT INTO user VALUES(NULL, :data, :imie)",
                  {
                      'data': czas,
                      'imie': imie.get()
                  })
        conn.commit()
        conn.close()
        r.destroy()
        gra()

    # ramki
    r = tk.LabelFrame(root, padx=10, pady=10)
    r.pack(padx=20, pady=20, side=TOP)

    r0 = tk.LabelFrame(r, padx=10, pady=10)
    r0.pack(padx=20, pady=20, side=TOP)

    r1 = tk.LabelFrame(r, padx=10, pady=10)
    r1.pack(padx=20, pady=20, side=TOP)

    r2 = tk.LabelFrame(r, padx=10, pady=10)
    r2.pack(padx=20, pady=20, side=TOP)

    r3 = tk.LabelFrame(r, padx=10, pady=10)
    r3.pack(padx=20, pady=20, side=TOP)

    l = tk.Label(r0, text="Witaj w programie \"Gra matematyczna\".",
                 font=("Arial", 20), fg="#8B008B")
    l.pack()

    l1 = tk.Label(r1, text="Podaj swoje imie",
                  font=("Arial", 20), fg="#8B008B")
    l1.pack()

    e = tk.Entry(r2, textvariable=imie, font=("Arial", 15), width=15)
    e.pack()

    b = tk.Button(r3, text="zapisz", command=zapisz)
    b.pack()


# Tworzenie okna
root = tk.Tk()
root.geometry("800x600+100+100")
root.title("Moja nauka")

# Blokada geometrii okna
root.resizable(False, False)

# Likwidacja paska stanu
# root.overrideredirect(True)
punkty = 0
wynikPoprawny = 0
wynikZly = 0


imie = StringVar()


start()  # start programu
root.mainloop()
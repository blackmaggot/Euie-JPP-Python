__author__ = 'blackmaggot'
from exircises import FirstExircise
class Selector:
    print(" 1. funkcja czyPalindrom \n 2. Konwerter stopni z C na F \n 3. Wyszukiwarka najwiekszej liczby z listy")
    def exircise_chooser(self, selecta = int(raw_input("Wprowadz nmer zadania: "))):

        if selecta == 1:
            firstt = FirstExircise.FirstExircise()
            firstt.czy_palindrom(raw_input("Wprowadz slowo"))
    exircise_chooser()




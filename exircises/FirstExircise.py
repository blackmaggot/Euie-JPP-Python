__author__ = 'WiktorMarchewka'


class FirstExircise:

    def czy_palindrom(self,):
        #wprowadzanie slowa do sprawdzenia
        input_word = raw_input("wprowadz slowo")
        #odwracanie slowa i zapisanie go pod nowa zmienna
        reversedWord = input_word[::-1]
        #walidacja dwoch zmiennych ze slowami
        if (reversedWord == input_word):
            print("Slowo " + input_word + " jest palindromem")
        else:
            print("Slowo " + input_word + " nie jest palindromem")
#wywolanie
executeExircise = FirstExircise()
executeExircise.czy_palindrom()

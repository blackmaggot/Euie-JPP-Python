__author__ = 'WiktorMarchewka'


class FirstExircise:

    def czy_palindrom(self,):
        input_word = raw_input("wprowadz slowo")
        reversedWord = input_word[::-1]
        if (reversedWord == input_word):
            print("Slowo " + input_word + " jest palindromem")
        else:
            print("Slowo " + input_word + " nie jest palindromem")

executeExircise = FirstExircise()
executeExircise.czy_palindrom()
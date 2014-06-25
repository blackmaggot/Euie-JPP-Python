# coding=utf-8
__author__ = 'WiktorMarchewka'

class NumbersTriangle:
    def __init__(self):
        self.rows_number = 10
    def building_triangle(self):
        for x in range(1, self.rows_number+1):
            iterate = [x]
            while (len(iterate) < x):
                iterate.extend([(iterate[-1]+x)])
            listToString = ' '.join(str(z) for z in iterate)
            print(listToString)


#Wysokość trójkąta definiowana w konstruktorze klasy
test = NumbersTriangle().building_triangle()
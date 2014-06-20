__author__ = 'WiktorMarchewka'

class NumbersTriangle:
    def __init__(self):
        self.rows_number = 1100
    def building_triangle(self):
        for x in range(1, self.rows_number):
            iterate = [x]
            while (len(iterate) < x):
                iterate.extend([(iterate[-1]+x)])
            listToString = ' '.join(str(z) for z in iterate)
            print(listToString)



test = NumbersTriangle().building_triangle()

# dupa = [1,2,3,4,5]
# dupastring = ' '.join(str(e) for e in dupa)
# print(dupastring)




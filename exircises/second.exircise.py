__author__ = 'WiktorMarchewka'


class TempConverter:
    def CdoF(self, celsius_degrees):
        farenheit_degrees = 1.8*celsius_degrees+32
        return farenheit_degrees



temp = TempConverter()
print(temp.CdoF(100))
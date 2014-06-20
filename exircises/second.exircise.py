__author__ = 'WiktorMarchewka'
import unittest


class TempConverter:
    def CdoF(self, celsius_degrees):
        farenheit_degrees = 1.8*celsius_degrees+32
        return farenheit_degrees

class TempConverterTest(unittest.TestCase):
    enumValues = (
        (0, 32),
        (10, 50),
        (20, 68),
        (30, 86),
        (40, 104),
        (50, 122),
        (60, 140),
        (70, 158),
        (80, 176),
        (90, 194),
        (100, 212)
    )
    def ConverterTest(self):
        for celcius, farenheit in self.enumValues:
            result = TempConverter.CdoF(celcius)
            self.assertEqual(farenheit, result)
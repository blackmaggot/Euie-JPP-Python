__author__ = 'WiktorMarchewka'
import sqlite3 as lite

class Singleton(object):

    con = lite.connect('uczelnia.db')
    cur = con.cursor()
    encode = "utf-8"


    def __init__(self, eldorado):
        self.eldorado = eldorado
        self.instance = None
    def __call__(self, *args, **kwargs):
        if self.instance is None:
            self.instance = self.eldorado(*args, **kwargs)
        return self.instance


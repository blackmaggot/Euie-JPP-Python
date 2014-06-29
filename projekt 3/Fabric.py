__author__ = 'WiktorMarchewka'
import sqlite3 as lite
from Singleton import *
from calldd import *

@Singleton
class Fabric(object):
    def getFromDb(self, whatSelect, fromSelect):
        with Singleton.con:
            cur = Singleton.cur
            dataArray = []
            data = cur.execute("select " + whatSelect + " from " + fromSelect + "").fetchall()
            print(len(data[0]), data)

            if len(data[0]) == 1:
                for i in range(0, len(data)):
                    column0 = str(data[i][0]).encode(Singleton.encode)
                    dataArray.append(column0)
            elif len(data[0]) == 2:
                for i in range(0, len(data)):
                    column0 = str(data[i][0]).encode(Singleton.encode)
                    column1 = str(data[i][1]).encode(Singleton.encode)
                    dataArray.append([column0, column1])
            elif len(data[0]) == 3:
                for i in range(0, len(data)):
                    column0 = str(data[i][0]).encode(Singleton.encode)
                    column1 = str(data[i][1]).encode(Singleton.encode)
                    column3 = str(data[i][2]).encode(Singleton.encode)
                    dataArray.append([column0, column1, column3])
            elif len(data[0]) == 4:
                for i in range(0, len(data)):
                    column0 = str(data[i][0]).encode(Singleton.encode)
                    column1 = str(data[i][1]).encode(Singleton.encode)
                    column3 = str(data[i][2]).encode(Singleton.encode)
                    column4 = str(data[i][3]).encode(Singleton.encode)
                    dataArray.append([column0, column1, column3, column4])
            elif len(data[0]) == 5:
                for i in range(0, len(data)):
                    column0 = str(data[i][0]).encode(Singleton.encode)
                    column1 = str(data[i][1]).encode(Singleton.encode)
                    column3 = str(data[i][2]).encode(Singleton.encode)
                    column4 = str(data[i][3]).encode(Singleton.encode)
                    column5 = str(data[i][4]).encode(Singleton.encode)
                    dataArray.append([column0, column1, column3, column4, column5])
            elif len(data[0]) == 6:
                for i in range(0, len(data)):
                    column0 = str(data[i][0]).encode(Singleton.encode)
                    column1 = str(data[i][1]).encode(Singleton.encode)
                    column3 = str(data[i][2]).encode(Singleton.encode)
                    column4 = str(data[i][3]).encode(Singleton.encode)
                    column5 = str(data[i][4]).encode(Singleton.encode)
                    column6 = str(data[i][5]).encode(Singleton.encode)
                    dataArray.append([column0, column1, column3, column4, column5, column6])

            return dataArray


test = Fabric()
print(test.getFromDb('*', 'subjects'))


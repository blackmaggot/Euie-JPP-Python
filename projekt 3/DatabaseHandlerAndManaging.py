from symbol import return_stmt

__author__ = 'blackmaggot'
import sqlite3 as lite


class DatabaseHandlerAndManaging(object):
    con = lite.connect('uczelnia.db')
    def getFromDb(self, table):
        with self.con:
            cur = self.con.cursor()
            # cur.execute("drop table Students")
            # cur.execute("CREATE TABLE Students(id INTEGER PRIMARY KEY AUTOINCREMENT, indexNumber INT, firstName TEXT, sureName TEXT, pesel TEXT, adress TEXT)")
            #cur.execute("INSERT INTO Students(indexNumber, firstName, sureName, pesel, adress) VALUES(2, 'Darek', 'Sekacz', '8888', 'daleko6')")
            #cur.execute("INSERT INTO Students(indexNumber, firstName, sureName, pesel, adress) VALUES(4, 'DarekMalejonek', 'Dureta', '67777777', 'daleko5')")
            p = cur.execute("select * from "+table).fetchall()
            firstNamesList = []
            for i in range(0, len(p)):
                # encodedString = str(row).encode("utf-8")
                encodedStringIndex = str(p[i][0]).encode("utf-8")
                encodedStringName = str(p[i][1]).encode("utf-8")
                encodedStringSurename = str(p[i][2]).encode("utf-8")
                encodedStringPesel = str(p[i][3]).encode("utf-8")

                firstNamesList.append([encodedStringIndex, encodedStringName, encodedStringSurename, encodedStringPesel])
            return firstNamesList

    def checkIfInListExist(self, inputList, checkedInput):
        out = []
        for x in range(0, len(inputList)):
            if checkedInput in inputList[x]:
                out.append(inputList[x])
        if not out:
            return False
        else:
            return out

    def exportListFromDict(self, list, outParameter):
        listFromDict = []
        for i in range(len(list)):
            listFromDict.append(list[i].get(outParameter))
        return listFromDict

    def updateStudent(self, indexNumber, firstName, sureName, pesel):
        with self.con:
            cur = self.con.cursor()
            cur.execute("update students set firstName ='"+firstName+"', sureName ='"+sureName+"', pesel ='"+pesel+"' where id="+indexNumber+"")



test = DatabaseHandlerAndManaging()
print(test.getFromDb('lecturers'))

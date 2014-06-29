from symbol import return_stmt

__author__ = 'WiktorMarchewka'
import sqlite3 as lite
from Singleton import *


class DatabaseHandlerAndManaging(object):
    con = lite.connect('uczelnia.db')
    def getFromDb(self, table):
        with Singleton.con:
            cur = Singleton.cur
            # cur.execute("drop table Students")
            # cur.execute("CREATE TABLE Students(id INTEGER PRIMARY KEY AUTOINCREMENT, indexNumber INT, firstName TEXT, sureName TEXT, pesel TEXT, adress TEXT)")
            #cur.execute("INSERT INTO Students(indexNumber, firstName, sureName, pesel, adress) VALUES(2, 'Darek', 'Sekacz', '8888', 'daleko6')")
            #cur.execute("INSERT INTO Students(indexNumber, firstName, sureName, pesel, adress) VALUES(4, 'DarekMalejonek', 'Dureta', '67777777', 'daleko5')")
            p = cur.execute("select * from "+table).fetchall()
            firstNamesList = []
            for i in range(0, len(p)):
                # encodedString = str(row).encode(Singleton.encode)
                encodedStringIndex = str(p[i][0]).encode(Singleton.encode)
                encodedStringName = str(p[i][1]).encode(Singleton.encode)
                encodedStringSurename = str(p[i][2]).encode(Singleton.encode)
                encodedStringPesel = str(p[i][3]).encode(Singleton.encode)

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
        with Singleton.con:
            cur = Singleton.cur
            cur.execute("update students set firstName ='"+firstName+"', sureName ='"+sureName+"', pesel ='"+pesel+"' where id="+indexNumber+"")
    def updateLecturer(self, firstName, sureName, pesel, lecturerNo):
        with Singleton.con:
            cur = Singleton.cur
            cur.execute("update Lecturers set firstName ='"+firstName+"', sureName ='"+sureName+"', pesel ='"+pesel+"' where id='"+lecturerNo+"'")

    def insertNewStudent(self, firstName, sureName, pesel, adress):
        with Singleton.con:
            cur = Singleton.cur
            cur.execute("insert into students (firstName, sureName, pesel, adress) values ('"+firstName+"', '"+sureName+"', '"+pesel+"', '"+adress+"')")

    def insertNewGroup(self, spec):
        with Singleton.con:
            cur = Singleton.cur
            cur.execute("insert into groups (groupSpecialisation) values ('"+spec+"')")

    def insertNewSubject(self, subjectName):
        with Singleton.con:
            cur = Singleton.cur
            cur.execute("insert into subjects (subjectName) values ('"+subjectName+"')")

    def insertNewSpecialisation(self, specName):
        with Singleton.con:
            cur = Singleton.cur
            cur.execute("insert into specialisations (specialisationName) values ('"+specName+"')")

    def insertNewSpecialisationSubjects(self, specName, subjectName):
        with Singleton.con:
            cur = Singleton.cur
            cur.execute("insert into specialisations (specialisationName, specialisationSubjects) values ('"+specName+"','"+subjectName+"')")


    def getSubjectsFromDb(self): #done
        with Singleton.con:
            cur = Singleton.cur
            p = cur.execute("select * from subjects").fetchall()
            subjectList = []
            for i in range(0, len(p)):
                encodedStringSubjectName = str(p[i]).encode(Singleton.encode)
                subjectList.append(encodedStringSubjectName)
            return subjectList



    def getSpecialisationsList(self): #done
        with Singleton.con:
            cur = Singleton.cur
            p = cur.execute("select specialisationName from specialisations").fetchall()
            specialisations = []

            for i in range(0, len(p)):
                encodedStringSubjectName = str(p[i][0]).encode(Singleton.encode)
                if encodedStringSubjectName not in specialisations:
                    specialisations.append(encodedStringSubjectName)
                else:
                    print("eldorado")
            return specialisations


    def getGroupsList(self): #done
        with Singleton.con:
            cur = Singleton.cur
            p = cur.execute("select * from groups").fetchall()
            groups = []

            for i in range(0, len(p)):
                encodedStringGroupNo = str(p[i][0]).encode(Singleton.encode)
                encodedStringGroupSpec = str(p[i][1]).encode(Singleton.encode)
                groups.append([encodedStringGroupNo, encodedStringGroupSpec])

            return groups

    def getSpecialisationTopicsList(self, specName):
        with Singleton.con:
            cur = Singleton.cur
            p = cur.execute("SELECT specialisationSubjects from specialisations where specialisationName = '"+specName+"'").fetchall()
            specialisationsTopics = []

            for i in range(0, len(p)):
                encodedStringSubjectName = str(p[i][0]).encode(Singleton.encode)
                specialisationsTopics.append(encodedStringSubjectName)
            return specialisationsTopics


test = DatabaseHandlerAndManaging()
print(test.getSubjectsFromDb())

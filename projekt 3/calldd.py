from PyQt4 import QtGui
from PyQt4.QtCore import QString

__author__ = 'WiktorMarchewka'
import sys
from uczelnia3 import *
from DatabaseHandlerAndManaging import *
from Fabric import *


class MyForm(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.dbHandler = DatabaseHandlerAndManaging()
        self.fabric = Fabric()

        self.subjectsListPopulate()
        self.groupsListPopulate()
        self.specialisationsListPopulate()
        self.studentDynamicFilling()
        self.lecturerDynamicFilling()


        self.ui.studentBrowser.textChanged.connect(self.studentDynamicFilling)
        self.ui.lecturerBrowser.textChanged.connect(self.lecturerDynamicFilling)

        self.ui.tableWidget.itemClicked.connect(self.setLineEditsWithDataFromTable)
        self.ui.tableWidgetLecturer.itemClicked.connect(self.setLineEditsWithDataFromLecturersTable)
        self.ui.specialisationsList.itemClicked.connect(self.setSubjectsForSpecialisation)

        self.ui.newGroupSubmitButton.clicked.connect(self.insertGroup)
        self.ui.studentEditDataButton.clicked.connect(self.updateStudentData)
        self.ui.newStudentSubmitButton.clicked.connect(self.insertStudent)
        self.ui.newSubjectButton.clicked.connect(self.insertSubject)
        self.ui.newSpecialisationSubmitButton.clicked.connect(self.insertSpec)
        self.ui.addSubjectToSpecialisationSubmitButton.clicked.connect(self.insertSubjectToSpec)
        self.ui.lecturerEditDataButton.clicked.connect(self.updateLecturerData)

    def updateStudentData(self):
        firstName = str(self.ui.studentFirstNameField.text())
        sureName = str(self.ui.studentSureNameField.text())
        pesel = str(self.ui.studentPeselNameField.text())
        indexNumber = str(self.ui.studentIndexNumberField.text())
        if all([len(firstName) != 0, len(indexNumber) != 0, len(sureName) != 0, len(pesel) != 0]):
            self.dbHandler.updateStudent(indexNumber, firstName, sureName, pesel)
        else:
            print "all fields must be filled with data"
        self.ui.tableWidget.clear()
        self.studentDynamicFilling()


    def updateLecturerData(self):
        firstName = str(self.ui.lecturerFirstNameField_3.text())
        sureName = str(self.ui.lecturerSureNameField_3.text())
        pesel = str(self.ui.lecturerPeselNameField_3.text())
        lecturerNo = str(self.ui.lecturerNo.text())
        if all([len(firstName) != 0, len(sureName) != 0, len(pesel) != 0]):
            self.dbHandler.updateLecturer(firstName, sureName, pesel, lecturerNo)
        else:
            print "all fields must be filled with data"
        self.ui.tableWidgetLecturer.clear()
        self.lecturerDynamicFilling()


    def insertStudent(self):
        firstName = str(self.ui.newStudentFirstNameField.text())
        sureName = str(self.ui.newStudentSureNameField.text())
        pesel = str(self.ui.newStudentPeselNameField.text())
        adress = str(self.ui.newStudentAdressField.text())
        if all([len(firstName) != 0, len(adress) != 0, len(sureName) != 0, len(pesel) != 0]):
            self.dbHandler.insertNewStudent(firstName, sureName, pesel, adress)
            self.ui.newStudentFirstNameField.clear()
            self.ui.newStudentSureNameField.clear()
            self.ui.newStudentPeselNameField.clear()
            self.ui.newStudentAdressField.clear()
        else:
            print "all fields must be filled with data"
        self.ui.tableWidget.clear()
        self.studentDynamicFilling()


    def insertGroup(self):
        spec = str(self.ui.specialisationsComboList.currentText())
        self.dbHandler.insertNewGroup(spec)
        self.ui.groupsListTableWidget.clear()
        self.groupsListPopulate()


    def insertSpec(self):
        specName = str(self.ui.newSpecialisationField.text())
        if len(specName) != 0:
            self.dbHandler.insertNewSpecialisation(specName)
            self.ui.newSpecialisationField.clear()
            self.specialisationsListPopulate()



    def insertSubject(self):
        subjectName= str(self.ui.newSubjectField.text())
        if len(subjectName) != 0:
            self.dbHandler.insertNewSubject(subjectName)
            self.ui.newSubjectField.clear()
            self.subjectsListPopulate()

        else:
            print "all fields must be filled with data"

    def insertSubjectToSpec(self):
        specSelected = self.ui.specialisationsList.currentRow()
        selectedSpecValue = str(self.ui.specialisationsList.item(specSelected, 0).text())
        subjectName = str(self.ui.subjectsListForSpecialisation.currentText())
        if len(subjectName) != 0:
            self.dbHandler.insertNewSpecialisationSubjects(selectedSpecValue, subjectName)
            self.ui.newSubjectField.clear()
            self.subjectsListPopulate()
        self.ui.specjalisationsSubjectsList.clear()
        self.setSubjectsForSpecialisation()




    def setLineEditsWithDataFromTable(self):
        row = self.ui.tableWidget.currentRow()
        indexNumber = str(self.ui.tableWidget.item(row, 0).text())
        firstName = str(self.ui.tableWidget.item(row, 1).text())
        sureName = str(self.ui.tableWidget.item(row, 2).text())
        pesel = str(self.ui.tableWidget.item(row, 3).text())
        self.ui.studentIndexNumberField.setText(QString(indexNumber))
        self.ui.studentFirstNameField.setText(QString(firstName))
        self.ui.studentSureNameField.setText(QString(sureName))
        self.ui.studentPeselNameField.setText(QString(pesel))
        out = [indexNumber, firstName, sureName, pesel]
        print(out)


    def setLineEditsWithDataFromLecturersTable(self):
        row = self.ui.tableWidgetLecturer.currentRow()
        lecturerNo = str(self.ui.tableWidgetLecturer.item(row, 0).text())
        firstName = str(self.ui.tableWidgetLecturer.item(row, 1).text())
        sureName = str(self.ui.tableWidgetLecturer.item(row, 2).text())
        pesel = str(self.ui.tableWidgetLecturer.item(row, 3).text())
        self.ui.lecturerNo.setText(QString(lecturerNo))
        self.ui.lecturerFirstNameField_3.setText(QString(firstName))
        self.ui.lecturerSureNameField_3.setText(QString(sureName))
        self.ui.lecturerPeselNameField_3.setText(QString(pesel))
        out = [firstName, sureName, pesel]
        print(out)


    def setSubjectsForSpecialisation(self):
        rowNumber = self.ui.specialisationsList.currentRow()
        list = str(self.ui.specialisationsList.item(rowNumber, 0).text())
        topicsList = self.dbHandler.getSpecialisationTopicsList(list)
        self.ui.specjalisationsSubjectsList.setRowCount(len(topicsList))
        self.ui.specjalisationsSubjectsList.setColumnCount(1)
        print(topicsList)
        for x in range(0, len(topicsList)):
            self.ui.specjalisationsSubjectsList.setItem(x, 0, QtGui.QTableWidgetItem(QString(topicsList[x])))
        self.ui.specjalisationsSubjectsList.setHorizontalHeaderLabels(QString("Przedmioty nauczania").split(";"))
        self.ui.specjalisationsSubjectsList.horizontalHeader().setStretchLastSection(True)

    def subjectsListPopulate(self):
        self.ui.subjectsListForSpecialisation.clear()
        subjectList = self.fabric.getFromDb('*', 'subjects')
        # subjectList = self.dbHandler.getSubjectsFromDb()
        self.ui.tableWidgetSubjects.setRowCount(len(subjectList))
        self.ui.tableWidgetSubjects.setColumnCount(1)
        for x in range(0, len(subjectList)):
            self.ui.tableWidgetSubjects.setItem(x, 0, QtGui.QTableWidgetItem(QString(subjectList[x][1])))
            self.ui.subjectsListForSpecialisation.addItem(QString(subjectList[x][1]))
        self.ui.tableWidgetSubjects.setHorizontalHeaderLabels(QString("Przedmioty nauczania").split(";"))
        self.ui.tableWidgetSubjects.horizontalHeader().setStretchLastSection(True)
            
    def groupsListPopulate(self):
        groupList = self.fabric.getFromDb('*', 'groups')
        # groupList = self.dbHandler.getGroupsList()
        self.ui.groupsListTableWidget.setRowCount(len(groupList))
        self.ui.groupsListTableWidget.setColumnCount(2)
        for x in range(0, len(groupList)):
            self.ui.groupsListTableWidget.setItem(x, 0, QtGui.QTableWidgetItem(QString(groupList[x][0])))
            self.ui.groupsListTableWidget.setItem(x, 1, QtGui.QTableWidgetItem(QString(groupList[x][1])))
            # self.ui.subjectsListForSpecialisation.addItem(QString(groupList[x]))
        self.ui.groupsListTableWidget.setHorizontalHeaderLabels(QString("Numer grupy;Specjalizacja").split(";"))
        self.ui.groupsListTableWidget.horizontalHeader().setStretchLastSection(True)

    def specialisationsListPopulate(self):
        specialisationstList = self.fabric.getFromDb('specialisationName', 'specialisations')
        # specialisationstList = self.dbHandler.getSpecialisationsList()
        self.ui.specialisationsList.setRowCount(len(specialisationstList))
        self.ui.specialisationsList.setColumnCount(1)
        for x in range(0, len(specialisationstList)):
            self.ui.specialisationsList.setItem(x, 0, QtGui.QTableWidgetItem(QString(specialisationstList[x])))
            self.ui.specialisationsComboList.addItem(QString(specialisationstList[x]))
        self.ui.specialisationsList.setHorizontalHeaderLabels(QString("Specjalizacje").split(";"))
        self.ui.specialisationsList.horizontalHeader().setStretchLastSection(True)


    def studentDynamicFilling(self):
        dane = self.ui.studentBrowser.text()
        firstNameFromDb = self.dbHandler.checkIfInListExist(self.dbHandler.getFromDb('students'), str(dane))
        print(firstNameFromDb)
        self.ui.tableWidget.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        if firstNameFromDb != False:
            self.ui.tableWidget.setRowCount(len(firstNameFromDb))
            self.ui.tableWidget.setColumnCount(4)
            # self.ui.tableWidget.setHorizontalHeaderLabels(QString('indeks', 'imie', 'nazwisko', 'pesel'))
            self.ui.tableWidget.setHorizontalHeaderLabels(QString("indeks;imie;nazwisko;pesel").split(";"))
            for x in range(0, len(firstNameFromDb)):
                print(len(firstNameFromDb))
                self.ui.tableWidget.setItem(x, 0, QtGui.QTableWidgetItem(QString(firstNameFromDb[x][0])))
                self.ui.tableWidget.setItem(x, 1, QtGui.QTableWidgetItem(QString(firstNameFromDb[x][1])))
                self.ui.tableWidget.setItem(x, 2, QtGui.QTableWidgetItem(QString(firstNameFromDb[x][2])))
                self.ui.tableWidget.setItem(x, 3, QtGui.QTableWidgetItem(QString(firstNameFromDb[x][3])))
            self.ui.tableWidget.setHorizontalHeaderLabels(QString("indeks;imie;nazwisko;pesel").split(";"))
            self.ui.tableWidget.horizontalHeader().setStretchLastSection(True)

        else:
            self.ui.tableWidget.clear()
            self.ui.tableWidget.setRowCount(len(self.dbHandler.getFromDb('students')))
            self.ui.tableWidget.setColumnCount(4)
            for x in range(0, len(self.dbHandler.getFromDb('students'))):
                self.ui.tableWidget.setItem(x, 0,
                                            QtGui.QTableWidgetItem(QString(self.dbHandler.getFromDb('students')[x][0])))
                self.ui.tableWidget.setItem(x, 1,
                                            QtGui.QTableWidgetItem(QString(self.dbHandler.getFromDb('students')[x][1])))
                self.ui.tableWidget.setItem(x, 2,
                                            QtGui.QTableWidgetItem(QString(self.dbHandler.getFromDb('students')[x][2])))
                self.ui.tableWidget.setItem(x, 3,
                                            QtGui.QTableWidgetItem(QString(self.dbHandler.getFromDb('students')[x][3])))

        self.ui.tableWidget.setHorizontalHeaderLabels(QString("indeks;imie;nazwisko;pesel").split(";"))
        self.ui.tableWidget.horizontalHeader().setStretchLastSection(True)


    def lecturerDynamicFilling(self):
        dane = self.ui.lecturerBrowser.text()
        firstNameFromDb = self.dbHandler.checkIfInListExist(self.dbHandler.getFromDb('lecturers'), str(dane))
        print(firstNameFromDb)
        self.ui.tableWidgetLecturer.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        if firstNameFromDb != False:
            self.ui.tableWidgetLecturer.setRowCount(len(firstNameFromDb))
            self.ui.tableWidgetLecturer.setColumnCount(4)
            for x in range(0, len(firstNameFromDb)):
                print(len(firstNameFromDb))
                self.ui.tableWidgetLecturer.setItem(x, 0, QtGui.QTableWidgetItem(QString(firstNameFromDb[x][0])))
                self.ui.tableWidgetLecturer.setItem(x, 1, QtGui.QTableWidgetItem(QString(firstNameFromDb[x][1])))
                self.ui.tableWidgetLecturer.setItem(x, 2, QtGui.QTableWidgetItem(QString(firstNameFromDb[x][2])))
                self.ui.tableWidgetLecturer.setItem(x, 3, QtGui.QTableWidgetItem(QString(firstNameFromDb[x][3])))
            self.ui.tableWidgetLecturer.setHorizontalHeaderLabels(QString("imie;nazwisko;pesel").split(";"))
        else:
            self.ui.tableWidgetLecturer.clear()
            self.ui.tableWidgetLecturer.setRowCount(len(self.dbHandler.getFromDb('lecturers')))
            self.ui.tableWidgetLecturer.setColumnCount(4)
            for x in range(0, len(self.dbHandler.getFromDb('lecturers'))):
                self.ui.tableWidgetLecturer.setItem(x, 0,
                                            QtGui.QTableWidgetItem(QString(self.dbHandler.getFromDb('lecturers')[x][0])))
                self.ui.tableWidgetLecturer.setItem(x, 1,
                                            QtGui.QTableWidgetItem(QString(self.dbHandler.getFromDb('lecturers')[x][1])))
                self.ui.tableWidgetLecturer.setItem(x, 2,
                                            QtGui.QTableWidgetItem(QString(self.dbHandler.getFromDb('lecturers')[x][2])))
                self.ui.tableWidgetLecturer.setItem(x, 3,
                                            QtGui.QTableWidgetItem(QString(self.dbHandler.getFromDb('lecturers')[x][3])))
            self.ui.tableWidgetLecturer.setHorizontalHeaderLabels(QString("numer;imie;nazwisko;pesel").split(";"))




if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
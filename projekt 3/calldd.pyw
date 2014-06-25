from PyQt4 import QtGui
from PyQt4.QtCore import QString

__author__ = 'blackmaggot'
import sys
from uczelnia3 import *
from DatabaseHandlerAndManaging import *


class MyForm(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.dbHandler = DatabaseHandlerAndManaging()
        self.subjectsListPopulate()
        self.specialisationsListPopulate()


        self.ui.studentIndexNumberField.textChanged.connect(self.studentDynamicFilling)
        self.ui.tableWidget.itemClicked.connect(self.setLineEditsWithDataFromTable)
        self.ui.specialisationsList.itemClicked.connect(self.setSubjectsForSpecialisation)
        self.ui.studentEditDataButton.clicked.connect(self.updateStudentData)
        self.ui.newStudentSubmitButton.clicked.connect(self.insertStudent)
        self.ui.newSubjectButton.clicked.connect(self.insertSubject)
        self.ui.newSpecialisationSubmitButton.clicked.connect(self.insertSpec)
        self.ui.addSubjectToSpecialisationSubmitButton.clicked.connect(self.insertSubjectToSpec)

    def updateStudentData(self):
        firstName = str(self.ui.studentFirstNameField.text())
        sureName = str(self.ui.studentSureNameField.text())
        pesel = str(self.ui.studentPeselNameField.text())
        indexNumber = str(self.ui.studentIndexNumberField.text())
        if all([len(firstName) != 0, len(indexNumber) != 0, len(sureName) != 0, len(pesel) != 0]):
            self.dbHandler.updateStudent(indexNumber, firstName, sureName, pesel)
        else:
            print "all fields must be filled with data"

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

    def setSubjectsForSpecialisation(self):
        rowNumber = self.ui.specialisationsList.currentRow()
        list = str(self.ui.specialisationsList.item(rowNumber, 0).text())
        topicsList = self.dbHandler.getSpecialisationTopicsList(list)
        self.ui.specjalisationsSubjectsList.setRowCount(len(topicsList))
        self.ui.specjalisationsSubjectsList.setColumnCount(1)
        print(topicsList)
        for x in range(0, len(topicsList)):
            self.ui.specjalisationsSubjectsList.setItem(x, 0, QtGui.QTableWidgetItem(QString(topicsList[x])))

    def subjectsListPopulate(self):
        subjectList = self.dbHandler.getSubjectsFromDb()
        self.ui.tableWidgetSubjects.setRowCount(len(subjectList))
        self.ui.tableWidgetSubjects.setColumnCount(1)
        for x in range(0, len(subjectList)):
            self.ui.tableWidgetSubjects.setItem(x, 0, QtGui.QTableWidgetItem(QString(subjectList[x])))
            self.ui.subjectsListForSpecialisation.addItem(QString(subjectList[x]))

    def specialisationsListPopulate(self):
        specialisationstList = self.dbHandler.getSpecialisationsList()
        self.ui.specialisationsList.setRowCount(len(specialisationstList))
        self.ui.specialisationsList.setColumnCount(1)
        for x in range(0, len(specialisationstList)):
            self.ui.specialisationsList.setItem(x, 0, QtGui.QTableWidgetItem(QString(specialisationstList[x])))


    def studentDynamicFilling(self):
        dane = self.ui.studentIndexNumberField.text()
        firstNameFromDb = self.dbHandler.checkIfInListExist(self.dbHandler.getFromDb('students'), str(dane))
        print(firstNameFromDb)
        self.ui.tableWidget.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        if firstNameFromDb != False:
            self.ui.tableWidget.setRowCount(len(firstNameFromDb))
            self.ui.tableWidget.setColumnCount(4)
            for x in range(0, len(firstNameFromDb)):
                print(len(firstNameFromDb))
                self.ui.tableWidget.setItem(x, 0, QtGui.QTableWidgetItem(QString(firstNameFromDb[x][0])))
                self.ui.tableWidget.setItem(x, 1, QtGui.QTableWidgetItem(QString(firstNameFromDb[x][1])))
                self.ui.tableWidget.setItem(x, 2, QtGui.QTableWidgetItem(QString(firstNameFromDb[x][2])))
                self.ui.tableWidget.setItem(x, 3, QtGui.QTableWidgetItem(QString(firstNameFromDb[x][3])))

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


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
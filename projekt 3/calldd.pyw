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


        #odwolanie do metody
        self.ui.studentIndexNumberField.textChanged.connect(self.studentDynamicFilling)
        self.ui.tableWidget.itemClicked.connect(self.setLineEditsWithDataFromTable)

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
        out =[indexNumber, firstName, sureName, pesel]
        print(out)



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
                self.ui.tableWidget.setItem(x, 0, QtGui.QTableWidgetItem(QString(self.dbHandler.getFromDb('students')[x][0])))
                self.ui.tableWidget.setItem(x, 1, QtGui.QTableWidgetItem(QString(self.dbHandler.getFromDb('students')[x][1])))
                self.ui.tableWidget.setItem(x, 2, QtGui.QTableWidgetItem(QString(self.dbHandler.getFromDb('students')[x][2])))
                self.ui.tableWidget.setItem(x, 3, QtGui.QTableWidgetItem(QString(self.dbHandler.getFromDb('students')[x][3])))









if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
from PyQt4 import QtGui, Qt
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
        self.ui.studentIndexNumberField.textChanged.connect(self.dane)


    def dane(self):
        dane = self.ui.studentIndexNumberField.text()
        firstNameFromDb = self.dbHandler.checkIfInListExist(self.dbHandler.getFromDb(), str(dane))
        print(firstNameFromDb)
        if firstNameFromDb != False:
            self.ui.tableWidget.setRowCount(len(firstNameFromDb))
            self.ui.tableWidget.setColumnCount(8)
            for x in range(0, len(firstNameFromDb)):
                print(len(firstNameFromDb))
                self.ui.tableWidget.setItem(x, 0, QtGui.QTableWidgetItem(QString(firstNameFromDb[x][0])))
                self.ui.tableWidget.setItem(x, 1, QtGui.QTableWidgetItem(QString(firstNameFromDb[x][1])))
                self.ui.tableWidget.setItem(x, 2, QtGui.QTableWidgetItem(QString(firstNameFromDb[x][2])))
                self.ui.tableWidget.setItem(x, 3, QtGui.QTableWidgetItem(QString(firstNameFromDb[x][3])))

        else:
            self.ui.tableWidget.clear()
            self.ui.tableWidget.setRowCount(0)









if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
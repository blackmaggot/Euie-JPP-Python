# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uczelnia.ui'
#
# Created: Sat Jun 21 15:36:29 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(1038, 600)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.studentsTab = QtGui.QTabWidget(Dialog)
        self.studentsTab.setEnabled(True)
        self.studentsTab.setGeometry(QtCore.QRect(90, 100, 708, 343))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.studentsTab.sizePolicy().hasHeightForWidth())
        self.studentsTab.setSizePolicy(sizePolicy)
        self.studentsTab.setObjectName(_fromUtf8("studentsTab"))
        self.R = QtGui.QWidget()
        self.R.setObjectName(_fromUtf8("R"))
        self.studentsTab.addTab(self.R, _fromUtf8(""))
        self.Wykladowcy = QtGui.QWidget()
        self.Wykladowcy.setObjectName(_fromUtf8("Wykladowcy"))
        self.layoutWidget = QtGui.QWidget(self.Wykladowcy)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 686, 262))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_8.setMargin(0)
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.verticalScrollBarOfLecturersList = QtGui.QScrollBar(self.layoutWidget)
        self.verticalScrollBarOfLecturersList.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBarOfLecturersList.setObjectName(_fromUtf8("verticalScrollBarOfLecturersList"))
        self.horizontalLayout_9.addWidget(self.verticalScrollBarOfLecturersList)
        self.instructorListField = QtGui.QListWidget(self.layoutWidget)
        self.instructorListField.setEditTriggers(QtGui.QAbstractItemView.SelectedClicked)
        self.instructorListField.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.instructorListField.setObjectName(_fromUtf8("instructorListField"))
        self.horizontalLayout_9.addWidget(self.instructorListField)
        self.verticalLayout_6.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_8.addLayout(self.verticalLayout_6)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.lecturerInformationLabel = QtGui.QLabel(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lecturerInformationLabel.sizePolicy().hasHeightForWidth())
        self.lecturerInformationLabel.setSizePolicy(sizePolicy)
        self.lecturerInformationLabel.setMaximumSize(QtCore.QSize(16777215, 16766643))
        self.lecturerInformationLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lecturerInformationLabel.setObjectName(_fromUtf8("lecturerInformationLabel"))
        self.verticalLayout_7.addWidget(self.lecturerInformationLabel)
        self.instructorNameField = QtGui.QLineEdit(self.layoutWidget)
        self.instructorNameField.setObjectName(_fromUtf8("instructorNameField"))
        self.verticalLayout_7.addWidget(self.instructorNameField)
        self.instructorSurNameField = QtGui.QLineEdit(self.layoutWidget)
        self.instructorSurNameField.setObjectName(_fromUtf8("instructorSurNameField"))
        self.verticalLayout_7.addWidget(self.instructorSurNameField)
        self.peselField = QtGui.QLineEdit(self.layoutWidget)
        self.peselField.setObjectName(_fromUtf8("peselField"))
        self.verticalLayout_7.addWidget(self.peselField)
        self.instructorAdressField = QtGui.QLineEdit(self.layoutWidget)
        self.instructorAdressField.setObjectName(_fromUtf8("instructorAdressField"))
        self.verticalLayout_7.addWidget(self.instructorAdressField)
        self.instructorLecturesLabel = QtGui.QLabel(self.layoutWidget)
        self.instructorLecturesLabel.setObjectName(_fromUtf8("instructorLecturesLabel"))
        self.verticalLayout_7.addWidget(self.instructorLecturesLabel)
        self.instructorLecturesList = QtGui.QListWidget(self.layoutWidget)
        self.instructorLecturesList.setEditTriggers(QtGui.QAbstractItemView.SelectedClicked)
        self.instructorLecturesList.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.instructorLecturesList.setObjectName(_fromUtf8("instructorLecturesList"))
        item = QtGui.QListWidgetItem()
        self.instructorLecturesList.addItem(item)
        item = QtGui.QListWidgetItem()
        self.instructorLecturesList.addItem(item)
        item = QtGui.QListWidgetItem()
        self.instructorLecturesList.addItem(item)
        item = QtGui.QListWidgetItem()
        self.instructorLecturesList.addItem(item)
        item = QtGui.QListWidgetItem()
        self.instructorLecturesList.addItem(item)
        item = QtGui.QListWidgetItem()
        self.instructorLecturesList.addItem(item)
        item = QtGui.QListWidgetItem()
        self.instructorLecturesList.addItem(item)
        item = QtGui.QListWidgetItem()
        self.instructorLecturesList.addItem(item)
        item = QtGui.QListWidgetItem()
        self.instructorLecturesList.addItem(item)
        self.verticalLayout_7.addWidget(self.instructorLecturesList)
        self.horizontalLayout_10.addLayout(self.verticalLayout_7)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_10)
        self.studentsTab.addTab(self.Wykladowcy, _fromUtf8(""))
        self.Studenci = QtGui.QWidget()
        self.Studenci.setObjectName(_fromUtf8("Studenci"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.Studenci)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.verticalScrollBarOfStudentsList = QtGui.QScrollBar(self.Studenci)
        self.verticalScrollBarOfStudentsList.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBarOfStudentsList.setObjectName(_fromUtf8("verticalScrollBarOfStudentsList"))
        self.horizontalLayout_3.addWidget(self.verticalScrollBarOfStudentsList)
        self.listWidget = QtGui.QListWidget(self.Studenci)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.horizontalLayout_3.addWidget(self.listWidget)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.studentInformationsLabel = QtGui.QLabel(self.Studenci)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.studentInformationsLabel.sizePolicy().hasHeightForWidth())
        self.studentInformationsLabel.setSizePolicy(sizePolicy)
        self.studentInformationsLabel.setMaximumSize(QtCore.QSize(16777215, 16766643))
        self.studentInformationsLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.studentInformationsLabel.setObjectName(_fromUtf8("studentInformationsLabel"))
        self.verticalLayout_3.addWidget(self.studentInformationsLabel)
        self.studentIndexNumberField = QtGui.QLineEdit(self.Studenci)
        self.studentIndexNumberField.setObjectName(_fromUtf8("studentIndexNumberField"))
        self.verticalLayout_3.addWidget(self.studentIndexNumberField)
        self.studentFirstNameField = QtGui.QLineEdit(self.Studenci)
        self.studentFirstNameField.setObjectName(_fromUtf8("studentFirstNameField"))
        self.verticalLayout_3.addWidget(self.studentFirstNameField)
        self.studentSureNameField = QtGui.QLineEdit(self.Studenci)
        self.studentSureNameField.setObjectName(_fromUtf8("studentSureNameField"))
        self.verticalLayout_3.addWidget(self.studentSureNameField)
        self.studentPeselNameField = QtGui.QLineEdit(self.Studenci)
        self.studentPeselNameField.setObjectName(_fromUtf8("studentPeselNameField"))
        self.verticalLayout_3.addWidget(self.studentPeselNameField)
        self.studentAdressField = QtGui.QLineEdit(self.Studenci)
        self.studentAdressField.setObjectName(_fromUtf8("studentAdressField"))
        self.verticalLayout_3.addWidget(self.studentAdressField)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.studentGroupLabel = QtGui.QLabel(self.Studenci)
        self.studentGroupLabel.setObjectName(_fromUtf8("studentGroupLabel"))
        self.horizontalLayout_6.addWidget(self.studentGroupLabel)
        self.studentGroupDropdownList = QtGui.QComboBox(self.Studenci)
        self.studentGroupDropdownList.setEditable(False)
        self.studentGroupDropdownList.setInsertPolicy(QtGui.QComboBox.InsertAfterCurrent)
        self.studentGroupDropdownList.setFrame(True)
        self.studentGroupDropdownList.setObjectName(_fromUtf8("studentGroupDropdownList"))
        self.studentGroupDropdownList.addItem(_fromUtf8(""))
        self.studentGroupDropdownList.addItem(_fromUtf8(""))
        self.studentGroupDropdownList.addItem(_fromUtf8(""))
        self.studentGroupDropdownList.addItem(_fromUtf8(""))
        self.studentGroupDropdownList.addItem(_fromUtf8(""))
        self.studentGroupDropdownList.addItem(_fromUtf8(""))
        self.horizontalLayout_6.addWidget(self.studentGroupDropdownList)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.studentYearLabel = QtGui.QLabel(self.Studenci)
        self.studentYearLabel.setObjectName(_fromUtf8("studentYearLabel"))
        self.horizontalLayout_5.addWidget(self.studentYearLabel)
        self.studentYearDropdownList = QtGui.QComboBox(self.Studenci)
        self.studentYearDropdownList.setEditable(False)
        self.studentYearDropdownList.setInsertPolicy(QtGui.QComboBox.InsertAfterCurrent)
        self.studentYearDropdownList.setFrame(True)
        self.studentYearDropdownList.setObjectName(_fromUtf8("studentYearDropdownList"))
        self.studentYearDropdownList.addItem(_fromUtf8(""))
        self.studentYearDropdownList.addItem(_fromUtf8(""))
        self.studentYearDropdownList.addItem(_fromUtf8(""))
        self.studentYearDropdownList.addItem(_fromUtf8(""))
        self.studentYearDropdownList.addItem(_fromUtf8(""))
        self.studentYearDropdownList.addItem(_fromUtf8(""))
        self.horizontalLayout_5.addWidget(self.studentYearDropdownList)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.studentStatusLable = QtGui.QLabel(self.Studenci)
        self.studentStatusLable.setMaximumSize(QtCore.QSize(16777215, 16776381))
        self.studentStatusLable.setScaledContents(False)
        self.studentStatusLable.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.studentStatusLable.setObjectName(_fromUtf8("studentStatusLable"))
        self.verticalLayout_2.addWidget(self.studentStatusLable)
        self.studentStatusFrame = QtGui.QFrame(self.Studenci)
        self.studentStatusFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.studentStatusFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.studentStatusFrame.setObjectName(_fromUtf8("studentStatusFrame"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.studentStatusFrame)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.studentOnListRadio = QtGui.QRadioButton(self.studentStatusFrame)
        self.studentOnListRadio.setObjectName(_fromUtf8("studentOnListRadio"))
        self.verticalLayout.addWidget(self.studentOnListRadio)
        self.studendSuspendedRadio = QtGui.QRadioButton(self.studentStatusFrame)
        self.studendSuspendedRadio.setObjectName(_fromUtf8("studendSuspendedRadio"))
        self.verticalLayout.addWidget(self.studendSuspendedRadio)
        self.studentRemovedRadio = QtGui.QRadioButton(self.studentStatusFrame)
        self.studentRemovedRadio.setObjectName(_fromUtf8("studentRemovedRadio"))
        self.verticalLayout.addWidget(self.studentRemovedRadio)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2.addWidget(self.studentStatusFrame)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.studentEditDataButton = QtGui.QPushButton(self.Studenci)
        self.studentEditDataButton.setObjectName(_fromUtf8("studentEditDataButton"))
        self.verticalLayout_5.addWidget(self.studentEditDataButton)
        self.studentsTab.addTab(self.Studenci, _fromUtf8(""))
        self.Oceny = QtGui.QWidget()
        self.Oceny.setObjectName(_fromUtf8("Oceny"))
        self.studentsTab.addTab(self.Oceny, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.studentsTab.addTab(self.tab, _fromUtf8(""))

        self.retranslateUi(Dialog)
        self.studentsTab.setCurrentIndex(2)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.studentsTab.setTabText(self.studentsTab.indexOf(self.R), _translate("Dialog", "Rocznik", None))
        self.lecturerInformationLabel.setText(_translate("Dialog", "Dane wykładowcy", None))
        self.instructorNameField.setPlaceholderText(_translate("Dialog", "Imię", None))
        self.instructorSurNameField.setPlaceholderText(_translate("Dialog", "Nazwisko", None))
        self.peselField.setPlaceholderText(_translate("Dialog", "PESEL", None))
        self.instructorAdressField.setPlaceholderText(_translate("Dialog", "Adres Zamieszkania", None))
        self.instructorLecturesLabel.setText(_translate("Dialog", "Przedmioty wykładowcy", None))
        __sortingEnabled = self.instructorLecturesList.isSortingEnabled()
        self.instructorLecturesList.setSortingEnabled(False)
        item = self.instructorLecturesList.item(0)
        item.setText(_translate("Dialog", "grge", None))
        item = self.instructorLecturesList.item(1)
        item.setText(_translate("Dialog", "re", None))
        item = self.instructorLecturesList.item(2)
        item.setText(_translate("Dialog", "ge", None))
        item = self.instructorLecturesList.item(3)
        item.setText(_translate("Dialog", "rg", None))
        item = self.instructorLecturesList.item(4)
        item.setText(_translate("Dialog", "erge", None))
        item = self.instructorLecturesList.item(5)
        item.setText(_translate("Dialog", "rg", None))
        item = self.instructorLecturesList.item(6)
        item.setText(_translate("Dialog", "erg", None))
        item = self.instructorLecturesList.item(7)
        item.setText(_translate("Dialog", "rege", None))
        item = self.instructorLecturesList.item(8)
        item.setText(_translate("Dialog", "rge", None))
        self.instructorLecturesList.setSortingEnabled(__sortingEnabled)
        self.studentsTab.setTabText(self.studentsTab.indexOf(self.Wykladowcy), _translate("Dialog", "Wykładowcy", None))
        self.studentInformationsLabel.setText(_translate("Dialog", "Dane studenta", None))
        self.studentIndexNumberField.setPlaceholderText(_translate("Dialog", "Index", None))
        self.studentFirstNameField.setPlaceholderText(_translate("Dialog", "Imię", None))
        self.studentSureNameField.setPlaceholderText(_translate("Dialog", "Nazwisko", None))
        self.studentPeselNameField.setPlaceholderText(_translate("Dialog", "PESEL", None))
        self.studentAdressField.setPlaceholderText(_translate("Dialog", "Adres Zamieszkania", None))
        self.studentGroupLabel.setText(_translate("Dialog", "Grupa", None))
        self.studentGroupDropdownList.setProperty("currentText", _translate("Dialog", "sacasc", None))
        self.studentGroupDropdownList.setItemText(0, _translate("Dialog", "sacasc", None))
        self.studentGroupDropdownList.setItemText(1, _translate("Dialog", "sacasc", None))
        self.studentGroupDropdownList.setItemText(2, _translate("Dialog", "ascascas", None))
        self.studentGroupDropdownList.setItemText(3, _translate("Dialog", "cascasca", None))
        self.studentGroupDropdownList.setItemText(4, _translate("Dialog", "scascasc", None))
        self.studentGroupDropdownList.setItemText(5, _translate("Dialog", "ascascasc", None))
        self.studentYearLabel.setText(_translate("Dialog", "Rocznik", None))
        self.studentYearDropdownList.setProperty("currentText", _translate("Dialog", "sacasc", None))
        self.studentYearDropdownList.setItemText(0, _translate("Dialog", "sacasc", None))
        self.studentYearDropdownList.setItemText(1, _translate("Dialog", "sacasc", None))
        self.studentYearDropdownList.setItemText(2, _translate("Dialog", "ascascas", None))
        self.studentYearDropdownList.setItemText(3, _translate("Dialog", "cascasca", None))
        self.studentYearDropdownList.setItemText(4, _translate("Dialog", "scascasc", None))
        self.studentYearDropdownList.setItemText(5, _translate("Dialog", "ascascasc", None))
        self.studentStatusLable.setText(_translate("Dialog", "Status studenta", None))
        self.studentOnListRadio.setText(_translate("Dialog", "Na liście studentów", None))
        self.studendSuspendedRadio.setText(_translate("Dialog", "Zawieszony w prawach", None))
        self.studentRemovedRadio.setText(_translate("Dialog", "Usunięty z listy studentów", None))
        self.studentEditDataButton.setText(_translate("Dialog", "Edytuj zmiany", None))
        self.studentsTab.setTabText(self.studentsTab.indexOf(self.Studenci), _translate("Dialog", "Studenci", None))
        self.studentsTab.setTabText(self.studentsTab.indexOf(self.Oceny), _translate("Dialog", "Oceny", None))
        self.studentsTab.setTabText(self.studentsTab.indexOf(self.tab), _translate("Dialog", "Przedmioty", None))


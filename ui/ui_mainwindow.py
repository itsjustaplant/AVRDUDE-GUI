# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'deneme.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setWindowModality(Qt.WindowModal)
        Form.setEnabled(True)
        Form.resize(421, 480)
        Form.setMinimumSize(QSize(421, 480))
        Form.setMaximumSize(QSize(421, 480))
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(17, 18, 49, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(185, 185, 185, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush2)
        brush3 = QBrush(QColor(18, 18, 18, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush3)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        Form.setPalette(palette)
        icon = QIcon()
        iconThemeName = u"Dark"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)
        
        Form.setWindowIcon(icon)
        Form.setStyleSheet(u"QWidget{\n"
"	background-color: #111231;\n"
"}")
        self.setupbutton = QPushButton(Form)
        self.setupbutton.setObjectName(u"setupbutton")
        self.setupbutton.setGeometry(QRect(0, 0, 141, 61))
        self.setupbutton.setStyleSheet(u"QPushButton{\n"
"	background-color: #0c081b;\n"
"	color: #f6e9e9;\n"
"	font-size: 24px;\n"
"}")
        self.setupbutton.setFlat(False)
        self.fusebutton = QPushButton(Form)
        self.fusebutton.setObjectName(u"fusebutton")
        self.fusebutton.setGeometry(QRect(140, 0, 141, 61))
        self.fusebutton.setStyleSheet(u"#fusebutton{\n"
"	background-color: #0c081b;\n"
"	color: #f6e9e9;\n"
"	font-size: 24px;\n"
"}")
        self.fusebutton.setFlat(False)
        self.aboutbutton = QPushButton(Form)
        self.aboutbutton.setObjectName(u"aboutbutton")
        self.aboutbutton.setGeometry(QRect(280, 0, 141, 61))
        self.aboutbutton.setStyleSheet(u"#aboutbutton{\n"
"	background-color: #0c081b;\n"
"	color: #f6e9e9;\n"
"	font-size: 24px;\n"
"}")
        self.aboutbutton.setFlat(False)
        self.flashbutton = QPushButton(Form)
        self.flashbutton.setObjectName(u"flashbutton")
        self.flashbutton.setGeometry(QRect(10, 420, 401, 41))
        self.flashbutton.setStyleSheet(u"QPushButton#flashbutton{\n"
"	background-color: #ff1b1b;\n"
"	font-size: 28px;\n"
"	font: bold;\n"
"	color: #f6e9e9;\n"
"}")
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 230, 401, 151))
        self.groupBox.setStyleSheet(u"QGroupBox{\n"
"	font-size: 18px;\n"
"	background-color: transparent;\n"
"	color: #f6e9e9;\n"
"	border: 0.5px solid #0c081b;\n"
"    border-radius: 9px;\n"
"    margin-top: 0.5em;\n"
"}\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"    padding: 0 3px 0 3px;\n"
"}")
        self.groupBox.setFlat(False)
        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 100, 281, 21))
        self.label_6.setStyleSheet(u"QLabel{\n"
"	background-color: transparent;\n"
"	font-size: 18px;\n"
"	color: #f6e9e9;\n"
"}")
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 70, 281, 21))
        self.label_5.setStyleSheet(u"QLabel{\n"
"	background-color: transparent;\n"
"	font-size: 18px;\n"
"	color: #f6e9e9;\n"
"}")
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 40, 181, 21))
        self.label_4.setStyleSheet(u"QLabel{\n"
"	background-color: transparent;\n"
"	font-size: 18px;\n"
"	color: #f6e9e9;\n"
"}")
        self.checkBox_3 = QCheckBox(self.groupBox)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setGeometry(QRect(320, 100, 21, 20))
        self.checkBox_2 = QCheckBox(self.groupBox)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setGeometry(QRect(320, 70, 21, 20))
        self.checkBox = QCheckBox(self.groupBox)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(320, 40, 21, 20))
        self.checkBox.setStyleSheet(u"\n"
"QCheckBox::indicator::checked{\n"
"	width: 50px;\n"
"	height: 50px;\n"
"	color: red;\n"
"}")
        self.groupBox_2 = QGroupBox(Form)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 70, 401, 141))
        self.groupBox_2.setStyleSheet(u"QGroupBox{\n"
"	font-size: 18px;\n"
"	background-color: transparent;\n"
"	color: #f6e9e9;\n"
"	border: 0.5px solid #0c081b;\n"
"    border-radius: 9px;\n"
"    margin-top: 0.5em;\n"
"}\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"    padding: 0 3px 0 3px;\n"
"}")
        self.groupBox_2.setFlat(False)
        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 110, 91, 21))
        self.label_3.setStyleSheet(u"QLabel{\n"
"	background-color: transparent;\n"
"	font-size: 18px;\n"
"	color: #f6e9e9;\n"
"}")
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 70, 111, 21))
        self.label.setStyleSheet(u"QLabel{\n"
"	background-color: transparent;\n"
"	font-size: 18px;\n"
"	color: #f6e9e9;\n"
"}")
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 40, 91, 21))
        self.label_2.setStyleSheet(u"QLabel{\n"
"	background-color: transparent;\n"
"	font-size: 18px;\n"
"	color: #f6e9e9;\n"
"}")
        self.comboBox = QComboBox(self.groupBox_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(140, 70, 104, 26))
        self.comboBox.setStyleSheet(u"QComboBox{\n"
"	background-color: #212860;\n"
"	font-size: 18px;\n"
"	color: #f6e9e9;\n"
"}\n"
"")
        self.comboBox_2 = QComboBox(self.groupBox_2)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(140, 30, 171, 26))
        self.comboBox_2.setStyleSheet(u"QComboBox{\n"
"	background-color: #212860;\n"
"	font-size: 18px;\n"
"	color: #f6e9e9;\n"
"}\n"
"")
        self.browsebutton = QPushButton(self.groupBox_2)
        self.browsebutton.setObjectName(u"browsebutton")
        self.browsebutton.setGeometry(QRect(292, 101, 111, 31))
        self.browsebutton.setStyleSheet(u"#browsebutton{\n"
"	background-color: #212860;\n"
"	color: #f6e9e9;\n"
"	font-size: 18px;\n"
"	border: none;\n"
"}")
        self.lineEdit = QLineEdit(self.groupBox_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(140, 110, 113, 21))
        self.lineEdit.setStyleSheet(u"QLineEdit{\n"
"	font-size: 18px;\n"
"	background-color: #212860;\n"
"}")

        self.retranslateUi(Form)
        self.browsebutton.clicked.connect(Form.close)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Neptune", None))
        self.setupbutton.setText(QCoreApplication.translate("Form", u"Setup", None))
        self.fusebutton.setText(QCoreApplication.translate("Form", u"Fuse", None))
        self.aboutbutton.setText(QCoreApplication.translate("Form", u"About", None))
        self.flashbutton.setText(QCoreApplication.translate("Form", u"FLASH!", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Options", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Automatic verification", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Override invalid signature check", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Perform chip erase", None))
        self.checkBox_3.setText(QCoreApplication.translate("Form", u"CheckBox", None))
        self.checkBox_2.setText(QCoreApplication.translate("Form", u"CheckBox", None))
        self.checkBox.setText(QCoreApplication.translate("Form", u"CheckBox", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"Main", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Hex File", None))
        self.label.setText(QCoreApplication.translate("Form", u"Programmer", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Chip", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"usbasp", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Form", u"arduino", None))

        self.comboBox_2.setItemText(0, QCoreApplication.translate("Form", u"Atmega328p", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("Form", u"Atmega128", None))

        self.browsebutton.setText(QCoreApplication.translate("Form", u"Browse", None))
    # retranslateUi


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
import csv
import os
import sys
import time
from time import gmtime, localtime, strftime
import dns.resolver
import subprocess as sub

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(485, 209)
        Dialog.setMouseTracking(False)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(30, 54, 321, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(368, 56, 91, 31))
        self.pushButton.setObjectName("pushButton")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(32, 126, 191, 28))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_2.setGeometry(QtCore.QRect(252, 126, 191, 28))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(32, 28, 181, 16))
        font = QtGui.QFont()
        font.setFamily("휴먼편지체")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(39, 99, 101, 16))
        font = QtGui.QFont()
        font.setFamily("휴먼편지체")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(255, 100, 81, 16))
        font = QtGui.QFont()
        font.setFamily("휴먼편지체")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(56, 175, 371, 16))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setItalic(True)
        self.label_4.setFont(font)
        self.label_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_4.setTextFormat(QtCore.Qt.AutoText)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(406, 5, 71, 20))
        font = QtGui.QFont()
        font.setFamily("한컴 쿨재즈 B")
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.pushButton.clicked.connect(self.query)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Lookup the NS"))
        self.pushButton.setText(_translate("Dialog", "Go!"))
        self.label.setText(_translate("Dialog", "Input the Domain name"))
        self.label_2.setText(_translate("Dialog", "Date & TIme"))
        self.label_3.setText(_translate("Dialog", "IP Address"))
        self.label_4.setText(_translate("Dialog", "Best Of the Best Digital Forensic"))
        self.label_5.setText(_translate("Dialog", "@L3ad0xFF"))

    def query(self):
        qurey_list = list()
        domain = self.lineEdit.text()
        now_date = time.strftime("%Y-%m-%d", localtime())
        now_time = time.strftime("%H:%M:%S", localtime())
        #gmt_date = time.strftime("%Y-%m-%d", gmtime())
        #gmt_time = time.strftime("%H:%M:%S", gmtime())
        the_time = str(now_date) + str(" ") +str(now_time)
        self.textBrowser.setText(the_time)
        resolver = dns.resolver.Resolver()
        resolver.nameservers = ['8.8.8.8']

        try :
            ip_query = resolver.query(domain, 'A')
            for rdata in ip_query :
                ip_addr = rdata.address
                
        except :
            resolver.nameservers = ['64.6.64.6']
            ip_query = resolver.query(domain, 'A')
            for rdata in ip_query :
                ip_addr = rdata.address
                
        self.textBrowser_2.setText(str(ip_addr))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


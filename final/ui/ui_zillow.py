# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_zillow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Zillow(object):
    def setupUi(self, Zillow):
        if not Zillow.objectName():
            Zillow.setObjectName(u"Zillow")
        Zillow.resize(295, 481)
        self.centralwidget = QWidget(Zillow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btnClear = QPushButton(self.centralwidget)
        self.btnClear.setObjectName(u"btnClear")

        self.verticalLayout.addWidget(self.btnClear)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.linZip = QLineEdit(self.centralwidget)
        self.linZip.setObjectName(u"linZip")

        self.gridLayout.addWidget(self.linZip, 3, 1, 1, 1)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)

        self.linPrice = QLineEdit(self.centralwidget)
        self.linPrice.setObjectName(u"linPrice")

        self.gridLayout.addWidget(self.linPrice, 0, 1, 1, 1)

        self.linCity = QLineEdit(self.centralwidget)
        self.linCity.setObjectName(u"linCity")

        self.gridLayout.addWidget(self.linCity, 2, 1, 1, 1)

        self.linAddress = QLineEdit(self.centralwidget)
        self.linAddress.setObjectName(u"linAddress")

        self.gridLayout.addWidget(self.linAddress, 1, 1, 1, 1)

        self.linYear = QLineEdit(self.centralwidget)
        self.linYear.setObjectName(u"linYear")

        self.gridLayout.addWidget(self.linYear, 4, 1, 1, 1)

        self.linType = QLineEdit(self.centralwidget)
        self.linType.setObjectName(u"linType")

        self.gridLayout.addWidget(self.linType, 5, 1, 1, 1)

        self.linBedrooms = QLineEdit(self.centralwidget)
        self.linBedrooms.setObjectName(u"linBedrooms")

        self.gridLayout.addWidget(self.linBedrooms, 6, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.btnAddHouse = QPushButton(self.centralwidget)
        self.btnAddHouse.setObjectName(u"btnAddHouse")

        self.verticalLayout.addWidget(self.btnAddHouse)

        self.btnSearchHouse = QPushButton(self.centralwidget)
        self.btnSearchHouse.setObjectName(u"btnSearchHouse")

        self.verticalLayout.addWidget(self.btnSearchHouse)

        self.linResults = QTextEdit(self.centralwidget)
        self.linResults.setObjectName(u"linResults")

        self.verticalLayout.addWidget(self.linResults)

        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.linIndex = QLineEdit(self.splitter)
        self.linIndex.setObjectName(u"linIndex")
        self.splitter.addWidget(self.linIndex)
        self.btnUpdateHouse = QPushButton(self.splitter)
        self.btnUpdateHouse.setObjectName(u"btnUpdateHouse")
        self.splitter.addWidget(self.btnUpdateHouse)

        self.verticalLayout.addWidget(self.splitter)

        Zillow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Zillow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 295, 21))
        Zillow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Zillow)
        self.statusbar.setObjectName(u"statusbar")
        Zillow.setStatusBar(self.statusbar)

        self.retranslateUi(Zillow)

        QMetaObject.connectSlotsByName(Zillow)
    # setupUi

    def retranslateUi(self, Zillow):
        Zillow.setWindowTitle(QCoreApplication.translate("Zillow", u"Zillow", None))
        self.btnClear.setText(QCoreApplication.translate("Zillow", u"Clear", None))
        self.label.setText(QCoreApplication.translate("Zillow", u"Price", None))
        self.label_2.setText(QCoreApplication.translate("Zillow", u"Address", None))
        self.label_5.setText(QCoreApplication.translate("Zillow", u"Year", None))
        self.label_3.setText(QCoreApplication.translate("Zillow", u"City", None))
        self.label_6.setText(QCoreApplication.translate("Zillow", u"Type", None))
        self.label_4.setText(QCoreApplication.translate("Zillow", u"Zip", None))
        self.linZip.setText(QCoreApplication.translate("Zillow", u"60089", None))
        self.label_7.setText(QCoreApplication.translate("Zillow", u"Badrooms", None))
        self.linPrice.setText(QCoreApplication.translate("Zillow", u"1000", None))
        self.linCity.setText(QCoreApplication.translate("Zillow", u"Chicago", None))
        self.linAddress.setText(QCoreApplication.translate("Zillow", u"2407 N Mildred", None))
        self.linYear.setText(QCoreApplication.translate("Zillow", u"1915", None))
        self.linType.setText(QCoreApplication.translate("Zillow", u"condo", None))
        self.linBedrooms.setText(QCoreApplication.translate("Zillow", u"2", None))
        self.btnAddHouse.setText(QCoreApplication.translate("Zillow", u"Create House", None))
        self.btnSearchHouse.setText(QCoreApplication.translate("Zillow", u"Search House", None))
        self.btnUpdateHouse.setText(QCoreApplication.translate("Zillow", u"Update House", None))
    # retranslateUi


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
        Zillow.resize(351, 311)
        self.centralwidget = QWidget(Zillow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_1 = QWidget()
        self.tab_1.setObjectName(u"tab_1")
        self.verticalLayout_2 = QVBoxLayout(self.tab_1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.tab_1)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.tab_1)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_5 = QLabel(self.tab_1)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.label_3 = QLabel(self.tab_1)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.label_6 = QLabel(self.tab_1)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)

        self.label_4 = QLabel(self.tab_1)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.linZip = QLineEdit(self.tab_1)
        self.linZip.setObjectName(u"linZip")

        self.gridLayout.addWidget(self.linZip, 3, 1, 1, 1)

        self.label_7 = QLabel(self.tab_1)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)

        self.linPrice = QLineEdit(self.tab_1)
        self.linPrice.setObjectName(u"linPrice")

        self.gridLayout.addWidget(self.linPrice, 0, 1, 1, 1)

        self.linCity = QLineEdit(self.tab_1)
        self.linCity.setObjectName(u"linCity")

        self.gridLayout.addWidget(self.linCity, 2, 1, 1, 1)

        self.linAddress = QLineEdit(self.tab_1)
        self.linAddress.setObjectName(u"linAddress")

        self.gridLayout.addWidget(self.linAddress, 1, 1, 1, 1)

        self.linYear = QLineEdit(self.tab_1)
        self.linYear.setObjectName(u"linYear")

        self.gridLayout.addWidget(self.linYear, 4, 1, 1, 1)

        self.linType = QLineEdit(self.tab_1)
        self.linType.setObjectName(u"linType")

        self.gridLayout.addWidget(self.linType, 5, 1, 1, 1)

        self.linBedrooms = QLineEdit(self.tab_1)
        self.linBedrooms.setObjectName(u"linBedrooms")

        self.gridLayout.addWidget(self.linBedrooms, 6, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.btnAddHouse = QPushButton(self.tab_1)
        self.btnAddHouse.setObjectName(u"btnAddHouse")

        self.verticalLayout_2.addWidget(self.btnAddHouse)

        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout.addWidget(self.tabWidget)

        Zillow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Zillow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 351, 21))
        Zillow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Zillow)
        self.statusbar.setObjectName(u"statusbar")
        Zillow.setStatusBar(self.statusbar)

        self.retranslateUi(Zillow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Zillow)
    # setupUi

    def retranslateUi(self, Zillow):
        Zillow.setWindowTitle(QCoreApplication.translate("Zillow", u"Zillow", None))
        self.label.setText(QCoreApplication.translate("Zillow", u"Price", None))
        self.label_2.setText(QCoreApplication.translate("Zillow", u"Address", None))
        self.label_5.setText(QCoreApplication.translate("Zillow", u"Year", None))
        self.label_3.setText(QCoreApplication.translate("Zillow", u"City", None))
        self.label_6.setText(QCoreApplication.translate("Zillow", u"Type", None))
        self.label_4.setText(QCoreApplication.translate("Zillow", u"Zip", None))
        self.linZip.setText(QCoreApplication.translate("Zillow", u"60614", None))
        self.label_7.setText(QCoreApplication.translate("Zillow", u"Badrooms", None))
        self.linPrice.setText(QCoreApplication.translate("Zillow", u"250000", None))
        self.linCity.setText(QCoreApplication.translate("Zillow", u"Chicago", None))
        self.linAddress.setText(QCoreApplication.translate("Zillow", u"2407 N Mildred", None))
        self.linYear.setText(QCoreApplication.translate("Zillow", u"1915", None))
        self.linType.setText(QCoreApplication.translate("Zillow", u"condo", None))
        self.linBedrooms.setText(QCoreApplication.translate("Zillow", u"2", None))
        self.btnAddHouse.setText(QCoreApplication.translate("Zillow", u"Create Listing", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), QCoreApplication.translate("Zillow", u"Add | Update houses", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Zillow", u"Search Houses", None))
    # retranslateUi


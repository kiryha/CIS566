# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'split_smart_main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_SplitSmart(object):
    def setupUi(self, SplitSmart):
        if not SplitSmart.objectName():
            SplitSmart.setObjectName(u"SplitSmart")
        SplitSmart.resize(407, 806)
        self.centralwidget = QWidget(SplitSmart)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btnSplitSmart = QPushButton(self.centralwidget)
        self.btnSplitSmart.setObjectName(u"btnSplitSmart")

        self.verticalLayout.addWidget(self.btnSplitSmart)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_2 = QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.splitter_5 = QSplitter(self.tab)
        self.splitter_5.setObjectName(u"splitter_5")
        self.splitter_5.setOrientation(Qt.Horizontal)
        self.label_5 = QLabel(self.splitter_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(80, 0))
        self.label_5.setMaximumSize(QSize(80, 16777215))
        self.splitter_5.addWidget(self.label_5)
        self.linSignupName = QLineEdit(self.splitter_5)
        self.linSignupName.setObjectName(u"linSignupName")
        self.splitter_5.addWidget(self.linSignupName)

        self.verticalLayout_2.addWidget(self.splitter_5)

        self.splitter_6 = QSplitter(self.tab)
        self.splitter_6.setObjectName(u"splitter_6")
        self.splitter_6.setOrientation(Qt.Horizontal)
        self.label_6 = QLabel(self.splitter_6)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(80, 0))
        self.label_6.setMaximumSize(QSize(80, 16777215))
        self.splitter_6.addWidget(self.label_6)
        self.linSignupLastName = QLineEdit(self.splitter_6)
        self.linSignupLastName.setObjectName(u"linSignupLastName")
        self.splitter_6.addWidget(self.linSignupLastName)

        self.verticalLayout_2.addWidget(self.splitter_6)

        self.splitter_4 = QSplitter(self.tab)
        self.splitter_4.setObjectName(u"splitter_4")
        self.splitter_4.setOrientation(Qt.Horizontal)
        self.label_4 = QLabel(self.splitter_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(80, 0))
        self.label_4.setMaximumSize(QSize(80, 16777215))
        self.splitter_4.addWidget(self.label_4)
        self.linSignupEmail = QLineEdit(self.splitter_4)
        self.linSignupEmail.setObjectName(u"linSignupEmail")
        self.splitter_4.addWidget(self.linSignupEmail)

        self.verticalLayout_2.addWidget(self.splitter_4)

        self.splitter_3 = QSplitter(self.tab)
        self.splitter_3.setObjectName(u"splitter_3")
        self.splitter_3.setOrientation(Qt.Horizontal)
        self.label_3 = QLabel(self.splitter_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(80, 0))
        self.label_3.setMaximumSize(QSize(80, 16777215))
        self.splitter_3.addWidget(self.label_3)
        self.linSignupPassword = QLineEdit(self.splitter_3)
        self.linSignupPassword.setObjectName(u"linSignupPassword")
        self.splitter_3.addWidget(self.linSignupPassword)

        self.verticalLayout_2.addWidget(self.splitter_3)

        self.btnSignUp = QPushButton(self.tab)
        self.btnSignUp.setObjectName(u"btnSignUp")
        self.btnSignUp.setMinimumSize(QSize(0, 35))

        self.verticalLayout_2.addWidget(self.btnSignUp)

        self.line = QFrame(self.tab)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.splitter = QSplitter(self.tab)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.label = QLabel(self.splitter)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(80, 0))
        self.label.setMaximumSize(QSize(80, 16777215))
        self.splitter.addWidget(self.label)
        self.linLoginEmail = QLineEdit(self.splitter)
        self.linLoginEmail.setObjectName(u"linLoginEmail")
        self.splitter.addWidget(self.linLoginEmail)

        self.verticalLayout_2.addWidget(self.splitter)

        self.splitter_2 = QSplitter(self.tab)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.label_2 = QLabel(self.splitter_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(80, 0))
        self.label_2.setMaximumSize(QSize(80, 16777215))
        self.splitter_2.addWidget(self.label_2)
        self.linLoginPassword = QLineEdit(self.splitter_2)
        self.linLoginPassword.setObjectName(u"linLoginPassword")
        self.splitter_2.addWidget(self.linLoginPassword)

        self.verticalLayout_2.addWidget(self.splitter_2)

        self.btnLogIn = QPushButton(self.tab)
        self.btnLogIn.setObjectName(u"btnLogIn")
        self.btnLogIn.setMinimumSize(QSize(0, 35))

        self.verticalLayout_2.addWidget(self.btnLogIn)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout.addWidget(self.tabWidget)

        SplitSmart.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(SplitSmart)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 407, 21))
        SplitSmart.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(SplitSmart)
        self.statusbar.setObjectName(u"statusbar")
        SplitSmart.setStatusBar(self.statusbar)

        self.retranslateUi(SplitSmart)

        QMetaObject.connectSlotsByName(SplitSmart)
    # setupUi

    def retranslateUi(self, SplitSmart):
        SplitSmart.setWindowTitle(QCoreApplication.translate("SplitSmart", u"Split Smart", None))
        self.btnSplitSmart.setText(QCoreApplication.translate("SplitSmart", u"Split Smart", None))
        self.label_5.setText(QCoreApplication.translate("SplitSmart", u"Name", None))
        self.label_6.setText(QCoreApplication.translate("SplitSmart", u"Last Name", None))
        self.label_4.setText(QCoreApplication.translate("SplitSmart", u"Email", None))
        self.label_3.setText(QCoreApplication.translate("SplitSmart", u"Password", None))
        self.btnSignUp.setText(QCoreApplication.translate("SplitSmart", u"Sign Up", None))
        self.label.setText(QCoreApplication.translate("SplitSmart", u"Email", None))
        self.label_2.setText(QCoreApplication.translate("SplitSmart", u"Password", None))
        self.btnLogIn.setText(QCoreApplication.translate("SplitSmart", u"Log In", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("SplitSmart", u"Login / Sign Up", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("SplitSmart", u"Tab 2", None))
    # retranslateUi


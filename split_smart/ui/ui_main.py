# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
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
        SplitSmart.resize(453, 773)
        self.centralwidget = QWidget(SplitSmart)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btnSplitSmart = QPushButton(self.centralwidget)
        self.btnSplitSmart.setObjectName(u"btnSplitSmart")

        self.verticalLayout.addWidget(self.btnSplitSmart)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_1 = QWidget()
        self.tab_1.setObjectName(u"tab_1")
        self.verticalLayout_2 = QVBoxLayout(self.tab_1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.splitter_5 = QSplitter(self.tab_1)
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

        self.splitter_6 = QSplitter(self.tab_1)
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

        self.splitter_4 = QSplitter(self.tab_1)
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

        self.splitter_3 = QSplitter(self.tab_1)
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

        self.btnSignUp = QPushButton(self.tab_1)
        self.btnSignUp.setObjectName(u"btnSignUp")
        self.btnSignUp.setMinimumSize(QSize(0, 35))

        self.verticalLayout_2.addWidget(self.btnSignUp)

        self.line = QFrame(self.tab_1)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.splitter = QSplitter(self.tab_1)
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

        self.splitter_2 = QSplitter(self.tab_1)
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

        self.btnLogIn = QPushButton(self.tab_1)
        self.btnLogIn.setObjectName(u"btnLogIn")
        self.btnLogIn.setMinimumSize(QSize(0, 35))

        self.verticalLayout_2.addWidget(self.btnLogIn)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_3 = QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.splitter_7 = QSplitter(self.tab_2)
        self.splitter_7.setObjectName(u"splitter_7")
        self.splitter_7.setOrientation(Qt.Horizontal)
        self.label_7 = QLabel(self.splitter_7)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(80, 0))
        self.label_7.setMaximumSize(QSize(80, 16777215))
        self.splitter_7.addWidget(self.label_7)
        self.linGroupName = QLineEdit(self.splitter_7)
        self.linGroupName.setObjectName(u"linGroupName")
        self.splitter_7.addWidget(self.linGroupName)

        self.verticalLayout_3.addWidget(self.splitter_7)

        self.btnCreateGroup = QPushButton(self.tab_2)
        self.btnCreateGroup.setObjectName(u"btnCreateGroup")
        self.btnCreateGroup.setMinimumSize(QSize(0, 35))

        self.verticalLayout_3.addWidget(self.btnCreateGroup)

        self.line_2 = QFrame(self.tab_2)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_2)

        self.label_11 = QLabel(self.tab_2)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_3.addWidget(self.label_11)

        self.comGroups = QComboBox(self.tab_2)
        self.comGroups.setObjectName(u"comGroups")

        self.verticalLayout_3.addWidget(self.comGroups)

        self.splitter_10 = QSplitter(self.tab_2)
        self.splitter_10.setObjectName(u"splitter_10")
        self.splitter_10.setOrientation(Qt.Horizontal)
        self.lisGroupUsers = QListView(self.splitter_10)
        self.lisGroupUsers.setObjectName(u"lisGroupUsers")
        self.lisGroupUsers.setMinimumSize(QSize(0, 500))
        self.lisGroupUsers.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.splitter_10.addWidget(self.lisGroupUsers)
        self.splitter_13 = QSplitter(self.splitter_10)
        self.splitter_13.setObjectName(u"splitter_13")
        self.splitter_13.setOrientation(Qt.Vertical)
        self.btnRemoveUsersFromGroup = QPushButton(self.splitter_13)
        self.btnRemoveUsersFromGroup.setObjectName(u"btnRemoveUsersFromGroup")
        self.btnRemoveUsersFromGroup.setMinimumSize(QSize(0, 35))
        self.btnRemoveUsersFromGroup.setMaximumSize(QSize(25, 16777215))
        self.splitter_13.addWidget(self.btnRemoveUsersFromGroup)
        self.btnAddUsersToGroup = QPushButton(self.splitter_13)
        self.btnAddUsersToGroup.setObjectName(u"btnAddUsersToGroup")
        self.btnAddUsersToGroup.setMinimumSize(QSize(0, 35))
        self.btnAddUsersToGroup.setMaximumSize(QSize(25, 16777215))
        self.splitter_13.addWidget(self.btnAddUsersToGroup)
        self.splitter_10.addWidget(self.splitter_13)
        self.lisUsers = QListView(self.splitter_10)
        self.lisUsers.setObjectName(u"lisUsers")
        self.lisUsers.setMinimumSize(QSize(0, 500))
        self.lisUsers.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.splitter_10.addWidget(self.lisUsers)

        self.verticalLayout_3.addWidget(self.splitter_10)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_4 = QVBoxLayout(self.tab_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.splitter_8 = QSplitter(self.tab_3)
        self.splitter_8.setObjectName(u"splitter_8")
        self.splitter_8.setOrientation(Qt.Horizontal)
        self.label_8 = QLabel(self.splitter_8)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(120, 0))
        self.label_8.setMaximumSize(QSize(120, 16777215))
        self.splitter_8.addWidget(self.label_8)
        self.comGroupsFoExpense = QComboBox(self.splitter_8)
        self.comGroupsFoExpense.setObjectName(u"comGroupsFoExpense")
        self.splitter_8.addWidget(self.comGroupsFoExpense)

        self.verticalLayout_4.addWidget(self.splitter_8)

        self.tabExpenses = QTableView(self.tab_3)
        self.tabExpenses.setObjectName(u"tabExpenses")

        self.verticalLayout_4.addWidget(self.tabExpenses)

        self.splitter_9 = QSplitter(self.tab_3)
        self.splitter_9.setObjectName(u"splitter_9")
        self.splitter_9.setOrientation(Qt.Horizontal)
        self.label_9 = QLabel(self.splitter_9)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(120, 0))
        self.label_9.setMaximumSize(QSize(120, 16777215))
        self.splitter_9.addWidget(self.label_9)
        self.linExpenceName = QLineEdit(self.splitter_9)
        self.linExpenceName.setObjectName(u"linExpenceName")
        self.splitter_9.addWidget(self.linExpenceName)
        self.linExpenceAmount = QLineEdit(self.splitter_9)
        self.linExpenceAmount.setObjectName(u"linExpenceAmount")
        self.splitter_9.addWidget(self.linExpenceAmount)

        self.verticalLayout_4.addWidget(self.splitter_9)

        self.btnCreateExpense = QPushButton(self.tab_3)
        self.btnCreateExpense.setObjectName(u"btnCreateExpense")
        self.btnCreateExpense.setMinimumSize(QSize(0, 35))

        self.verticalLayout_4.addWidget(self.btnCreateExpense)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.verticalLayout_5 = QVBoxLayout(self.tab_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.splitter_11 = QSplitter(self.tab_4)
        self.splitter_11.setObjectName(u"splitter_11")
        self.splitter_11.setOrientation(Qt.Horizontal)
        self.label_10 = QLabel(self.splitter_11)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(120, 0))
        self.label_10.setMaximumSize(QSize(120, 16777215))
        self.splitter_11.addWidget(self.label_10)
        self.comUsersBalance = QComboBox(self.splitter_11)
        self.comUsersBalance.setObjectName(u"comUsersBalance")
        self.splitter_11.addWidget(self.comUsersBalance)

        self.verticalLayout_5.addWidget(self.splitter_11)

        self.tabBalace = QTableView(self.tab_4)
        self.tabBalace.setObjectName(u"tabBalace")

        self.verticalLayout_5.addWidget(self.tabBalace)

        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.verticalLayout_6 = QVBoxLayout(self.tab_5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.splitter_12 = QSplitter(self.tab_5)
        self.splitter_12.setObjectName(u"splitter_12")
        self.splitter_12.setOrientation(Qt.Horizontal)
        self.label_12 = QLabel(self.splitter_12)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(80, 0))
        self.label_12.setMaximumSize(QSize(80, 16777215))
        self.splitter_12.addWidget(self.label_12)
        self.comUserPayFrom = QComboBox(self.splitter_12)
        self.comUserPayFrom.setObjectName(u"comUserPayFrom")
        self.splitter_12.addWidget(self.comUserPayFrom)

        self.verticalLayout_6.addWidget(self.splitter_12)

        self.splitter_15 = QSplitter(self.tab_5)
        self.splitter_15.setObjectName(u"splitter_15")
        self.splitter_15.setOrientation(Qt.Horizontal)
        self.label_13 = QLabel(self.splitter_15)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(80, 0))
        self.label_13.setMaximumSize(QSize(80, 16777215))
        self.splitter_15.addWidget(self.label_13)
        self.comUserPayTo = QComboBox(self.splitter_15)
        self.comUserPayTo.setObjectName(u"comUserPayTo")
        self.splitter_15.addWidget(self.comUserPayTo)

        self.verticalLayout_6.addWidget(self.splitter_15)

        self.splitter_14 = QSplitter(self.tab_5)
        self.splitter_14.setObjectName(u"splitter_14")
        self.splitter_14.setOrientation(Qt.Horizontal)
        self.label_14 = QLabel(self.splitter_14)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(80, 0))
        self.label_14.setMaximumSize(QSize(80, 16777215))
        self.splitter_14.addWidget(self.label_14)
        self.linPayAmount = QLineEdit(self.splitter_14)
        self.linPayAmount.setObjectName(u"linPayAmount")
        self.splitter_14.addWidget(self.linPayAmount)
        self.btnSubmitPayment = QPushButton(self.splitter_14)
        self.btnSubmitPayment.setObjectName(u"btnSubmitPayment")
        self.splitter_14.addWidget(self.btnSubmitPayment)

        self.verticalLayout_6.addWidget(self.splitter_14)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_3)

        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.tabWidget.addTab(self.tab_6, "")

        self.verticalLayout.addWidget(self.tabWidget)

        SplitSmart.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(SplitSmart)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 453, 21))
        SplitSmart.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(SplitSmart)
        self.statusbar.setObjectName(u"statusbar")
        SplitSmart.setStatusBar(self.statusbar)

        self.retranslateUi(SplitSmart)

        self.tabWidget.setCurrentIndex(4)


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
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), QCoreApplication.translate("SplitSmart", u"Users", None))
        self.label_7.setText(QCoreApplication.translate("SplitSmart", u"Group Name", None))
        self.btnCreateGroup.setText(QCoreApplication.translate("SplitSmart", u"Create Group", None))
        self.label_11.setText(QCoreApplication.translate("SplitSmart", u"Manage Group Users: Group Users << >> All Users", None))
        self.btnRemoveUsersFromGroup.setText(QCoreApplication.translate("SplitSmart", u">>", None))
        self.btnAddUsersToGroup.setText(QCoreApplication.translate("SplitSmart", u"<<", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("SplitSmart", u"Groups", None))
        self.label_8.setText(QCoreApplication.translate("SplitSmart", u"Group for Expense", None))
        self.label_9.setText(QCoreApplication.translate("SplitSmart", u"Expence Name | Amount", None))
        self.btnCreateExpense.setText(QCoreApplication.translate("SplitSmart", u"Create Expense for Current Group", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("SplitSmart", u"Expenses", None))
        self.label_10.setText(QCoreApplication.translate("SplitSmart", u"Select User", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("SplitSmart", u"Balance Tracking", None))
        self.label_12.setText(QCoreApplication.translate("SplitSmart", u"Fro User: ", None))
        self.label_13.setText(QCoreApplication.translate("SplitSmart", u"To User: ", None))
        self.label_14.setText(QCoreApplication.translate("SplitSmart", u"Amount: ", None))
        self.btnSubmitPayment.setText(QCoreApplication.translate("SplitSmart", u"Submit Payment", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("SplitSmart", u"Payment", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QCoreApplication.translate("SplitSmart", u"Reports", None))
    # retranslateUi


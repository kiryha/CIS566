# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_HotelRoom(object):
    def setupUi(self, HotelRoom):
        if not HotelRoom.objectName():
            HotelRoom.setObjectName(u"HotelRoom")
        HotelRoom.resize(322, 380)
        self.centralwidget = QWidget(HotelRoom)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.label_2 = QLabel(self.splitter)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(80, 16777215))
        self.splitter.addWidget(self.label_2)
        self.comRoomType = QComboBox(self.splitter)
        self.comRoomType.setObjectName(u"comRoomType")
        self.splitter.addWidget(self.comRoomType)

        self.verticalLayout.addWidget(self.splitter)

        self.splitter_2 = QSplitter(self.centralwidget)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.label_3 = QLabel(self.splitter_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(80, 16777215))
        self.splitter_2.addWidget(self.label_3)
        self.linBidAmount = QLineEdit(self.splitter_2)
        self.linBidAmount.setObjectName(u"linBidAmount")
        self.splitter_2.addWidget(self.linBidAmount)

        self.verticalLayout.addWidget(self.splitter_2)

        self.btnBid = QPushButton(self.centralwidget)
        self.btnBid.setObjectName(u"btnBid")
        self.btnBid.setMinimumSize(QSize(0, 35))

        self.verticalLayout.addWidget(self.btnBid)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.txtResults = QTextEdit(self.centralwidget)
        self.txtResults.setObjectName(u"txtResults")

        self.verticalLayout.addWidget(self.txtResults)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        HotelRoom.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(HotelRoom)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 322, 21))
        HotelRoom.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(HotelRoom)
        self.statusbar.setObjectName(u"statusbar")
        HotelRoom.setStatusBar(self.statusbar)

        self.retranslateUi(HotelRoom)

        QMetaObject.connectSlotsByName(HotelRoom)
    # setupUi

    def retranslateUi(self, HotelRoom):
        HotelRoom.setWindowTitle(QCoreApplication.translate("HotelRoom", u"Hotel Room", None))
        self.label_2.setText(QCoreApplication.translate("HotelRoom", u"Room Type", None))
        self.label_3.setText(QCoreApplication.translate("HotelRoom", u"Bid Amount", None))
        self.btnBid.setText(QCoreApplication.translate("HotelRoom", u"Bid Selected Room Type", None))
        self.label.setText(QCoreApplication.translate("HotelRoom", u"Bid Results", None))
    # retranslateUi


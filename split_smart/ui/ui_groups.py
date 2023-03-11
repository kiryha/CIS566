# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_groups.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_GroupManager(object):
    def setupUi(self, GroupManager):
        if not GroupManager.objectName():
            GroupManager.setObjectName(u"GroupManager")
        GroupManager.resize(271, 568)
        self.verticalLayout = QVBoxLayout(GroupManager)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(GroupManager)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(GroupManager)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.lisGroups = QListView(GroupManager)
        self.lisGroups.setObjectName(u"lisGroups")

        self.verticalLayout.addWidget(self.lisGroups)

        self.pushButton_2 = QPushButton(GroupManager)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(0, 35))

        self.verticalLayout.addWidget(self.pushButton_2)

        self.label_3 = QLabel(GroupManager)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.lisUsers = QListView(GroupManager)
        self.lisUsers.setObjectName(u"lisUsers")

        self.verticalLayout.addWidget(self.lisUsers)

        self.pushButton = QPushButton(GroupManager)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 35))

        self.verticalLayout.addWidget(self.pushButton)


        self.retranslateUi(GroupManager)

        QMetaObject.connectSlotsByName(GroupManager)
    # setupUi

    def retranslateUi(self, GroupManager):
        GroupManager.setWindowTitle(QCoreApplication.translate("GroupManager", u"Manage Group Users", None))
        self.label.setText(QCoreApplication.translate("GroupManager", u"Group Name:", None))
        self.label_2.setText(QCoreApplication.translate("GroupManager", u"Group Members", None))
        self.pushButton_2.setText(QCoreApplication.translate("GroupManager", u"Remove Selected Users", None))
        self.label_3.setText(QCoreApplication.translate("GroupManager", u"Users", None))
        self.pushButton.setText(QCoreApplication.translate("GroupManager", u"Add Selected Users", None))
    # retranslateUi


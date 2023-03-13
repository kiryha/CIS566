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
        self.labGroupName = QLabel(GroupManager)
        self.labGroupName.setObjectName(u"labGroupName")

        self.verticalLayout.addWidget(self.labGroupName)

        self.label_2 = QLabel(GroupManager)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.lisGroupUsers = QListView(GroupManager)
        self.lisGroupUsers.setObjectName(u"lisGroupUsers")
        self.lisGroupUsers.setSelectionMode(QAbstractItemView.ExtendedSelection)

        self.verticalLayout.addWidget(self.lisGroupUsers)

        self.btnRemoveUsersFromGroup = QPushButton(GroupManager)
        self.btnRemoveUsersFromGroup.setObjectName(u"btnRemoveUsersFromGroup")
        self.btnRemoveUsersFromGroup.setMinimumSize(QSize(0, 35))

        self.verticalLayout.addWidget(self.btnRemoveUsersFromGroup)

        self.label_3 = QLabel(GroupManager)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.lisUsers = QListView(GroupManager)
        self.lisUsers.setObjectName(u"lisUsers")
        self.lisUsers.setSelectionMode(QAbstractItemView.ExtendedSelection)

        self.verticalLayout.addWidget(self.lisUsers)

        self.btnAddUsersToGroup = QPushButton(GroupManager)
        self.btnAddUsersToGroup.setObjectName(u"btnAddUsersToGroup")
        self.btnAddUsersToGroup.setMinimumSize(QSize(0, 35))

        self.verticalLayout.addWidget(self.btnAddUsersToGroup)


        self.retranslateUi(GroupManager)

        QMetaObject.connectSlotsByName(GroupManager)
    # setupUi

    def retranslateUi(self, GroupManager):
        GroupManager.setWindowTitle(QCoreApplication.translate("GroupManager", u"Manage Group Users", None))
        self.labGroupName.setText(QCoreApplication.translate("GroupManager", u"Group Name:", None))
        self.label_2.setText(QCoreApplication.translate("GroupManager", u"Group Members", None))
        self.btnRemoveUsersFromGroup.setText(QCoreApplication.translate("GroupManager", u"Remove Selected Users", None))
        self.label_3.setText(QCoreApplication.translate("GroupManager", u"Users", None))
        self.btnAddUsersToGroup.setText(QCoreApplication.translate("GroupManager", u"Add Selected Users", None))
    # retranslateUi


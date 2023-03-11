"""
CIS 566 Term Project: Split Smart - share expenses
"""

import os
import sqlite3
from PySide2 import QtWidgets, QtCore, QtGui
from ui import ui_main
from ui import ui_groups


# Database
def init_database(sql_file_path):
    """
    Create Database
    """

    connection = sqlite3.connect(sql_file_path)
    cursor = connection.cursor()

    cursor.execute('''CREATE TABLE "user" (
                    id integer primary key autoincrement,
                    first_name text,
                    last_name text,
                    email text,
                    password text,
                    description text
                    )''')

    cursor.execute('''CREATE TABLE "group" (
                    id integer primary key autoincrement,
                    name text,
                    description text
                    )''')

    cursor.execute('''CREATE TABLE "user_group" (
                    id integer primary key autoincrement,
                    user_id integer,
                    group_id integer,
                    description text,
                    FOREIGN KEY(user_id) REFERENCES "user"(id),
                    FOREIGN KEY(group_id) REFERENCES "group"(id)
                    )''')

    connection.commit()
    connection.close()


class User:
    def __init__(self, user_tuple):
        self.id = None
        self.first_name = user_tuple[1]
        self.last_name = user_tuple[2]
        self.email = user_tuple[3]
        self.password = user_tuple[4]
        self.description = user_tuple[5]


class Group:
    def __init__(self):
        self.id = None
        self.name = None
        self.description = ''


class UserGroup:
    def __init__(self):
        self.id = None
        self.user_id = None
        self.group_id = None
        self.description = ''


class Balance:
    def __init__(self):
        self.id = None
        self.balance = None
        self.user_id = ''
        self.description = ''


class Database:
    def __init__(self, sql_file_path):
        self.sql_file_path = sql_file_path

    # Tuple to object conversion
    def convert_to_user(self, user_tuples):

        users = []

        for user_tuple in user_tuples:
            user = User(user_tuple)
            users.append(user)

        return users

    def add_user(self, user_tuple):

        user = User(user_tuple)

        connection = sqlite3.connect(self.sql_file_path)
        cursor = connection.cursor()

        # Add object to DB
        cursor.execute("INSERT INTO 'user' VALUES ("
                       ":id,"
                       ":first_name,"
                       ":last_name,"
                       ":email,"
                       ":password,"
                       ":description)",

                       {'id': cursor.lastrowid,
                        'first_name': user.first_name,
                        'last_name': user.last_name,
                        'email': user.email,
                        'password': user.password,
                        'description': user.description})

        connection.commit()
        user.id = cursor.lastrowid  # Add database ID to the object
        connection.close()

        # print 'User {0} {1} added!'.format(user.first_name, user.last_name)
        return user

    def add_group(self, group_name):

        connection = sqlite3.connect(self.sql_file_path)
        cursor = connection.cursor()

        # Add object to DB
        cursor.execute("INSERT INTO 'group' VALUES ("
                       ":id,"
                       ":name,"
                       ":description)",

                       {'id': cursor.lastrowid,
                        'name': group_name,
                        'description': ''})

        connection.commit()
        connection.close()

    def get_groups(self):

        connection = sqlite3.connect(self.sql_file_path)
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM 'group'")
        group_tuples = cursor.fetchall()

        connection.commit()
        connection.close()

        print(group_tuples)

        return group_tuples

    def add_user_to_group(self, user_id, group_id):

        connection = sqlite3.connect(self.sql_file_path)
        cursor = connection.cursor()

        # Add object to DB
        cursor.execute("INSERT INTO 'user_group' VALUES ("
                       ":id,"
                       ":user_id,"
                       ":group_id,"
                       ":description)",

                       {'id': cursor.lastrowid,
                        'user_id': user_id,
                        'group_id': group_id,
                        'description': ''})

        connection.commit()
        connection.close()


# Data Models
class ListModel(QtCore.QAbstractListModel):
    def __init__(self, data, parent=None):
        QtCore.QAbstractListModel.__init__(self, parent)
        self._data = data

    def rowCount(self, parent):

        return len(self._data)

    def data(self, index, role):

        if not index.isValid():
            return

        # Get selected row
        row_index = index.row()
        data = self._data[row_index]

        if role == QtCore.Qt.DisplayRole:  # Display name in UI
            return data.name
        # if role == QtCore.Qt.UserRole + 1:  # Return ID
        #     return data.id
        # if role == QtCore.Qt.UserRole + 2:  # Return NAME
        #     return data.name
        # if role == QtCore.Qt.UserRole + 3:  # Return PATH
        #     return data.path


class GroupManager(QtWidgets.QDialog, ui_groups.Ui_GroupManager):
    def __init__(self, parent=None):
        super(GroupManager, self).__init__(parent=parent)
        self.setupUi(self)
        self.parent = parent

        self.model_groups = None
        self.model_users = None

    def showEvent(self, event):

        self.lisGroups.setModel(self.model_groups)
        self.lisUsers.setModel(self.model_users)


class SplitSmart(QtWidgets.QMainWindow, ui_main.Ui_SplitSmart):
    def __init__(self):
        super(SplitSmart, self).__init__()
        self.setupUi(self)

        self.sql_file_path = f'{root}/database/data.db'
        self.init_database()
        self.database = Database(self.sql_file_path)

        self.init_ui()

        self.group_manager = GroupManager(self)

        self.btnSignUp.clicked.connect(self.sign_up_user)
        self.btnCreateGroup.clicked.connect(self.create_group)
        self.btnManageGroupUsers.clicked.connect(self.manage_groups)

        self.btnSplitSmart.clicked.connect(self.test)

    def init_database(self):

        if not os.path.exists(self.sql_file_path):
            init_database(self.sql_file_path)

    def init_ui(self):

        groups = self.database.get_groups()
        # self.comGroups.addItems()

    def sign_up_user(self):

        user_first_name = self.linSignupName.text()
        user_last_name = self.linSignupLastName.text()
        user_email = self.linSignupEmail.text()
        user_password = self.linSignupPassword.text()

        print(f'Signing Up User {user_first_name} {user_last_name}...')

        user_tuple = [None, user_first_name, user_last_name, user_email, user_password, '']
        
        self.database.add_user(user_tuple)

    def create_group(self):

        group_name = self.linGroupName.text()
        self.database.add_group(group_name)

    def manage_groups(self):

        self.group_manager.model_groups = ListModel([])
        self.group_manager.model_users = ListModel([])

        self.group_manager.exec_()

    def test(self):

        print('Split Smart')


if __name__ == "__main__":
    root = os.path.dirname(os.path.abspath(__file__))
    app = QtWidgets.QApplication([])
    split_smart = SplitSmart()
    split_smart.setWindowIcon(QtGui.QIcon('{0}/icons/split_smart.ico'.format(root)))
    split_smart.show()
    app.exec_()

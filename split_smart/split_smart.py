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


def populate_database(sql_file_path):

    populate_data = {
        'users': [
            {'id': 1,
             'first_name': 'Kiryha',
             'last_name': 'Krysko',
             'email': 'coder@umich.edu',
             'password': '123',
             'description': ''},

            {'id': 2,
             'first_name': 'Yulia',
             'last_name': 'Basko',
             'email': 'jbasko@umich.edu',
             'password': 'sonechko',
             'description': ''},

            {'id': 3,
             'first_name': 'Rodriges',
             'last_name': 'Bender',
             'email': 'bender@umich.edu',
             'password': 'futurama',
             'description': ''}],

        'groups': [
            {'id': 1,
             'name': 'Penoplast',
             'description': ''},

            {'id': 2,
             'name': 'Booze',
             'description': ''}]}

    for user_data in populate_data['users']:

        connection = sqlite3.connect(sql_file_path)
        cursor = connection.cursor()

        cursor.execute("INSERT INTO 'user' VALUES ("
                       ":id,"
                       ":first_name,"
                       ":last_name,"
                       ":email,"
                       ":password,"
                       ":description)",

                       {'id': user_data['id'],
                        'first_name': user_data['first_name'],
                        'last_name': user_data['last_name'],
                        'email': user_data['email'],
                        'password': user_data['password'],
                        'description': ''})

        connection.commit()
        connection.close()

    for group_data in populate_data['groups']:

        connection = sqlite3.connect(sql_file_path)
        cursor = connection.cursor()

        cursor.execute("INSERT INTO 'group' VALUES ("
                       ":id,"
                       ":name,"
                       ":description)",

                       {'id': group_data['id'],
                        'name': group_data['name'],
                        'description': ''})

        connection.commit()
        connection.close()


class User:
    def __init__(self, user_tuple):
        self.id = user_tuple[0]
        self.first_name = user_tuple[1]
        self.last_name = user_tuple[2]
        self.email = user_tuple[3]
        self.password = user_tuple[4]
        self.description = user_tuple[5]


class Group:
    def __init__(self, group_tuple):
        self.id = group_tuple[0]
        self.name = group_tuple[1]
        self.description = group_tuple[2]


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
        self.users = []
        self.groups = []

        self.init_database()

    def init_database(self):

        self.users.extend(self.get_users())

    # Tuple to object conversion
    def convert_to_user(self, user_tuples):

        users = []

        for user_tuple in user_tuples:
            user = User(user_tuple)
            users.append(user)

        return users

    def convert_to_group(self, group_tuples):

        groups = []

        for group_tuple in group_tuples:
            groups.append(Group(group_tuple))

        return groups

    # CRUD
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
        self.users.append(user)

        return user

    def get_users(self):

        connection = sqlite3.connect(self.sql_file_path)
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM 'user'")
        user_tuples = cursor.fetchall()

        connection.commit()
        connection.close()

        if user_tuples:
            return self.convert_to_user(user_tuples)

    def add_group(self, group_tuple):

        group = Group(group_tuple)

        connection = sqlite3.connect(self.sql_file_path)
        cursor = connection.cursor()

        # Add object to DB
        cursor.execute("INSERT INTO 'group' VALUES ("
                       ":id,"
                       ":name,"
                       ":description)",

                       {'id': cursor.lastrowid,
                        'name': group.name,
                        'description': ''})

        connection.commit()
        group.id = cursor.lastrowid  # Add database ID to the object
        connection.close()

        self.groups.append(group)

        return group

    def get_groups(self):

        connection = sqlite3.connect(self.sql_file_path)
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM 'group'")
        group_tuples = cursor.fetchall()

        connection.commit()
        connection.close()

        if group_tuples:
            return self.convert_to_group(group_tuples)

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
    def __init__(self, database, attribute, parent=None):
        QtCore.QAbstractListModel.__init__(self, parent)
        self.database = database
        self.attribute = attribute

    def rowCount(self, parent):

        if self.attribute == 'groups':
            return len(self.database.groups)

        if self.attribute == 'users':
            return len(self.database.users)

    def data(self, index, role):

        if not index.isValid():
            return

        # Get selected row
        row_index = index.row()

        if self.attribute == 'groups':
            obj = self.database.groups[row_index]
        if self.attribute == 'users':
            obj = self.database.users[row_index]

        if role == QtCore.Qt.DisplayRole:  # Display name in UI

            if self.attribute == 'groups':
                return obj.name
            if self.attribute == 'users':
                return obj.first_name

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

        self.lisGroupMembers.setModel(self.model_groups)
        print(self.model_users)
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
            populate_database(self.sql_file_path)

    def init_ui(self):

        groups = self.database.get_groups()

        for group in groups:
            self.comGroups.addItem(group.name)

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
        group_tuple = [None, group_name, '']

        self.database.add_group(group_tuple)

    def manage_groups(self):

        group_name = self.comGroups.currentText()
        self.group_manager.labGroupName.setText(f'Group Name: {group_name}')
        self.group_manager.model_users = ListModel(self.database, 'users')

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

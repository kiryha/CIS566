"""
CIS 566 Term Project: Split Smart - share expenses
"""

import os
import sqlite3
from PySide2 import QtWidgets, QtGui
from ui import split_smart_main


# Database
def init_database(sql_file_path):
    """
    Create Database
    """

    connection = sqlite3.connect(sql_file_path)
    cursor = connection.cursor()

    cursor.execute('''CREATE TABLE user (
                    id integer primary key autoincrement,
                    first_name text,
                    last_name text,
                    email text,
                    password text,
                    description text
                    )''')

    connection.commit()
    connection.close()


class User:
    def __init__(self):
        self.id = None
        self.first_name = ''
        self.last_name = ''
        self.email = ''
        self.password = ''
        self.description = ''


class Database:
    def __init__(self, sql_file_path):
        self.sql_file_path = sql_file_path

    def add_user(self, user_name, user_last_name, user_email, user_password):

        connection = sqlite3.connect(self.sql_file_path)
        cursor = connection.cursor()

        # Add object to DB
        cursor.execute("INSERT INTO user VALUES ("
                       ":id,"
                       ":first_name,"
                       ":last_name,"
                       ":email,"
                       ":password,"
                       ":description)",

                       {'id': cursor.lastrowid,
                        'first_name': user_name,
                        'last_name': user_last_name,
                        'email': user_email,
                        'password': user_password,
                        'description': ''})

        connection.commit()
        # user.id = cursor.lastrowid  # Add database ID to the object
        connection.close()

        # print 'User {0} {1} added!'.format(user.first_name, user.last_name)
        # return user


class SplitSmart(QtWidgets.QMainWindow, split_smart_main.Ui_SplitSmart):
    def __init__(self):
        super(SplitSmart, self).__init__()
        self.setupUi(self)

        self.sql_file_path = f'{root}/database/data.db'
        self.init_database()
        self.database = Database(self.sql_file_path)

        self.btnSignUp.clicked.connect(self.sign_up_user)
        self.btnSplitSmart.clicked.connect(self.test)

    def init_database(self):

        if not os.path.exists(self.sql_file_path):
            init_database(self.sql_file_path)

    def sign_up_user(self):

        user_name = self.linSignupName.text()
        user_last_name = self.linSignupLastName.text()
        user_email = self.linSignupEmail.text()
        user_password = self.linSignupPassword.text()

        print(f'Signing Up User {user_name} {user_last_name}...')

        self.database.add_user(user_name, user_last_name, user_email, user_password)

    def test(self):

        print('Split Smart')


if __name__ == "__main__":
    root = os.path.dirname(os.path.abspath(__file__))
    app = QtWidgets.QApplication([])
    split_smart = SplitSmart()
    split_smart.setWindowIcon(QtGui.QIcon('{0}/icons/split_smart.ico'.format(root)))
    split_smart.show()
    app.exec_()

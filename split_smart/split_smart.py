"""
CIS 566 Term Project: Split Smart - share expenses
Python 3.7 + Pyside 2
"""

import os
import time
import sqlite3
import smtplib
from PySide2 import QtWidgets, QtCore, QtGui
from ui import ui_main


# Database
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


class GroupUser:
    def __init__(self):
        self.id = None
        self.user_id = None
        self.group_id = None
        self.description = ''


class Balance:
    def __init__(self, balance_tuple):
        self.id = balance_tuple[0]
        self.amount = balance_tuple[1]
        self.user_id = balance_tuple[2]
        self.description = balance_tuple[3]


class Expense:
    def __init__(self, expense_tuple):
        self.id = expense_tuple[0]
        self.name = expense_tuple[1]
        self.amount = expense_tuple[2]
        self.date = expense_tuple[3]
        self.description = expense_tuple[4]


class UserExpense:
    def __init__(self, user_expense_tuple):
        self.id = user_expense_tuple[0]
        self.expense_id = user_expense_tuple[1]
        self.user_id = user_expense_tuple[2]
        self.group_id = user_expense_tuple[3]
        self.amount = user_expense_tuple[4]
        self.description = user_expense_tuple[5]


class Payment:
    def __init__(self, payment_tuple):
        self.id = payment_tuple[0]
        self.user_from_id = payment_tuple[1]
        self.user_to_id = payment_tuple[2]
        self.amount = payment_tuple[3]
        self.date = payment_tuple[4]
        self.description = payment_tuple[5]


class Database:
    __instance = None

    def __init__(self, sql_file_path):
        self.sql_file_path = sql_file_path

        # Singleton setup
        if Database.__instance is not None:
            return
        else:
            Database.__instance = self

        # Static data
        self.users = []
        self.groups = []
        # Dynamic data
        self.user_expenses = []
        self.user_balances = []
        self.payments = []
        self.user_expense_report = []

        self.init_database()

    def get_instance(sql_file_path):

        # Get Singe Database() instance
        if Database.__instance is None:
            Database(sql_file_path)

        return Database.__instance

    def init_database(self):

        self.users.extend(self.get_users())
        self.groups.extend(self.get_groups())

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

    def convert_to_expense(self, expense_tuples):

        expenses = []

        for expense_tuple in expense_tuples:
            expenses.append(Expense(expense_tuple))

        return expenses

    def convert_to_user_expense(self, user_expense_tuples):

        user_expenses = []

        for user_expense_tuple in user_expense_tuples:
            user_expenses.append(UserExpense(user_expense_tuple))

        return user_expenses

    def convert_to_payment(self, payment_tuples):

        payments = []

        for payment_tuple in payment_tuples:
            payments.append(Payment(payment_tuple))

        return payments

    # CRUD
    # Users
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

        print(f'>> database.add_user: Name = {user.first_name} {user.last_name}')

        self.users.append(user)

        return user

    def get_user(self, user_id):

        connection = sqlite3.connect(self.sql_file_path)
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM 'user' WHERE id=:id",
                       {'id': user_id})
        user_tuple = cursor.fetchone()

        connection.commit()
        connection.close()

        if user_tuple:
            return self.convert_to_user([user_tuple])[0]

    def get_users(self):

        connection = sqlite3.connect(self.sql_file_path)
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM 'user'")
        user_tuples = cursor.fetchall()

        connection.commit()
        connection.close()

        if user_tuples:
            return self.convert_to_user(user_tuples)

    # Groups
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

        print(f'>> database.add_group: Name = {group.name}')

        self.groups.append(group)

        return group

    def get_group(self, group_id):

        connection = sqlite3.connect(self.sql_file_path)
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM 'group' WHERE id=:id",
                       {'id': group_id})

        group_tuple = cursor.fetchone()

        connection.commit()
        connection.close()

        if group_tuple:
            return self.convert_to_group([group_tuple])[0]

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

        user_name = f'{self.get_user(user_id).first_name} {self.get_user(user_id).last_name}'
        group_name = self.get_group(group_id).name

        connection = sqlite3.connect(self.sql_file_path)
        cursor = connection.cursor()

        # Add object to DB
        cursor.execute("INSERT INTO 'group_user' VALUES ("
                       ":id,"
                       ":user_id,"
                       ":group_id,"
                       ":description)",

                       {'id': cursor.lastrowid,
                        'user_id': user_id,
                        'group_id': group_id,
                        'description': f'{user_name} in {group_name}'})

        connection.commit()
        connection.close()

        print(f'>> database.add_user_to_group: User| Group Names = {user_name} | {group_name}')

    def remove_user_from_group(self, user_id, group_id):

        user_name = f'{self.get_user(user_id).first_name} {self.get_user(user_id).last_name}'
        group_name = self.get_group(group_id).name

        connection = sqlite3.connect(self.sql_file_path)
        cursor = connection.cursor()

        cursor.execute("DELETE FROM 'group_user' "
                       "WHERE user_id=:user_id "
                       "AND group_id=:group_id",

                       {'user_id': user_id, 'group_id': group_id})

        connection.commit()
        connection.close()

        print(f'>> database.remove_user_from_group: User| Group Names = {user_name} | {group_name}')

    def get_group_users(self, group_id):

        group_users = []

        connection = sqlite3.connect(self.sql_file_path)
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM 'group_user' WHERE group_id=:group_id",
                       {'group_id': group_id})

        group_user_tuples = cursor.fetchall()

        connection.close()

        if group_user_tuples:

            for group_user_tuple in group_user_tuples:
                user = self.get_user(group_user_tuple[1])
                group_users.append(user)

        return group_users

    # Expenses
    def add_expense(self, expense_tuple, group_id):

        expense = Expense(expense_tuple)
        group_name = self.get_group(group_id).name

        connection = sqlite3.connect(self.sql_file_path)
        cursor = connection.cursor()

        # Add object to DB
        cursor.execute("INSERT INTO 'expense' VALUES ("
                       ":id,"
                       ":name,"
                       ":amount,"
                       ":date,"
                       ":description)",

                       {'id': cursor.lastrowid,
                        'name': expense.name,
                        'amount': expense.amount,
                        'date': expense.date,
                        'description': f'For group: {group_name}'})

        connection.commit()
        expense.id = cursor.lastrowid  # Add database ID to the object
        connection.close()

        print(f'>> database.add_expense: Group | Expense Names = {group_name} | {expense.name}, Amount = {expense.amount}')

        # Get group users and add user expenses
        group_users = self.get_group_users(group_id)

        for user in group_users:
            user_expense_tuple = [None, expense.id, user.id, group_id, 0, '']
            self.add_user_expense(user_expense_tuple)

    def get_expense(self, expense_id):

        connection = sqlite3.connect(self.sql_file_path)
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM 'expense' WHERE id=:id",
                       {'id': expense_id})

        expense_tuple = cursor.fetchone()

        connection.commit()
        connection.close()

        if expense_tuple:
            return self.convert_to_expense([expense_tuple])[0]

    def add_user_expense(self, user_expense_tuple):

        user_expense = UserExpense(user_expense_tuple)
        expense_name = self.get_expense(user_expense.expense_id).name
        user_name = f'{self.get_user(user_expense.user_id).first_name} {self.get_user(user_expense.user_id).last_name}'

        connection = sqlite3.connect(self.sql_file_path)
        cursor = connection.cursor()

        # Add object to DB
        cursor.execute("INSERT INTO 'user_expense' VALUES ("
                       ":id,"
                       ":expense_id,"
                       ":user_id,"
                       ":group_id,"
                       ":amount,"
                       ":description)",

                       {'id': cursor.lastrowid,
                        'expense_id': user_expense.expense_id,
                        'user_id': user_expense.user_id,
                        'group_id': user_expense.group_id,
                        'amount': user_expense.amount,
                        'description': f'Expense {expense_name} for {user_name}'})

        connection.commit()
        user_expense.id = cursor.lastrowid  # Add database ID to the object
        connection.close()

        print(f'>> database.add_user_expense: Expense Name = {expense_name}, User = {user_name}')

        self.user_expenses.append(user_expense)

        return user_expense

    def get_user_expenses(self, group_id):

        # Clean up data
        del self.user_expenses[:]

        connection = sqlite3.connect(self.sql_file_path)
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM 'user_expense' WHERE group_id=:group_id",
                       {'group_id': group_id})

        user_expense_tuples = cursor.fetchall()

        connection.commit()
        connection.close()

        if user_expense_tuples:
            user_expenses = self.convert_to_user_expense(user_expense_tuples)
            self.user_expenses.extend(user_expenses)

    def get_user_expenses_report(self, user_id):

        # Clean up data
        del self.user_expense_report[:]

        connection = sqlite3.connect(self.sql_file_path)
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM 'user_expense' WHERE user_id=:user_id",
                       {'user_id': user_id})

        user_expense_tuples = cursor.fetchall()

        connection.commit()
        connection.close()

        if user_expense_tuples:
            user_expenses = self.convert_to_user_expense(user_expense_tuples)
            self.user_expense_report.extend(user_expenses)

    def get_user_expense(self, user_expense_id):

        connection = sqlite3.connect(self.sql_file_path)
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM 'user_expense' WHERE id=:id",
                       {'id': user_expense_id})

        user_expense_tuple = cursor.fetchone()

        connection.commit()
        connection.close()

        if user_expense_tuple:
            return self.convert_to_user_expense([user_expense_tuple])[0]

    def update_user_expense(self, user_expense_id, amount):

        connection = sqlite3.connect(self.sql_file_path)
        cursor = connection.cursor()

        cursor.execute("UPDATE 'user_expense' SET "
                       "amount=:amount "

                       "WHERE id=:id",

                       {'id': user_expense_id,
                        'amount': amount})

        connection.commit()
        connection.close()

        user_expense = self.get_user_expense(user_expense_id)
        expense = self.get_expense(user_expense.expense_id)
        user_name = f'{self.get_user(user_expense.user_id).first_name} {self.get_user(user_expense.user_id).last_name}'

        print(f'>> database.update_user_expense: Expense Name = {expense.name}, User = {user_name}, Amount = {amount}')

    # Balance
    def calculate_user_expenses_amount(self, user_id):

        amount = 0

        connection = sqlite3.connect(self.sql_file_path)
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM 'user_expense' WHERE user_id=:user_id",
                       {'user_id': user_id})

        user_expense_tuples = cursor.fetchall()

        connection.commit()
        connection.close()

        for user_expense_tuple in user_expense_tuples:
            amount += user_expense_tuple[4]

        return amount

    def get_user_balance(self, user_id):

        current_user = self.get_user(user_id)
        users = self.get_users()

        # Get other users
        other_users = []
        for user in users:
            if user.id != user_id:
                other_users.append(user)

        del self.user_balances[:]

        # Populate balance data
        for user in other_users:

            # Calculate how much every other user spent in total
            amount = self.calculate_user_expenses_amount(user.id)

            balance_tuple = [None, amount, user.id, f'{user.first_name}']
            balance = Balance(balance_tuple)

            self.user_balances.append(balance)

    # Payment
    def add_payment(self, payment_tuple):

        payment = Payment(payment_tuple)

        connection = sqlite3.connect(self.sql_file_path)
        cursor = connection.cursor()

        # Add object to DB
        cursor.execute("INSERT INTO 'payment' VALUES ("
                       ":id,"
                       ":user_from_id,"
                       ":user_to_id,"
                       ":amount,"
                       ":date,"
                       ":description)",

                       {'id': cursor.lastrowid,
                        'user_from_id': payment.user_from_id,
                        'user_to_id': payment.user_to_id,
                        'amount': payment.amount,
                        'date': payment.date,
                        'description': payment.description})

        connection.commit()
        payment.id = cursor.lastrowid  # Add database ID to the object
        connection.close()

    def get_user_payments(self, user_id):

        del self.payments[:]

        connection = sqlite3.connect(self.sql_file_path)
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM 'payment' WHERE user_from_id=:user_from_id",
                       {'user_from_id': user_id})

        payment_tuples = cursor.fetchall()

        connection.commit()
        connection.close()

        if payment_tuples:
            payments = self.convert_to_payment(payment_tuples)
            self.payments.extend(payments)

            return payments


# Data Models
class ListModel(QtCore.QAbstractListModel):
    def __init__(self, database, attribute, group_id=None, parent=None):
        QtCore.QAbstractListModel.__init__(self, parent)
        # print(database,  attribute, group_id, parent)
        self.database = database
        self.attribute = attribute
        self.group_id = group_id
        self.group_users = []

    def rowCount(self, parent):

        if self.attribute == 'groups':
            return len(self.database.groups)

        if self.attribute == 'users':
            return len(self.database.users)

        if self.attribute == 'group_users':
            del self.group_users[:]
            self.group_users.extend(self.database.get_group_users(self.group_id))
            return len(self.group_users)

    def data(self, index, role):

        if not index.isValid():
            return

        # Get selected row
        row_index = index.row()

        if self.attribute == 'groups':
            obj = self.database.groups[row_index]
        if self.attribute == 'users':
            obj = self.database.users[row_index]
        if self.attribute == 'group_users':
            obj = self.group_users[row_index]

        if role == QtCore.Qt.DisplayRole:  # Display name in UI

            if self.attribute == 'groups':
                return obj.name
            if self.attribute == 'users':
                return f'{obj.first_name} {obj.last_name}'
            if self.attribute == 'group_users':
                return f'{obj.first_name} {obj.last_name}'

        if role == QtCore.Qt.UserRole + 1:  # Return object
            return obj


class ComboboxModel(QtCore.QAbstractListModel):
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
                return f'{obj.first_name} {obj.last_name}'

        if role == QtCore.Qt.UserRole + 1:  # Return object
            return obj


class UserExpenseModel(QtCore.QAbstractTableModel):
    def __init__(self, database, parent=None):
        QtCore.QAbstractTableModel.__init__(self, parent)
        self.database = database
        self.header = ['Expense Name', 'User Name', 'Amount']

    def flags(self, index):

        if index.column() == 2:
            return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable
        else:
            return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable

    def headerData(self, column, orientation, role):

        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self.header[column]

    def rowCount(self, parent):

        return len(self.database.user_expenses)

    def columnCount(self, parent):

        return len(self.header)

    def data(self, index, role):

        if not index.isValid():
            return

        row = index.row()
        column = index.column()

        if role == QtCore.Qt.DisplayRole:
            expense = self.database.get_expense(self.database.user_expenses[row].expense_id)

            if column == 0:
                return expense.name

            if column == 1:
                user = self.database.get_user(self.database.user_expenses[row].user_id)
                return f'{user.first_name} {user.last_name}'

            if column == 2:
                return self.database.user_expenses[row].amount

        if role == QtCore.Qt.EditRole:
            if column == 2:
                return self.database.user_expenses[row].amount

    def setData(self, index, input_data, role=QtCore.Qt.EditRole):

        row = index.row()
        column = index.column()

        if role == QtCore.Qt.EditRole:
            user_expense = self.database.user_expenses[row]
            if column == 2:
                self.database.update_user_expense(user_expense.id, input_data)
                self.database.get_user_expenses(user_expense.group_id)
                self.layoutChanged.emit()

            return True


class UserBalanceModel(QtCore.QAbstractTableModel):
    def __init__(self, database, parent=None):
        QtCore.QAbstractTableModel.__init__(self, parent)
        self.database = database
        self.header = ['User Name', 'Owes Amount']

    def flags(self, index):

        return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable

    def headerData(self, column, orientation, role):

        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self.header[column]

    def rowCount(self, parent):

        return len(self.database.user_balances)

    def columnCount(self, parent):

        return len(self.header)

    def data(self, index, role):

        if not index.isValid():
            return

        row = index.row()
        column = index.column()

        if role == QtCore.Qt.DisplayRole:

            balance = self.database.user_balances[row]
            user = self.database.get_user(balance.user_id)

            if column == 0:
                return f'{user.first_name} {user.last_name}'

            if column == 1:
                return balance.amount


class PaymentModel(QtCore.QAbstractTableModel):
    def __init__(self, database, parent=None):
        QtCore.QAbstractTableModel.__init__(self, parent)
        self.database = database
        self.header = ['Recipient Name', 'Sent Amount']

    def flags(self, index):

        return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable

    def headerData(self, column, orientation, role):

        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self.header[column]

    def rowCount(self, parent):

        return len(self.database.payments)

    def columnCount(self, parent):

        return len(self.header)

    def data(self, index, role):

        if not index.isValid():
            return

        row = index.row()
        column = index.column()

        if role == QtCore.Qt.DisplayRole:

            payment = self.database.payments[row]
            user_to = self.database.get_user(payment.user_to_id)

            if column == 0:
                return f'{user_to.first_name} {user_to.last_name}'

            if column == 1:
                return payment.amount


class ExpenseReportModel(QtCore.QAbstractTableModel):
    def __init__(self, database, parent=None):
        QtCore.QAbstractTableModel.__init__(self, parent)
        self.database = database
        self.header = ['Expense Name', 'Group', 'Amount', 'User Paid']

    def flags(self, index):

        return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable

    def headerData(self, column, orientation, role):

        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self.header[column]

    def rowCount(self, parent):

        return len(self.database.user_expense_report)

    def columnCount(self, parent):

        return len(self.header)

    def data(self, index, role):

        if not index.isValid():
            return

        row = index.row()
        column = index.column()

        if role == QtCore.Qt.DisplayRole:

            user_expense = self.database.user_expense_report[row]
            expense = self.database.get_expense(user_expense.expense_id)
            group = self.database.get_group(user_expense.group_id)

            if column == 0:
                return expense.name

            if column == 1:
                return group.name

            if column == 2:
                return expense.amount

            if column == 3:
                return user_expense.amount


# Application
class AlignDelegate(QtWidgets.QItemDelegate):
    def paint(self, painter, option, index):
        option.displayAlignment = QtCore.Qt.AlignCenter
        QtWidgets.QItemDelegate.paint(self, painter, option, index)


class SplitSmart(QtWidgets.QMainWindow, ui_main.Ui_SplitSmart):
    def __init__(self):
        super(SplitSmart, self).__init__()
        self.setupUi(self)

        self.sql_file_path = f'{root}/database/data.db'
        self.init_database()
        self.database = Database.get_instance(self.sql_file_path)

        # Data Models
        self.model_groups = None
        self.list_model_users = None
        self.combobox_model_users = None
        self.model_group_users = None
        self.model_user_expense = None
        self.model_user_balance = None
        self.model_payment = None
        self.model_user_expense_report = None

        self.init_ui()

        # UI commands
        # Users
        self.btnSignUp.clicked.connect(self.sign_up_user)
        # Groups
        self.btnCreateGroup.clicked.connect(self.create_group)
        self.comGroups.currentIndexChanged.connect(self.populate_group_users)
        self.btnRemoveUsersFromGroup.clicked.connect(self.remove_users_from_group)
        self.btnAddUsersToGroup.clicked.connect(self.add_users_to_group)
        # Expenses
        self.comGroupsFoExpense.currentIndexChanged.connect(self.populate_user_expenses)
        self.btnCreateExpense.clicked.connect(self.create_expense)
        # Balance Tracking
        self.comUsersBalance.currentIndexChanged.connect(self.populate_user_balance)
        # Payment
        self.btnSubmitPayment.clicked.connect(self.add_payment)
        # Reports
        self.comUsersReport.currentIndexChanged.connect(self.populate_report)

    # Init
    def create_database(self, sql_file_path):
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

        cursor.execute('''CREATE TABLE "group_user" (
                        id integer primary key autoincrement,
                        user_id integer,
                        group_id integer,
                        description text,
                        FOREIGN KEY(user_id) REFERENCES "user"(id),
                        FOREIGN KEY(group_id) REFERENCES "group"(id)
                        )''')

        cursor.execute('''CREATE TABLE "expense" (
                        id integer primary key autoincrement,
                        name text,
                        amount real,
                        date text,
                        description text
                        )''')

        cursor.execute('''CREATE TABLE "user_expense" (
                        id integer primary key autoincrement,
                        expense_id integer,
                        user_id integer,
                        group_id integer,
                        amount real,
                        description text,
                        FOREIGN KEY(expense_id) REFERENCES "expense"(id),
                        FOREIGN KEY(user_id) REFERENCES "user"(id),
                        FOREIGN KEY(group_id) REFERENCES "group"(id)
                        )''')

        cursor.execute('''CREATE TABLE "payment" (
                        id integer primary key autoincrement,
                        user_from_id integer,
                        group_to_id integer,
                        amount real,
                        date text,
                        description text,
                        FOREIGN KEY(user_from_id) REFERENCES "user"(id),
                        FOREIGN KEY(group_to_id) REFERENCES "user"(id)
                        )''')

        connection.commit()
        connection.close()

    def populate_database(self, sql_file_path):

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
                 'email': 'basko@umich.edu',
                 'password': 'love',
                 'description': ''},

                {'id': 3,
                 'first_name': 'Rodriges',
                 'last_name': 'Bender',
                 'email': 'bender@umich.edu',
                 'password': 'futurama',
                 'description': ''}],

            'groups': [
                {'id': 1,
                 'name': 'Trip to Japan',
                 'description': ''},

                {'id': 2,
                 'name': 'Graduation Party',
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

    def init_database(self):

        if not os.path.exists(self.sql_file_path):
            self.create_database(self.sql_file_path)
            self.populate_database(self.sql_file_path)

    def setup_table(self, table):

        table.verticalHeader().hide()
        table.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        table.horizontalHeader().setStretchLastSection(True)
        table.setItemDelegate(AlignDelegate())

    def init_ui(self):

        # Setup tables look and feel
        self.setup_table(self.tabExpenses)
        self.setup_table(self.tabBalace)
        self.setup_table(self.tabReportBalance)
        self.setup_table(self.tabReportExpenses)
        self.setup_table(self.tabReportPayments)

        # Groups data
        self.model_groups = ComboboxModel(self.database, 'groups')

        # Users data
        self.combobox_model_users = ComboboxModel(self.database, 'users')

        self.populate_group_users()
        self.populate_user_expenses()
        self.populate_user_balance()
        self.populate_payment()
        self.populate_report()

    def populate_group_users(self):
        """
        Show groups and group users in UI
        """

        # Load data to UI from DB
        self.comGroups.setModel(self.model_groups)

        # Get Data from UI
        model = self.comGroups.model().index(self.comGroups.currentIndex(), 0)
        group = model.data(QtCore.Qt.UserRole + 1)

        self.list_model_users = ListModel(self.database, 'users')
        self.model_group_users = ListModel(self.database, 'group_users', group.id)

        self.lisGroupUsers.setModel(self.model_group_users)
        self.lisUsers.setModel(self.list_model_users)

    def populate_user_expenses(self):
        """
        Show in UI how much each user paid for all expenses of current group
        """

        # Load data from DB
        self.comGroupsFoExpense.setModel(self.model_groups)

        # Get group from UI
        model = self.comGroupsFoExpense.model().index(self.comGroupsFoExpense.currentIndex(), 0)
        group = model.data(QtCore.Qt.UserRole + 1)

        self.database.get_user_expenses(group.id)
        self.model_user_expense = UserExpenseModel(self.database)
        self.tabExpenses.setModel(self.model_user_expense)

    def populate_user_balance(self):
        """
        Calculate how much current user (selected in UI) owes to all other users
        assuming all users should spent equal amount.
        """

        # Get data from DB
        self.comUsersBalance.setModel(self.combobox_model_users)

        # Get user from UI
        model = self.comUsersBalance.model().index(self.comUsersBalance.currentIndex(), 0)
        user = model.data(QtCore.Qt.UserRole + 1)

        self.database.get_user_balance(user.id)
        self.model_user_balance = UserBalanceModel(self.database)
        self.tabBalace.setModel(self.model_user_balance)

    def populate_payment(self):
        """
        Show payment data in UI
        """

        self.comUserPayTo.setModel(self.combobox_model_users)
        self.comUserPayFrom.setModel(self.combobox_model_users)

    def populate_report(self):
        """
        Show payment data in UI
        """

        # Load data from DB
        self.comUsersReport.setModel(self.combobox_model_users)

        # Get user from UI
        model = self.comUsersReport.model().index(self.comUsersReport.currentIndex(), 0)
        user = model.data(QtCore.Qt.UserRole + 1)

        # Provide Balance report
        self.database.get_user_balance(user.id)
        self.model_user_balance = UserBalanceModel(self.database)
        self.tabReportBalance.setModel(self.model_user_balance)

        # Provide payment reports
        self.database.get_user_payments(user.id)
        self.model_payment = PaymentModel(self.database)
        self.tabReportPayments.setModel(self.model_payment)

        # Provide Expense reports
        self.database.get_user_expenses_report(user.id)
        self.model_user_expense_report = ExpenseReportModel(self.database)
        self.tabReportExpenses.setModel(self.model_user_expense_report)

    # Users
    def sign_up_user(self):

        # Get data
        user_first_name = self.linSignupName.text()
        user_last_name = self.linSignupLastName.text()
        user_email = self.linSignupEmail.text()
        user_password = self.linSignupPassword.text()
        user_tuple = [None, user_first_name, user_last_name, user_email, user_password, '']

        # Update database
        self.database.add_user(user_tuple)

        # Clean UI
        self.linSignupName.clear()
        self.linSignupLastName.clear()
        self.linSignupEmail.clear()
        self.linSignupPassword.clear()

    # Groups
    def create_group(self):

        group_name = self.linGroupName.text()
        group_tuple = [None, group_name, '']

        self.model_groups.layoutAboutToBeChanged.emit()
        self.database.add_group(group_tuple)
        self.model_groups.layoutChanged.emit()

        self.linGroupName.clear()

    def add_users_to_group(self):

        self.model_group_users.layoutAboutToBeChanged.emit()

        # Get data from UI
        users = []
        model_indexes = self.lisUsers.selectedIndexes()
        model = self.comGroups.model().index(self.comGroups.currentIndex(), 0)
        group = model.data(QtCore.Qt.UserRole + 1)

        for model_index in model_indexes:
            obj = model_index.data(QtCore.Qt.UserRole + 1)
            users.append(obj)

        # Update database
        for user in users:
            self.database.add_user_to_group(user.id, group.id)

        self.model_group_users.layoutChanged.emit()

    def remove_users_from_group(self):

        self.model_group_users.layoutAboutToBeChanged.emit()

        # Get data from UI
        users = []
        model_indexes = self.lisGroupUsers.selectedIndexes()
        model = self.comGroups.model().index(self.comGroups.currentIndex(), 0)
        group = model.data(QtCore.Qt.UserRole + 1)

        for model_index in model_indexes:
            obj = model_index.data(QtCore.Qt.UserRole + 1)
            users.append(obj)

        # Update database
        for user in users:
            self.database.remove_user_from_group(user.id, group.id)

        self.model_group_users.layoutChanged.emit()

    # Expenses
    def create_expense(self):
        """
        Register new expense entity in the database
        """

        # Get data
        expense_name = self.linExpenceName.text()
        expense_amount = self.linExpenceAmount.text()
        date = time.strftime('20%y_%m_%d_%H_%M', time.localtime(time.time()))

        model = self.comGroupsFoExpense.model().index(self.comGroupsFoExpense.currentIndex(), 0)
        group = model.data(QtCore.Qt.UserRole + 1)

        # Check, if group is empty, do not create expense
        group_users = self.database.get_group_users(group.id)
        if not group_users:
            print(f'>> Add users to group before adding expenses!')
            return

        expense_tuple = [None, expense_name, expense_amount, date, '']

        # Update Database
        self.model_user_expense.layoutAboutToBeChanged.emit()
        self.database.add_expense(expense_tuple, group.id)
        self.model_user_expense.layoutChanged.emit()

        # Sent notification about expense creation
        # self.user_notification(group_users, expense_name, expense_amount, group.name)

        # Cleanup UI
        self.linExpenceName.clear()
        self.linExpenceAmount.clear()

    # Payment
    def add_payment(self):
        """
        Register payment in the database
        """

        # Get UI data
        payment_amount = float(self.linPayAmount.text())
        date = time.strftime('20%y_%m_%d_%H_%M', time.localtime(time.time()))

        model_from = self.comUserPayFrom.model().index(self.comUserPayFrom.currentIndex(), 0)
        model_to = self.comUserPayTo.model().index(self.comUserPayTo.currentIndex(), 0)
        user_from = model_from.data(QtCore.Qt.UserRole + 1)
        user_to = model_to.data(QtCore.Qt.UserRole + 1)

        # Submit data
        description = f'{user_from.first_name} >> {user_to.first_name}'
        payment_tuple = [None, user_from.id, user_to.id, payment_amount, date, description]
        self.database.add_payment(payment_tuple)

        print(f'Payment ${payment_amount} From {user_from.first_name} To {user_to.first_name} submitted!')

    # General
    def user_notification(self, group_users, expense_name, expense_amount, group_name):

        print(f'>> Sending expense notification...')

        # Authenticate
        login = "random.t4@outlook.com"
        password = 'starrs1234'
        session = smtplib.SMTP('smtp-mail.outlook.com', 587)
        session.starttls()
        session.login(login, password)

        # Send email to each user
        for user in group_users:

            print(f'>> User = {user.first_name} {user.last_name}')

            subject = 'SplitSmart: new expense created'
            text = f'Hello {user.first_name} {user.last_name},\n\n' \
                   f'The expense "{expense_name}" for ${expense_amount} was created within group "{group_name}".\n\n' \
                   f'Have a wonderful payment!\nSpitSmart team :)'
            message = f'Subject: {subject}\n\n{text}'

            session.sendmail(login, user.email, message)

        session.quit()

        print(f'>> Notification sent to all group users!')


if __name__ == "__main__":

    root = os.path.dirname(os.path.abspath(__file__))
    app = QtWidgets.QApplication([])
    split_smart = SplitSmart()
    split_smart.setWindowIcon(QtGui.QIcon('{0}/icons/split_smart.ico'.format(root)))
    split_smart.show()
    app.exec_()

'''
    @anfreire

    linktr.ee/anfreire
'''

from Sources.imports import *
from Auxiliary.Functions import *
from Sources.init_config import get_font

'''
    This module contains the dialog that will appear when the user wants to add a user to the database in the Data Base setup.
'''

class AddUser(QDialog):
    '''
    Dialog to add a user to the database in the Data Base setup.
    It has 3 parameters: usrs, passwrds and flag.
    The usrs is the list of usernames in the database.
    The passwrds is the list of passwords in the database.
    The flag is the flag that will be used to verify if the user was added, and it will be used as a return value.
    If at least one user was added, it will set the flag to True.
    Its important to note that the flag must be initialized as False.
    The new users, new passwords and flag are acesseble through the method get_values().
    This class will also check if the username is already in the database, and if it is, it will display a message box.
    This class will also check if the username or password are empty, and if they are, it will display a message box.
    This class appends the new users and passwords to the lists passed as parameters trhought the method try_add_user().
    '''
    def __init__(self, usrs: list, passwrds: list, flag: bool, parent=None) -> None:
        super().__init__(parent)
        '''
        Constructor of the Add User Dialog Layout.
        Executes the dialog in the last line.
        '''
        self.setWindowTitle("Add User")
        self.usrs = usrs
        self.setModal(True)
        self.passwrds = passwrds
        self.flag = flag
        self.username_input = QLineEdit()
        self.password_input = QLineEdit()
        username_label = QLabel("Username:")
        password_label = QLabel("Password:")
        self.username_input.setPlaceholderText("Enter username here")
        self.password_input.setPlaceholderText("Enter password here")
        self.password_input.setMinimumWidth(300)
        self.username_input.setMinimumWidth(300)
        layout = QFormLayout()
        layout.addRow(username_label, self.username_input)
        layout.addRow(password_label, self.password_input)
        add_button = QPushButton("Add")
        cancel_button = QPushButton("Cancel")
        add_button.clicked.connect(self.try_add_usr)
        cancel_button.clicked.connect(self.reject)
        layout.addRow(add_button, cancel_button)
        font = self.username_input.font()
        font.setPointSize(font.pointSize() + 4)
        self.username_input.setFont(get_font())
        self.password_input.setFont(get_font())
        username_label.setFont(get_font())
        password_label.setFont(get_font())
        add_button.setFont(get_font())
        cancel_button.setFont(get_font())
        layout.setVerticalSpacing(20)
        layout.setContentsMargins(40,40,40,40)
        self.setLayout(layout)
        self.exec()

    def check_user_exists(self, username: str) -> bool:
        '''
        This method checks if the username is already in the list of usernames.
        '''
        for user in self.usrs:
            if user == username:
                return True
            return False

    def try_add_usr(self) -> None:
        '''
        This method tries to add the user to the database.
        It will check if the username is already in the database, if it is, it will display a message box.
        If one user was added, it will set the flag to True.
        '''
        username = self.username_input.text()
        password = self.password_input.text()
        if self.check_user_exists(username):
            show_dialog(self, "Error", "User already registred!", get_font())
            return
        elif username == None or username == '' or username.isspace() or username == 'username':
            show_dialog(self, "Error", "Invalid username!", get_font())
            return
        elif password == None or password.isspace() or password == '' or password == 'password':
            show_dialog(self, "Error", "Invalid password!", get_font())
            return
        else:
            self.usrs.append(username)
            self.passwrds.append(password)  
            self.username_input.setText('')
            self.password_input.setText('')
            self.hide()
            self.flag = True

    def get_values(self) -> tuple:
        '''
        This method returns the new users, new passwords and flag, as explained in the class description.
        '''
        return self.usrs, self.passwrds, self.flag
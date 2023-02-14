'''
    @anfreire

    linktr.ee/anfreire
'''

from Sources.imports import *
from Auxiliary.Functions import *
from Auxiliary.Classes import Events
from Sources.init_config import get_font

'''
    This module contains the code for the Login page.
'''

class Login(Events):
    '''
    This class is the login window.
    '''
    def __init__(self, parent=None) -> None:
        '''
        This method initializes the parent class and the login window widgets.
        '''
        super().__init__(parent)
        self.show_password = False
        self.start_widgets_login()

    def start_widgets_login(self) -> None:
        '''
        This method sets the widgets of the login window.
        It should be called only once, at the __init__ method.
        '''
        self.ui.input_password_login.setEchoMode(QLineEdit.Password)
        self.ui.input_password_login.setPlaceholderText("Password")
        self.ui.input_user_login.setPlaceholderText("Enter your username")
        self.ui.input_password_login.setPlaceholderText("Enter your password")
        self.ui.input_user_login.setToolTip("Enter the username you used to register")
        self.ui.input_password_login.setToolTip("Enter the password you used to register")
        self.ui.input_user_login.returnPressed.connect(self.ui.button_proceed_login.click)
        self.ui.input_password_login.returnPressed.connect(self.ui.button_proceed_login.click)

    def setup_login(self) -> None:
        '''
        This method sets the login window signals and slots.
        '''
        self.flags.login = True
        self.set_default_close_event()
        self.ui.button_return_login.hide()
        disconnect_button(self.ui.button_proceed_login).connect(lambda:self.authenticate())
        disconnect_button(self.ui.button_recover_login).connect(lambda:self.forgot_password_login())
        disconnect_button(self.ui.button_password_login).connect(lambda:self.see_password_click())

    def empty_login(self) -> None:
        '''
        This method empties the login window widgets.
        '''
        self.ui.input_user_login.setText('')
        self.ui.input_password_login.setText('')

    def forgot_password_login(self) -> None:
        '''
        This method goes to the forgot confirm email window.
        Starts the recovery process and sets the recover flag to True.
        '''
        self.flags.recover = True
        self.empty_confirm_email()
        self.setup_confirm_email()
        self.go_confirm_email()

    def go_login(self) -> None:
        '''
        This method sets the login window as the current widget.
        '''
        self.ui.stackedWidget.setCurrentWidget(self.ui.Login)
        self.turn_off_actions_menu()

    def see_password_click(self) -> None:
        '''
        This method shows or hides the password.
        '''
        if self.show_password == False:
            self.ui.input_password_login.setEchoMode(QLineEdit.Normal)
            self.show_password = True
        else:
            self.ui.input_password_login.setEchoMode(QLineEdit.Password)
            self.show_password = False

    def authenticate(self) -> None:
        '''
        This method authenticates the user.
        It checks if the username and password are correct, and if they are, proceeds to the method proceed_database.
        '''
        username = self.ui.input_user_login.text()
        password = self.ui.input_password_login.text()
        try:
            self.data.update_values(retrieve_from_db())
        except sqlite3.OperationalError:
            show_dialog(self, "Error", "No database file found! Please register first!\nPlease reset the database!", get_font())
            return
        for usr, pswrd in zip(self.data.users, self.data.passwrds):
            if username == usr and password == pswrd:
                self.proceed_database()
                return
        show_dialog(self, "Error", "Wrong username or password!", get_font())
        
    def proceed_database(self) -> None:
        '''
        This method checks if the database is encrypted or not, so it can procced to the tables window.
        '''
        if self.data.config == 'T':
            try:
                decrypt_database(self.data)
            except:
                pass
        self.open_database()
        self.go_tables()
        self.turn_on_actions_menu()
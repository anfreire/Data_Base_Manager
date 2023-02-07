from imports import *
from Sources.Classes import *
from Sources.Functions import *
from init_config import costum_font

class Login(Widget):
    '''
    This class is the login window.
    '''
    def __init__(self, parent=None) -> None:
        '''
        This method initializes the login window.
        '''
        super().__init__(parent)
        self.show_password = False
        self.start_widgets_login()

    def start_widgets_login(self) -> None:
        '''
        This method sets the widgets of the login window.
        It should be called only once, at the __init__ method.
        '''
        self.ui.password_input_login.setEchoMode(QLineEdit.Password)
        self.ui.password_input_login.setPlaceholderText("Password")
        self.ui.username_input_login.setPlaceholderText("Username")

    def setup_login(self) -> None:
        '''
        This method sets the login window signals and slots.
        '''
        self.flags.login = True
        self.set_default_close_event()
        disconnect_button(self.ui.authenticate_button_login)
        self.ui.authenticate_button_login.clicked.connect(lambda:self.authenticate())
        disconnect_button(self.ui.forgot_password_button_login)
        self.ui.forgot_password_button_login.clicked.connect(lambda:self.forgot_password_login())
        disconnect_button(self.ui.see_password_button)
        self.ui.see_password_button.clicked.connect(lambda:self.see_password_click())

    def empty_login(self) -> None:
        '''
        This method empties the login window widgets.
        '''
        self.ui.username_input_login.setText('')
        self.ui.password_input_login.setText('')

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
        self.ui.stackedWidget.setCurrentWidget(self.ui.login)

    def see_password_click(self) -> None:
        '''
        This method shows or hides the password.
        '''
        if self.show_password == False:
            self.ui.password_input_login.setEchoMode(QLineEdit.Normal)
            self.show_password = True
        else:
            self.ui.password_input_login.setEchoMode(QLineEdit.Password)
            self.show_password = False

    def authenticate(self) -> None:
        '''
        This method authenticates the user.
        It checks if the username and password are correct, and if they are, proceeds to the method proceed_database.
        '''
        username = self.ui.username_input_login.text()
        password = self.ui.password_input_login.text()
        try:
            self.data.update_values(retrieve_from_db())
        except sqlite3.OperationalError:
            dialog = QMessageBox()
            dialog.setFont(costum_font)
            dialog.critical(self, "Error", "No database file found! Please register first!\nPlease reset the database!", QMessageBox.Ok)
            return
        for usr, pswrd in zip(self.data.users, self.data.passwrds):
            if username == usr and password == pswrd:
                self.proceed_database()
                return
        dialog = QMessageBox()
        dialog.setFont(costum_font)
        dialog.critical(self, "Error", "Wrong username or password!", QMessageBox.Ok)
        
    def proceed_database(self) -> None:
        '''
        This method checks if the database is encrypted or not, so it can procced to the program home.
        '''
        if self.data.config == 'T':
            try:
                decrypt_database(self.data)
            except:
                pass
        self.go_home()
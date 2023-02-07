from imports import *
from Sources.Classes import *
from Widgets.Dialogs import *
from Sources.Functions import *
from init_config import costum_font

class Confirm_Email(Widget):
    '''
    This class is used to confirm the email when the user is recovering the database.
    '''
    def __init__(self, parent=None) -> None:
        '''
        This method initializes parent class.
        '''
        super().__init__(parent)

    def setup_confirm_email(self) -> None:
        '''
        This method sets up the confirm email signals and slots.
        Sets the middle recovery close event, that unable the user to close the window, to prevent unexpected behavior.
        '''
        self.set_middle_recovery_close_event()
        disconnect_button(self.ui.reset_db_button_confirm_email)
        self.ui.reset_db_button_confirm_email.clicked.connect(lambda:self.restart_config())
        disconnect_button(self.ui.confirm_email_button)
        self.ui.confirm_email_button.clicked.connect(lambda:self.recover_events_1())
        disconnect_button(self.ui.return_button_confirm_email)
        self.ui.return_button_confirm_email.clicked.connect(lambda:self.return_login_from_confirm_email())
        self.ui.label_4.setText("Data Base\nRecovery")
        self.ui.confirm_email_button.setText("Recover the DataBase")

    def empty_confirm_email(self) -> None:
        '''
        This method empties the confirm email widget.
        '''
        self.ui.input_email_confirm.setText('')

    def go_confirm_email(self) -> None:
        '''
        This method sets the Confirm Email as the current page.
        '''
        self.ui.stackedWidget.setCurrentWidget(self.ui.reset)

    def return_login_from_confirm_email(self) -> None:
        '''
        This method returns to the login widget.
        Its assigned to the return button.
        '''
        self.setup_login()
        self.go_login()

    def recover_events_1(self) -> None:
        '''
        This method checks the email the user has entered.
        If the email is correct, it sends the email to the user, with the code generated.
        Changes the button signal to the verify code, on the method recover_events_2().
        '''
        try:
            self.data.update_values(retrieve_from_db())
        except sqlite3.OperationalError:
            dialog = QMessageBox()
            dialog.setFont(costum_font)
            dialog.critical(None, "Error", "The data to login was not found!\nPlease reset the program.", QMessageBox.Ok)
            return
        receiver_email = self.ui.input_email_confirm.text()
        if receiver_email != self.data.email:
            dialog = QMessageBox()
            dialog.setFont(costum_font)
            dialog.critical(None, "Error", "Email does not match the one registered!", QMessageBox.Ok)
            return
        elif receiver_email == self.data.email:
            send_email(self.data, "tmpmailanfreire@gmail.com", "cfmywsuyfnvirxaq")
            self.recover_events_2()

    def recover_events_2(self) -> None:
        '''
        This method its called as soon as the emails is sent, so the code can be verified.
        This method verifies the code.
        For that, the only button that can be pressed in this window, its disconnected, and if pressed, opens the dialog to verify the code.
        Without the need the press of a button when this method its called, the costum dialod CodeVerify is called and is open to verify the code.
        If the code is verified, the method recovery_done_events() its executed.
        If the user, clicks the Recovery button, as previously said, the costum dialog CodeVerify is called and is open to verify the code.
        '''
        disconnect_button(self.ui.confirm_email_button)
        self.ui.confirm_email_button.clicked.connect(lambda:self.recover_events_2())
        dialog = CodeVerify(self.data.code, False)
        verification = dialog.get_flag()
        if verification == True:
            self.recovery_done_events()
        
    def recovery_done_events(self) -> None:
        '''
        This method is called when the code is verified.
        This method shows a message to the user, giving instructions on what to do next.
        Clears the input email and proceeds to the config widget.
        '''
        dialog = QMessageBox()
        dialog.setFont(costum_font)
        dialog.information(None, "Success", "User authenticated!\nYou can now set the new login credentials, change the email or go with the same one, but you will need to confirm it again.", QMessageBox.Ok)
        self.setup_config()
        self.go_config()
        self.empty_confirm_email()
            
    def restart_config(self) -> None:
        '''
        This method resets the program, if the user wants to.
        Deletes the .bin folder, that contains the database, the users and the email.
         ͡° ͜ʖ ͡°
        '''
        restart_question = QMessageBox.question(self, 'Restart', "Do you want to restart the program?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if restart_question == QMessageBox.Yes:
            restart_question_2 = QMessageBox.question(self, 'WARNING', "ALL DATA WILL BE ERASED!\nUsers, Email and the Database!\nAre you sure?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if restart_question_2 == QMessageBox.Yes:
                directory = '.bin'
                if os.path.exists(directory):
                    shutil.rmtree(directory)
                self.empty_login()
                self.empty_config()
                self.empty_confirm_email()
                self.empty_start()
                self.flags.reset()
                self.data.reset()
                self.flags.recover = False
                self.go_start()
                return
            return
        return
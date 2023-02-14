'''
    @anfreire

    linktr.ee/anfreire
'''

from Sources.imports import *
from Auxiliary.Functions import *
from Auxiliary.Classes import Events
from Sources.init_config import get_font
from Widgets.CodeVerify import CodeVerify

'''
    This module contains the code for the Confirm Email page.
'''

class ConfirmEmail(Events):
    '''
    This class is used to confirm the email when the user is recovering the database.
    '''
    def __init__(self, parent=None) -> None:
        '''
        This method initializes parent class and starts the widgets.
        '''
        super().__init__(parent)
        self.start_widgets_confirm_email()
        
    def start_widgets_confirm_email(self) -> None:
        '''
        This method sets the widgets of the Confirm Email widget.
        It should be called only once, at the __init__ method.
        '''
        self.ui.input_email_confirm_email.setToolTip("Enter the email you used to register the database.")
        self.ui.input_email_confirm_email.setPlaceholderText("Email used to register the database")

    def setup_confirm_email(self) -> None:
        '''
        This method sets up the confirm email signals and slots and widgets.
        '''
        disconnect_button(self.ui.button_reset_confirm_email).connect(lambda:self.restart_config())
        disconnect_button(self.ui.button_proceed_confirm_email).connect(lambda:self.recover_events_1())
        disconnect_button(self.ui.button_return_confirm_email).connect(lambda:self.return_login_from_confirm_email())

    def empty_confirm_email(self) -> None:
        '''
        This method empties the confirm email widget.
        '''
        self.ui.input_email_confirm_email.setText('')

    def go_confirm_email(self) -> None:
        '''
        This method sets the Confirm Email as the current page.
        '''
        self.ui.stackedWidget.setCurrentWidget(self.ui.Confirm_Email)
        self.turn_off_actions_menu()

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
            show_dialog(self, "Error", "The database was not found!\nPlease reset the program.", get_font())
            return
        receiver_email = self.ui.input_email_confirm_email.text()
        if receiver_email != self.data.email:
            show_dialog(self, "Error", "Email does not match the one registered!", get_font())
            return
        elif receiver_email == self.data.email:
            try:
                send_email(self.data, "YOUR_EMAIL_HERE", "YOUR_PASSWORD_HERE")
            except Exception as e:
                show_dialog(self, "Error", f"An error has occurred while sending the email!\nPlease try again later.\nInfo: {e}", get_font())
                return
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
        disconnect_button(self.ui.button_proceed_confirm_email).connect(lambda:self.recover_events_2())
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
        show_dialog(self, "info", "Code verified!\nYou can now set the new login credentials, change the email or go with the same one, but you will need to confirm it again.", get_font())
        self.setup_config()
        self.go_config()
        self.empty_confirm_email()
            
    def restart_config(self) -> None:
        '''
        This method resets the program, if the user wants to.
        Deletes the .bin folder, that contains the database, the users and the email.
        '''
        restart_question = show_question(self,  "question", "Do you want to restart the program?", get_font())
        if restart_question == True:
            restart_question_2 = show_question(self,  "warning", "ALL DATA WILL BE ERASED!\nUsers, Email and the Database!\nAre you sure?", get_font())
            if restart_question_2 == True:
                directory = '.bin'
                if os.path.exists(directory):
                    shutil.rmtree(directory)
                directory = ".backups"
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

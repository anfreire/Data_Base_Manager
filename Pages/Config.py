from imports import *
from Sources.Classes import *
from Widgets.Dialogs import *
from Sources.Functions import *
from init_config import costum_font

class Config(Widget):
    '''
    This class contains the methods that are used in the configuration page.
    Connects the signals and slots of the configuration page for the setup and for the recovery.
    '''
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        '''
        This method initializes the configuration page widgets.
        This method should only be called once, that is, when the application is started.
        '''
        self.start_widgets_config()

    def start_widgets_config(self) -> None:
        '''
        This method sets the widgets of the configuration page.
        It should only be called once, as it is called in the __init__ method.
        '''
        self.header = QListWidgetItem("Users")
        self.header.setFont(costum_font)
        self.header.setTextAlignment(Qt.AlignCenter)
        self.ui.listWidget.addItem(self.header)
        self.ui.email_input_config.setToolTip("This is your email to recover your password.")
        self.ui.email_input_config.setPlaceholderText("Email to recover the acess")

    def setup_config(self) -> None:
        '''
        This method setups the configuration page signals, layout and slots for the setup and for the recovery.
        The setup will depend on the flags.create_db and flags.recover.
        '''
        disconnect_button(self.ui.browse_db_file_button) 
        self.ui.browse_db_file_button.clicked.connect(lambda:self.browse_db_file())
        disconnect_button(self.ui.proceed_button_config)
        self.ui.proceed_button_config.clicked.connect(lambda:self.proceed_event_1())
        disconnect_button(self.ui.add_user_button)
        self.ui.add_user_button.clicked.connect(lambda:self.update_user_lists())
        self.setup_config_layout()
        if self.flags.recover == False:
            self.setup_config_register()
        elif self.flags.recover == True:
            self.setup_config_recover()
        
    def setup_config_layout(self) -> None:
        '''
        This method setups the configuration page layout, when the user is registring and recovering.
        Its called by setup_config().
        Mainly, it removes the widgets that are associed with adding a database file.
        Depends on the flags.create_db and flags.recover .
        '''
        if self.flags.create_db == False and self.flags.recover == False:
            if self.ui.horizontalLayout_4.indexOf(self.ui.verticalLayout_6) == -1:
                self.ui.horizontalLayout_4.addItem(self.ui.verticalLayout_6)
                self.ui.verticalLayout_6.setContentsMargins(50, -1, -1, -1)
            if self.ui.verticalLayout_6.indexOf(self.ui.password_label_2) == -1:
                self.ui.verticalLayout_6.addWidget(self.ui.password_label_2, 0, Qt.AlignHCenter|Qt.AlignBottom)
                self.ui.password_label_2.show()
            if self.ui.verticalLayout_6.indexOf(self.ui.browse_db_file_button) == -1:
                self.ui.verticalLayout_6.addWidget(self.ui.browse_db_file_button, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
                self.ui.browse_db_file_button.show()
        elif self.flags.create_db == True or self.flags.recover == True:
            if self.ui.verticalLayout_6.indexOf(self.ui.password_label_2) != -1:
                self.ui.verticalLayout_6.removeWidget(self.ui.password_label_2)
                self.ui.password_label_2.hide()
            if self.ui.verticalLayout_6.indexOf(self.ui.browse_db_file_button) != -1:
                self.ui.verticalLayout_6.removeWidget(self.ui.browse_db_file_button)
            if self.ui.horizontalLayout_4.indexOf(self.ui.verticalLayout_6) != -1:
                self.ui.horizontalLayout_4.removeItem(self.ui.verticalLayout_6)
                self.ui.browse_db_file_button.hide()

    def setup_config_register(self) -> None:
        '''
        This method setups the configuration page signals and slots, when the user is registering.
        Its called by setup_config(), when the flag.recover is False.
        Sets the close event to the middle of the configuration process, that deletes the data with the user's logging information.
        '''
        self.set_middle_config_close_event()
        disconnect_button(self.ui.return_button_config)
        self.ui.return_button_config.clicked.connect(lambda:self.return_start_from_config())
        
    def setup_config_recover(self) -> None:
        '''
        This method setups the configuration page signals and slots, when the user is recovering.
        Its called by setup_config(), when the flag.recover is True.
        Removes the old logging data, to save the new one.
        '''
        self.delete_data()
        self.set_middle_recovery_close_event()
        self.ui.return_button_config.clicked.connect(lambda:self.show_warning())
        
    def show_warning(self) -> None:
        '''
        This method shows a warning message, when the user tries to return to in the middle of the recovery process.
        '''
        dialog = QMessageBox()
        dialog.setFont(costum_font)
        dialog.warning(self, "Warning", "There is no logging data and you need to end the recovery process. If you close the window, you will lose the data.", QMessageBox.Ok)
        
    def empty_config(self) -> None:
        '''
        This method empties the configuration page widgets.
        '''
        self.ui.email_input_config.setText('')
        while self.ui.listWidget.count() > 1:
            self.ui.listWidget.takeItem(1)
            
    def go_config(self) -> None:
        '''
        This method sets the configuration page as the current page.
        '''
        self.ui.stackedWidget.setCurrentWidget(self.ui.config)

    def return_start_from_config(self) -> None:
        '''
        This method returns to the start page from the configuration page.
        It is used when the user clicks on the return button, when the user is registering.
        '''
        self.go_start()

    def browse_db_file(self) -> None:
        '''
        This method opens a file dialog to select a database file.
        If the user selects a file, it checks if it is a .db file.
        If it is, it copies it to the .bin folder, with the name src.db, and updates the loggin data setting the flag.db_file_added to True.
        '''
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        fileName, _ = QFileDialog.getOpenFileName(self,"Open DB File", "","DB Files (*.db);;All Files (*)", options=options)
        if fileName:
            # check if file is a .db file
            if fileName.endswith('.db'):
                bin_dir = '.bin'
                create_folder(bin_dir)
                bin_file = os.path.join(bin_dir, "src.db")
                shutil.copy2(fileName, bin_file)
                self.flags.db_file_added = True
                return
            else:
                dialog = QMessageBox()
                dialog.setFont(costum_font)
                dialog.critical(None, "Error!", "Not a database file! (.db)", QMessageBox.Ok)
        else:
            dialog = QMessageBox()
            dialog.setFont(costum_font)
            dialog.critical(None, "Error!", "No file has been setected!", QMessageBox.Ok)
    
    def delete_data(self) -> None:
        '''
        This method is called when the user is recovering the acess to the database.
        If the user previously selected to encrypt the database, it decrypts the database, because the key will be changed.
        This method deletes the log.db file, to replace it with the new one.
        Sets the default configuration, and the default flags.
        Sets the information to encrypt the database, if the user selected to encrypt it, or not, if the user selected not to encrypt it.
        '''
        if self.data.config == 'T':
            self.flags.encrypt_db = True
            decrypt_database(self.ui.stackedWidget)
        self.data.reset()
        file_path = os.path.join('.bin', 'log.db')
        if os.path.exists(file_path):
            os.remove(file_path)
        if self.flags.encrypt_db == True:
            self.data.config = 'T'
        else:
            self.data.config = 'F'
        self.flags.email_added = False
        self.flags.users_added = False

    def update_user_lists(self) -> None:
        '''
        This method updates the user list, when the user adds a new user.
        Uses the costum dialog AddUser, to get the new user and password.
        More information about the AddUser dialog, in the AddUser class.
        '''
        self.data.users, self.data.passwrds, self.flags.users_added = AddUser(self.data.users, self.data.passwrds, self.flags.users_added).get_values()
        for user in self.data.users:
            if self.ui.listWidget.findItems(user, Qt.MatchExactly):
                continue
            user = QListWidgetItem(user)
            user.setFont(costum_font)
            user.setTextAlignment(Qt.AlignCenter)
            self.ui.listWidget.addItem(user)

    def proceed_event_1(self) -> None:
        '''
        This method checks if the user has added all the required data.
        Checks if the email is valid, if it is, it updates the loggin data and the corresponding flag.
        If the user meets all the requirements, proceeds to the method email_change_handler().
        '''
        if self.flags.users_added == False:
            dialog = QMessageBox()
            dialog.setFont(costum_font)
            dialog.critical(None, "Error!", "No users added!", QMessageBox.Ok)
            return
        elif self.flags.db_file_added == False and self.flags.create_db == False and self.flags.recover == False:
            dialog = QMessageBox()
            dialog.setFont(costum_font)
            dialog.critical(None, "Error!", "No database file added!", QMessageBox.Ok)
            return
        elif is_email_valid(self.ui.email_input_config.text()) == True:
            self.data.email = self.ui.email_input_config.text()
            self.flags.email_added = True
        else:
            dialog = QMessageBox()
            dialog.setFont(costum_font)
            dialog.critical(None, "Error!", "Invalid email!", QMessageBox.Ok)
            return
        if self.flags.email_added == True and self.flags.users_added == True and \
            ((self.flags.db_file_added == True and self.flags.create_db == False and self.flags.recover == False) or \
            (self.flags.db_file_added == False and self.flags.create_db == True and self.flags.recover == False) or \
            (self.flags.db_file_added == False and self.flags.create_db == False and self.flags.recover == True)):
                self.email_change_handler()

    def email_change_handler(self) -> None:
        '''
        This method handles the email change during the registration process or the recovery process.
        Its only a helper method to handle the email change.
        Sends the email to the user, with the code, and proceeds to the method proceed_event_2().
        '''
        self.data.generate_code()
        send_email(self.data, "insert_email_here", "inset_password_here")
        disconnect_button(self.ui.proceed_button_config)
        self.ui.proceed_button_config.clicked.connect(lambda:self.proceed_event_2())  
        self.proceed_event_2()
            
    def proceed_event_2(self) -> None:
        '''
        This method verifies the code, when the user is registering or recovering, with the costum dialod CodeVerify.
        If the code is verified, it saves the data to the database and executes the method configuration_done_events().
        If the email has changed, it disconnects the proceed button and connects it back to the method proceed_event_1().
        '''
        if self.data.email != self.ui.email_input_config.text():
            disconnect_button(self.ui.proceed_button_config)
            self.ui.proceed_button_config.clicked.connect(lambda:self.proceed_event_1())
        tmp_code = CodeVerify(self.data.code, False)
        tmp_verification = tmp_code.get_flag()
        if tmp_verification == True:
            save_to_db(self.data)
            self.configuration_done_events()
            
    def configuration_done_events(self) -> None:
        '''
        This method is called when the code is verified.
        If the user is selected to encrypt the database, it encrypts the database.
        Clears all widgets from all previous windows, and sets the default close event.
        Proceeds to the next window, the login window.
        '''
        self.set_default_close_event()
        if self.data.config == 'T':
            encrypt_database(self.data)
        if self.flags.recover == True:
            self.flags.recover = False
        dialog = QMessageBox()
        dialog.setFont(costum_font)
        dialog.information(None, "Welcome!", "Welcome to the DataBase!\nPlease, remember your password and email to recover your DataBase in the future.", QMessageBox.Ok)
        self.empty_start()
        self.empty_config()
        self.empty_login()
        self.setup_login()
        self.go_login()
 

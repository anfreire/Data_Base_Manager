'''
    @anfreire

    linktr.ee/anfreire
'''

from Sources.imports import *
from Auxiliary.Functions import *
from Widgets.AddUser import AddUser
from Auxiliary.Classes import Events
from Sources.init_config import get_font
from Widgets.CodeVerify import CodeVerify

'''
    This mehod contains the configuration page.
'''

class Config(Events):
    '''
    This class contains the methods that are used in the configuration page.
    Connects the signals and slots of the configuration page for the setup and for the recovery.
    '''
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        '''
        This method initializes the parent class and starts the widgets.
        '''
        self.start_widgets_config()

    def start_widgets_config(self) -> None:
        '''
        This method sets the widgets of the configuration page.
        It should only be called once, as it is called in the __init__ method.
        '''
        self.header = QListWidgetItem("Users")
        font_list = copy.copy(get_font())
        font_list.setPointSize(30)
        self.header.font().setBold(True)
        self.header.setFont(font_list)
        self.header.setTextAlignment(Qt.AlignCenter)
        self.ui.listWidget.addItem(self.header)
        self.ui.input_email_config.setToolTip("This is your email to recover your password.")
        self.ui.input_email_config.setPlaceholderText("Email to recover the acess")
        self.ui.input_email_config.returnPressed.connect(self.ui.button_proceed_config.click)

    def setup_config(self) -> None:
        '''
        This method setups the configuration page signals, layout and slots for the setup and for the recovery.
        The setup will depend on the flags.create_db and flags.recover.
        '''
        disconnect_button(self.ui.button_browse_config).connect(lambda:self.browse_db_file())
        disconnect_button(self.ui.button_proceed_config).connect(lambda:self.proceed_event_1())
        disconnect_button(self.ui.button_add_config).connect(lambda:self.update_user_lists())
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
            if self.ui.horizontalLayout_2.indexOf(self.ui.verticalLayout) == -1:
                self.ui.horizontalLayout_2.addItem(self.ui.verticalLayout)
            if self.ui.verticalLayout.indexOf(self.ui.label_10) == -1:
                self.ui.verticalLayout.addWidget(self.ui.label_10, 0, Qt.AlignHCenter|Qt.AlignBottom)
                self.ui.label_10.show()
            if self.ui.verticalLayout.indexOf(self.ui.button_browse_config) == -1:
                self.ui.verticalLayout.addWidget(self.ui.button_browse_config, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
                self.ui.button_browse_config.show()
        elif self.flags.create_db == True or self.flags.recover == True:
            if self.ui.verticalLayout.indexOf(self.ui.label_10) != -1:
                self.ui.verticalLayout.removeWidget(self.ui.label_10)
                self.ui.label_10.hide()
            if self.ui.verticalLayout.indexOf(self.ui.button_browse_config) != -1:
                self.ui.verticalLayout.removeWidget(self.ui.button_browse_config)
                self.ui.button_browse_config.hide()
            if self.ui.horizontalLayout_2.indexOf(self.ui.verticalLayout) != -1:
                self.ui.horizontalLayout_2.removeItem(self.ui.verticalLayout)

    def setup_config_register(self) -> None:
        '''
        This method setups the configuration page signals and slots, when the user is registering.
        Its called by setup_config(), when the flag.recover is False and flag.create_db is False.
        Sets the close event to the middle of the configuration process, that deletes the data with the user's logging information, more information in the method set_middle_config_close_event().
        '''
        self.set_middle_config_close_event()
        disconnect_button(self.ui.button_return_config).connect(lambda:self.return_start_from_config())
        
    def setup_config_recover(self) -> None:
        '''
        This method setups the configuration page signals and slots, when the user is recovering.
        Its called by setup_config(), when the flag.recover is True.
        Decrypts the database file, if the user chose to encrypt it, because the code to encrypt will change.
        Resets old logging information and sets the flags flags.email_added and flags.users_added to False for the recovery.
        '''
        try:
            if self.data.config == 'T':
                decrypt_database(self.data)
        except:
            pass
        self.flags.email_added = False
        self.flags.users_added = False
        self.data.reset()
        disconnect_button(self.ui.button_return_config).connect(lambda:self.return_confirm_email_from_config())
        
    def empty_config(self) -> None:
        '''
        This method empties the configuration page widgets.
        '''
        self.ui.input_email_config.setText('')
        while self.ui.listWidget.count() > 1:
            self.ui.listWidget.takeItem(1)
            
    def go_config(self) -> None:
        '''
        This method sets the configuration page as the current page.
        '''
        self.ui.stackedWidget.setCurrentWidget(self.ui.Config)
        self.turn_off_actions_menu()

    def return_start_from_config(self) -> None:
        '''
        This method returns to the start page from the configuration page.
        It is used when the user clicks on the return button, when the user is registering.
        '''
        self.go_start()
        
    def return_confirm_email_from_config(self) -> None:
        '''
        This method returns to the confirm email page from the configuration page.
        It is used when the user clicks on the return button, when the user is recovering.
        Empties the configuration page widgets, because an email confirmation will be sent again, to start the recovery process.
        '''
        self.empty_config()
        self.go_confirm_email()

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
                show_dialog(self, "error", "Not a database file! (.db)", get_font())
        else:
            show_dialog(self, "error", "No file has been setected!", get_font())
        
    def replace_data(self, new_users, new_passwrds, new_code, new_email) -> None:
        '''
        This function is used to update the logging information in the recovery process.
        '''
        self.data.update_values(retrieve_from_db())
        conn = sqlite3.connect('.bin/log.db')
        with conn:
            c = conn.cursor()
            c.execute("SELECT users, passwrds, code, email, config, key FROM data")
            result = c.fetchone()
            code = result[2]
            email = result[3]
            config = result[4]
            key = result[5]
        encrypted_users = encrypt(str(new_users).encode(), key)
        encrypted_passwrds = encrypt(str(new_passwrds).encode(), key)
        encrypted_code = encrypt(str(new_code).encode(), key)
        encrypted_email = encrypt(str(new_email).encode(), key)
        conn = sqlite3.connect('.bin/log.db')
        with conn:
            c = conn.cursor()
            c.execute("UPDATE data SET users = ?, passwrds = ?, code = ?, email = ?", (encrypted_users, encrypted_passwrds, encrypted_code, encrypted_email))
            conn.commit()

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
            user.setFont(get_font())
            user.setTextAlignment(Qt.AlignCenter)
            self.ui.listWidget.addItem(user)

    def proceed_event_1(self) -> None:
        '''
        This method checks if the user has added all the required data.
        Checks if the email is valid, if it is, it updates the loggin data and the corresponding flag.
        If the user meets all the requirements, proceeds to the method email_change_handler().
        '''
        if self.flags.users_added == False:
            show_dialog(self, "error", "No users added!", get_font())
            return
        elif self.flags.db_file_added == False and self.flags.create_db == False and self.flags.recover == False:
            show_dialog(self, "error", "No database file added!", get_font())
            return
        elif is_email_valid(self.ui.input_email_config.text()) == True:
            self.data.email = self.ui.input_email_config.text()
            self.flags.email_added = True
        else:
            show_dialog(self, "error", "Invalid email!", get_font())
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
        try:
            send_email(self.data, "YOUR_EMAIL_HERE", "YOUR_PASSWORD_HERE")
        except Exception as e:
            show_dialog(self, "error", f"An error has occurred while sending the email!\nPlease try again later.\nInfo: {e}", get_font())
            return
        disconnect_button(self.ui.button_proceed_config).connect(lambda:self.proceed_event_2())  
        self.proceed_event_2()
            
    def proceed_event_2(self) -> None:
        '''
        This method verifies the code, when the user is registering or recovering, with the costum dialod CodeVerify.
        If the code is verified, it saves the data to the database and executes the method configuration_done_events().
        If the email has changed, it disconnects the proceed button and connects it back to the method proceed_event_1().
        '''
        if self.data.email != self.ui.input_email_config.text():
            disconnect_button(self.ui.button_proceed_config).connect(lambda:self.proceed_event_1())
        tmp_code = CodeVerify(self.data.code, False)
        tmp_verification = tmp_code.get_flag()
        if self.flags.recover == True:
            self.replace_data(self.data.users, self.data.passwrds, self.data.code, self.data.email)
        if tmp_verification == True:
            save_to_db(self.data)
            self.configuration_done_events()
            
    def configuration_done_events(self) -> None:
        '''
        This method is called when the code is verified.
        If the user selected to encrypt the database, it encrypts the database.
        Clears all widgets from all previous windows, and sets the default close event.
        Proceeds to the next window, the login window.
        '''
        self.set_default_close_event()
        if self.data.config == 'T':
            encrypt_database(self.data)
        if self.flags.recover == True:
            
            self.flags.recover = False
        show_dialog(self, "info", "Welcome to the DataBase!\nPlease, remember your password and email to recover your DataBase in the future.", get_font())
        self.empty_start()
        self.empty_config()
        self.empty_login()
        self.setup_login()
        self.go_login()
 

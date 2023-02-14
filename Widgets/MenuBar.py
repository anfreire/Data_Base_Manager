'''
    @anfreire

    linktr.ee/anfreire
'''

from Sources.imports import *
from Auxiliary.Functions import *
from Auxiliary.Classes import Events
from Widgets.EditUsers import EditUsers
from Sources.init_config import get_font
from Widgets.TimerDialog import TimerDialog

'''
    This module contains the menu bar of the application and its actions.
    Each action is a method of this class.
    The action change Shorcuts is not implemented yet, only in newTab / newTable.
'''

class MenuBar(Events):
    '''
    This class is the MenuBar of the application.
    '''
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        '''
        This is the constructor of the parent class and setups the menu bar.
        '''
        self.start_actions()
        self.tabWidgets = []
        
    def start_actions(self) -> None:
        '''
        This method sets the menu actions.
        It should be called only once, at the __init__ method.
        '''
        self.ui.menuData_Base.addAction("Backup", self.backup_database)
        self.ui.menuData_Base.addAction("Restore", self.restore_database)
        self.ui.menuData_Base.addAction("Remove Backup", self.remove_backup)
        self.ui.menuData_Base.addAction("Import Data Base file", self.import_database)
        self.ui.menuData_Base.addAction("Export Data Base file", self.export_database)
        self.ui.menuData_Base.addAction("Export Data as ...", self.export_data)
        self.ui.menuData_Base.addAction("Data Base Editor", self.edit_database)
        self.ui.menuSettings.addAction("Change Theme", self.change_theme)
        self.ui.menuSettings.addAction("Change Font", self.change_font)
        self.ui.menuSettings.addAction("Edit Users", self.edit_users)
        self.ui.menuSettings.addAction("Change Table Shortcuts", None)
        self.ui.menuSettings.addAction("Change Encryption", self.change_encryption)
        
        
    def turn_off_actions_menu(self) -> None:
        '''
        This method turns off the menu actions for setup, recovery and login.
        '''
        self.ui.menuData_Base.actions()[0].setEnabled(False)
        self.ui.menuData_Base.actions()[1].setEnabled(False)
        self.ui.menuData_Base.actions()[2].setEnabled(False)
        self.ui.menuData_Base.actions()[3].setEnabled(False)
        self.ui.menuData_Base.actions()[4].setEnabled(False)
        self.ui.menuData_Base.actions()[5].setEnabled(False)
        self.ui.menuData_Base.actions()[6].setEnabled(False)
        self.ui.menuSettings.actions()[0].setEnabled(True)
        self.ui.menuSettings.actions()[1].setEnabled(True)
        self.ui.menuSettings.actions()[2].setEnabled(False)
        self.ui.menuSettings.actions()[3].setEnabled(False)
        self.ui.menuSettings.actions()[4].setEnabled(False)
        
    def turn_on_actions_menu(self) -> None:
        '''
        This method turns on the menu actions for when the user authenticates.
        '''
        self.ui.menuData_Base.actions()[0].setEnabled(True)
        self.ui.menuData_Base.actions()[1].setEnabled(True)
        self.ui.menuData_Base.actions()[2].setEnabled(True)
        self.ui.menuData_Base.actions()[3].setEnabled(True)
        self.ui.menuData_Base.actions()[4].setEnabled(True)
        self.ui.menuData_Base.actions()[5].setEnabled(True)
        self.ui.menuData_Base.actions()[6].setEnabled(True)
        self.ui.menuSettings.actions()[0].setEnabled(True)
        self.ui.menuSettings.actions()[1].setEnabled(True)
        self.ui.menuSettings.actions()[2].setEnabled(True)
        self.ui.menuSettings.actions()[3].setEnabled(True)
        self.ui.menuSettings.actions()[4].setEnabled(True)
        
    def edit_database(self) -> None:
        '''
        This method goes to the editor.
        '''
        self.flags.login = True
        self.setup_editor()
        self.go_editor()

    def import_database(self) -> None:
        '''
        This method opens a dialog to select the database file to import.
        If the user selects a file, it will be copied to the current database and the current database will be deleted.
        Before the import, the user will be asked to confirm the operation.
        If any error occurs, the user will be notified.
        '''
        file_dialog = QFileDialog()
        file_dialog.setNameFilter("Database files (*.db)")
        file_dialog.setAcceptMode(QFileDialog.AcceptOpen)
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        file_dialog.setModal(True)
        ans = file_dialog.exec_()
        if ans != -1 and ans != 0:
            selected_file = file_dialog.selectedFiles()[0]
            if not selected_file.endswith(".db"):
                show_dialog(self, "info", "Please select a database file.", get_font())
                return
            confirm_dialog = show_question(self, "warning", "Restoring the database will delete all data in the current database. Are you sure you want to continue?", get_font())
            if confirm_dialog == True:
                try:
                    shutil.copy2(selected_file, ".bin/src.db")
                    show_dialog(self, "info", "The database was successfully restored.", get_font())
                    self.open_database()
                except Exception as e:
                    show_dialog(self, "error", f"info: {e}", get_font())

    def export_database(self) -> None:
        '''
        This method opens a dialog to select where to save the database file.
        When the user selects the destination, the current database will be copied to the selected destination.
        If any error occurs, a dialog will be opened to inform the user.
        '''
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()", "", "Database Files (*.db);;All Files (*)", options=options)
        if file_name:
            if not file_name.endswith('.db'):
                file_name += '.db'
            try:
                shutil.copy2('.bin/src.db', file_name)
            except Exception as e:
                show_dialog(self, "error", f"info: {e}", get_font())
                return
        else:
            return

    def export_data(self) -> None:
        '''
        This method opens a dialog to prompt the user to select the type of file he wants to export.
        Then it opens a file dialog to select the path and name of the file.
        After that it converts the data from the database to the selected file type and saves it.
        Currently only Excel and JSON are supported.
        '''
        dialog = QInputDialog(self)
        dialog.setModal(True)
        dialog.setFont(get_font())
        dialog.setContentsMargins(10, 10, 10, 10)
        dialog.setLabelText("Select the type of file you want to export:")
        dialog.setComboBoxItems(["Excel", "JSON"])
        dialog.setOkButtonText("Select")
        dialog.setCancelButtonText("Cancel")
        result = dialog.exec_()
        if result != -1 and result != 0:
            file_type = dialog.textValue()
            file_format = {"Excel": ".xlsx", "JSON": ".json"}
            now = datetime.datetime.now().strftime("%Y-%m-%d")
            output_file = "Database" + now + file_format[file_type]
            file_dialog = QFileDialog()
            file_dialog.setAcceptMode(QFileDialog.AcceptSave)
            file_dialog.setDefaultSuffix(file_format[file_type])
            file_dialog.setFileMode(QFileDialog.AnyFile)
            file_dialog.setDirectory(".")
            file_dialog.selectFile(output_file)
            if file_dialog.exec_() == QFileDialog.Accepted:
                output_file = file_dialog.selectedFiles()[0]
                if file_type == "Excel":
                    conn = sqlite3.connect(".bin/src.db")
                    with conn:
                        cursor = conn.cursor()
                        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
                        with pd.ExcelWriter(output_file) as writer:
                            for table_name in cursor.fetchall():
                                table_name = table_name[0]
                                df = pd.read_sql_query("SELECT * from " + table_name, conn)
                                df.to_excel(writer, sheet_name=table_name, index=False)
                elif file_type == "JSON":
                    conn = sqlite3.connect(".bin/src.db")
                    with conn:
                        cursor = conn.cursor()
                        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
                        with open(output_file, 'w') as f:
                            for table_name in cursor.fetchall():
                                table_name = table_name[0]
                                df = pd.read_sql_query("SELECT * from " + table_name, conn)
                                df.to_json(f, orient='index')
       
    def restore_database(self) -> None:
        '''
        This method opens a dialog to select the backup file to restore.
        Then it copies the selected file to the database file, deleting the old database file.
        If there are no backups, a dialog will be opened to inform the user.
        '''
        backup_folder = ".backups"
        backups = [f for f in os.listdir(backup_folder) if os.path.isfile(os.path.join(backup_folder, f))]
        if not backups:
            show_dialog(self, "info", "No backups found.", get_font())
            return
        options = backups
        dialog = QInputDialog(self)
        dialog.setModal(True)
        dialog.setContentsMargins(10, 10, 10, 10)
        dialog.setWindowTitle('Select Backup')
        dialog.setLabelText('Backups:')
        dialog.setComboBoxItems(options)
        dialog.resize(300, 200)
        dialog.setFont(get_font())
        selected_index = dialog.exec_()
        if selected_index != -1 and selected_index != 0:
            item = dialog.textValue()
            shutil.copy2(os.path.join(backup_folder, item), ".bin/src.db")
            show_dialog(self, "info", "The selected backup has been restored.", get_font())
            self.open_database()

    def backup_database(self) -> None:
        '''
        This method opens a dialog to prompt the user to enter the name of the backup.
        Then it copies the database file to the backup folder with the name entered by the user.
        If a backup with the same name already exists or if the name is empty, a dialog will be opened to inform the user.
        '''        
        backup_folder = ".backups"
        if not os.path.exists(backup_folder):
            os.makedirs(backup_folder)
        input_dialog = QInputDialog()
        input_dialog.setModal(True)
        input_dialog.setFont(get_font())
        input_dialog.setInputMode(QInputDialog.TextInput)
        input_dialog.setLabelText("Enter backup name:")
        input_dialog.setContentsMargins(10, 10, 10, 10)
        input_dialog.setWindowTitle("Backup Database")
        answer = input_dialog.exec_()
        if answer != -1 and answer != 0:
            output_file = input_dialog.textValue()
            if output_file == "":
                show_dialog(self, "error", "The backup name cannot be empty.", get_font())
                self.backup_database()
            output_path = os.path.join(backup_folder, output_file)
            if os.path.exists(output_path):
                show_dialog(self, "error", "A backup with the same name already exists.", get_font())
                self.backup_database()
            shutil.copy2(".bin/src.db", output_path)
            show_dialog(self, "info", "The backup was successful.", get_font())
            
    def remove_backup(self) -> None:  
        '''
        This method opens a dialog to select the backup to remove.
        Then it deletes the selected backup file.
        If there are no backups, a dialog will be opened to inform the user.
        '''   
        backup_folder = ".backups"
        backups = [f for f in os.listdir(backup_folder) if os.path.isfile(os.path.join(backup_folder, f))]
        if not backups:
            show_dialog(self, "info", "No backups found.", get_font())
            return
        options = backups
        dialog = QInputDialog(self)
        dialog.setModal(True)
        dialog.setWindowTitle('Remove Backup')
        dialog.setLabelText('Select the backup to remove:')
        dialog.setComboBoxItems(options)
        dialog.setContentsMargins(10, 10, 10, 10)
        dialog.setFont(get_font())
        selected_index = dialog.exec_()
        if selected_index != -1 and selected_index != 0:
            item = dialog.textValue()
            os.remove(os.path.join(backup_folder, item))
            show_dialog(self, "info", f"The backup {item} has been removed.", get_font())

    def edit_users(self) -> None:
        '''
        This method opens the EditUsers window to edit the users in the program.
        More info in the EditUsers class.
        '''
        EditUsers(self)
        
    def change_theme(self) -> None:
        '''
        This method opens the ChangeTheme window to change the theme of the program.
        After setting the theme, the config file is updated.
        After setting the theme the font size of the widgets is updated because it is not updated automatically and returns to the default window size value.
        '''
        options = ['Light', 'Dark']
        dialog = QInputDialog(self)
        dialog.setModal(True)
        dialog.setWindowTitle('Select Theme')
        dialog.setLabelText('Choose a theme:')
        dialog.setComboBoxItems(options)
        dialog.setContentsMargins(10, 10, 10, 10)
        dialog.setFont(get_font())
        previous_font_buttons, previous_font_labels, previous_font_widgets, previous_tabWidgets = self.get_previous_font_size_widgets()
        selected_index = dialog.exec_()
        if selected_index != -1 and selected_index != 0:
            selected_option = dialog.textValue()
            if selected_option == 'Light':
                selected_option = 'light'
                qdarktheme.setup_theme(selected_option)
            else:
                selected_option = 'dark'
                qdarktheme.setup_theme(selected_option)
            config = configparser.ConfigParser()
            config.read('config.ini')
            config.set('DEFAULT', 'current_theme', selected_option)
            with open('config.ini', 'w') as configfile:
                config.write(configfile)
            self.apply_previous_font_size_widgets(previous_font_buttons, previous_font_labels, previous_font_widgets, previous_tabWidgets)

    def get_previous_font_size_widgets(self) -> None:
        '''
        This method gets the previous font size of the widgets.
        Its purpose is to be able to apply the previous font size after changing the theme.
        '''
        previous_font_buttons = []
        previous_font_labels = []
        previous_font_widgets = []
        previous_tabWidgets = []
        for widget in self.widgets.values():
            previous_font_widgets.append(widget['widget'].font().pointSize())
        for widget in self.buttons.values():
            previous_font_buttons.append(widget['widget'].font().pointSize())
        for widget in self.labels.values():
            previous_font_labels.append(widget['widget'].font().pointSize())
        for dict in self.tabWidgets:
            for widget in dict.values():
                previous_tabWidgets.append(widget['widget'].font().pointSize())
        return previous_font_buttons, previous_font_labels, previous_font_widgets, previous_tabWidgets
        
    def apply_previous_font_size_widgets(self, previous_font_buttons, previous_font_labels, previous_font_widgets, previous_tabWidgets) -> None:
        '''
        This method applies the previous font size of the widgets.
        Its purpose is to be able to apply the previous font size after changing the theme.
        '''
        for i, widget in enumerate(self.widgets.values()):
            widget['widget'].setFont(QFont(widget['widget'].font().family(), previous_font_widgets[i]))
        for i, widget in enumerate(self.buttons.values()):
            widget['widget'].setFont(QFont(widget['widget'].font().family(), previous_font_buttons[i]))
        for i, widget in enumerate(self.labels.values()):
            widget['widget'].setFont(QFont(widget['widget'].font().family(), previous_font_labels[i]))
        for dict in self.tabWidgets:
            for i, widget in enumerate(dict.values()):
                widget['widget'].setFont(QFont(widget['widget'].font().family(), previous_tabWidgets[i]))
        self.update_events()
        
    def change_font(self) -> None:
        '''
        This method opens a dialog to change the font of the program.
        After the font is changed, the program will update the font of the widgets and display a dialog to verify if the user wants to save the changes.
        If the user accepts, the config file will be updated.
        If not, the font will be restored to the previous one.
        '''
        font_dialog = QFontDialog(self)
        font_dialog.setModal(True)
        font_dialog.setFont(get_font())
        old_font = copy.copy(get_font())
        ok, font = font_dialog.getFont()
        if ok:
            for widget in self.widgets.values():
                widget['widget'].setFont(QFont(font.family(), widget['widget'].font().pointSize()))
            for widget in self.buttons.values():
                widget['widget'].setFont(QFont(font.family(), widget['widget'].font().pointSize()))
            for widget in self.labels.values():
                widget['widget'].setFont(QFont(font.family(), widget['widget'].font().pointSize()))
            for dict in self.tabWidgets:
                for widget in dict.values():
                    widget['widget'].setFont(QFont(font.family(), widget['widget'].font().pointSize()))
            self.update_events()
            verification = TimerDialog(self)
            if verification.exec_() == QDialog.Accepted:
                config = configparser.ConfigParser()
                config.read('config.ini')
                config.set('DEFAULT', 'font', QFont(font).family())
                with open('config.ini', 'w') as configfile:
                    config.write(configfile)
            else:
                for widget in self.widgets.values():
                    widget['widget'].setFont(QFont(old_font.family(), widget['widget'].font().pointSize()))
                for widget in self.buttons.values():
                    widget['widget'].setFont(QFont(old_font.family(), widget['widget'].font().pointSize()))
                for widget in self.labels.values():
                    widget['widget'].setFont(QFont(old_font.family(), widget['widget'].font().pointSize()))
                for dict in self.tabWidgets:
                    for widget in dict.values():
                        widget['widget'].setFont(QFont(old_font.family(), widget['widget'].font().pointSize()))
        self.update_events()
            
    def change_encryption(self) -> None:
        '''
        This method opens a dialog to change the encryption of the program.
        If the user chooses to disable the encryption, a warning will be displayed to verify if the user is sure.
        If the user chooses to proceed, the config file will be updated.
        '''
        dialog = QInputDialog()
        dialog.setModal(True)
        dialog.setFont(get_font())
        dialog.setComboBoxItems(['True', 'False'])
        dialog.setLabelText('Choose a encryption:')
        dialog.setWindowTitle('Select Encryption')
        dialog.resize(300, 200)
        dialog.setFont(get_font())
        selected_index = dialog.exec_()
        if selected_index != -1 and selected_index != 0:
            selected_option = dialog.textValue()
            answer = selected_option
            if self.data.config == 'T' and answer == 'False':
                warning = show_question(self,  "Warning", "Are you sure you want to disable encryption? This will make your data vulnerable to hackers.", get_font())
                if warning == True:
                    self.update_config('F')
            elif self.data.config == 'F' and answer == 'True':
                self.update_config('T')
            else:
                return  
    
    def update_config(self, new_config) -> None:
        '''
        This function is used to update the encryption value in the user loggin information
        Its purpose is to be able to update the encryption value in the database.
        Auxiliary function of change_encryption.
        '''
        self.data.update_values(retrieve_from_db())
        conn = sqlite3.connect('.bin/log.db')
        with conn:
            c = conn.cursor()
            c.execute("SELECT users, passwrds, code, email, config, key FROM data")
            result = c.fetchone()
            users = result[0]
            passwrds = result[1]
            code = result[2]
            email = result[3]
            config = result[4]
            key = result[5]
        encrypted_config = encrypt(str(new_config).encode(), key)
        conn = sqlite3.connect('.bin/log.db')
        with conn:
            c = conn.cursor()
            c.execute("UPDATE data SET config = ?", (encrypted_config,))
            conn.commit()
        self.data.config = new_config



        
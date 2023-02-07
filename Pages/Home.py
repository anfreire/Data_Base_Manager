from imports import *
from Sources.Classes import *
from Widgets.editusers import *
from Sources.Functions import *
from Widgets.align_input import *
from Widgets.configuration import *
from init_config import costum_font

class Home(Widget):
    '''
    This class is the home of the application, the window after the login.
    '''
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        '''
        This is the constructor of the class.
        '''
        self.start_widgets_home()
        
    def start_widgets_home(self) -> None:
        '''
        This method starts the widgets of the home page.
        It should be called only once, at the __init__ method.
        '''
        disconnect_button(self.ui.enter_the_database_db_button)
        self.ui.enter_the_database_db_button.clicked.connect(lambda:self.go_tables_from_home())
        disconnect_button(self.ui.logout_db_button)
        self.ui.logout_db_button.clicked.connect(lambda:self.go_login_from_home())
        disconnect_button(self.ui.edit_db_db_button)
        self.ui.edit_db_db_button.clicked.connect(lambda:self.go_editor_from_home())
        disconnect_button(self.ui.export_data_specific_file_format_home_db_button)
        self.ui.export_data_specific_file_format_home_db_button.clicked.connect(lambda:self.export_data())
        disconnect_button(self.ui.backup_restore_db_button)
        self.ui.backup_restore_db_button.clicked.connect(lambda:self.backup_restore())
        disconnect_button(self.ui.edit_users_home_db_button)
        self.ui.edit_users_home_db_button.clicked.connect(lambda:self.edit_users())
        disconnect_button(self.ui.settings_db_button)
        self.ui.settings_db_button.clicked.connect(lambda:self.settings())
        disconnect_button(self.ui.import_data_from_different_file_formats_home_db_button)
        self.ui.import_data_from_different_file_formats_home_db_button.clicked.connect(lambda:self.import_data())

    def go_home(self) -> None:
        '''
        This method sets the home page as the current page.
        '''
        self.set_middle_table_close_event()
        self.ui.stackedWidget.setCurrentWidget(self.ui.home)
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.home_db)

    def go_tables_from_home(self) -> None:
        '''
        This method goes to the tables window from the home window.
        '''
        self.set_middle_table_close_event()
        self.open_database()
        self.go_tables()
        
    def go_editor_from_home(self) -> None:
        '''
        This method goes to the editor window from the home window.
        '''
        self.flags.login = True
        self.setup_editor()
        self.go_editor()
        
    def go_login_from_home(self) -> None:
        '''
        This method logs out the user and goes to the login window from the home window.
        Encrypts the database if the user has chosen to do so.
        '''
        if self.data.config == 'T':
            encrypt_database(self.data)
        self.empty_login()
        self.setup_login()
        self.go_login()

    def import_data(self) -> None:
        '''
        Still working on it.    t(ಠ益ಠ t)
        '''
        dialog = QMessageBox(self)
        dialog.setFont(costum_font)
        dialog.information(self, "Not available", "This feature is not available yet.", QMessageBox.Ok)
        return
        # dialog = QInputDialog(self)
        # dialog.setFont(costum_font)
        # dialog.setLabelText("Select the type of file you want to import:")
        # dialog.setComboBoxItems(["Excel"])
        # dialog.setOkButtonText("Select")
        # dialog.setCancelButtonText("Cancel")
        # options = QFileDialog.Options()
        # options |= QFileDialog.ReadOnly
        # result = dialog.exec_()
        # if result == QDialog.Accepted:
        #     dialog = QMessageBox(self)
        #     dialog.setFont(costum_font)
        #     dialog.information(self, "Instructions", "Move the columns to the right position and then click on 'Proceed' to import the data.", QMessageBox.Ok)
        #     conn = sqlite3.connect(".bin/src.db")
        #     with conn:
        #         cursor = conn.cursor()
        #         table_names = [row[0] for row in cursor.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()]
        #     file_type = dialog.textValue()
        #     if file_type == "Excel":
        #         fileName, _ = QFileDialog.getOpenFileName(self,"Open Excel File", "","Excel Files (*.xls, *xlsx);;All Files (*)", options=options)
        #         if fileName.endswith('.xls') or fileName.endswith('.xlsx'):
        #             sheet_names = pd.read_excel(fileName, sheet_name=None).keys()
        #             if len(sheet_names) > 1 and len(table_names) > 1:
        #                 tmp = Align_input(table_names, sheet_names , self)
        #                 mapping_db = tmp.get_mapping_db()
        #                 mapping_file = tmp.get_mapping_excel()
                        
        #                 for sheet_name, table_name in zip(sheet_names, table_names):
        #                     if mapping_file[sheet_name] == table_name:
        #                         df = pd.read_excel(fileName, sheet_name=sheet_name)
        #                         columns = df.columns.tolist()
        #                         conn = sqlite3.connect(".bin/src.db")
        #                         with conn:
        #                             cursor = conn.cursor()
        #                             table_columns = [row[1] for row in cursor.execute(f"PRAGMA table_info ({table_name})").fetchall()]
        #                             if str(table_name).startswith("sqlite_") or str(table_columns).startswith("sqlite_"):
        #                                 continue
        #                             df = df[[mapping_file.get(col, col) for col in columns]]
        #                             df = df.drop(columns=[col for col in table_columns if col not in mapping_db.values()], axis=1)
        #                             df.to_sql(table_name, conn, if_exists='replace')           
        #             elif len(sheet_names) > 1 and len(table_names) == 1:
        #                 sheet_chooser = QInputDialog(self)
        #                 sheet_chooser.setLabelText("Select the sheet you want to import:")
        #                 sheet_chooser.setComboBoxItems(sheet_names)
        #                 sheet_chooser.setOkButtonText("Select")
        #                 sheet_chooser.setCancelButtonText("Cancel")
        #                 result = sheet_chooser.exec_()
        #                 if result == QDialog.Accepted:
        #                     df = pd.read_excel(fileName, sheet_name=None)
        #                     conn = sqlite3.connect(".bin/src.db")
        #                     with conn:
        #                         cursor = conn.cursor()
        #                         table_names = [row[1] for row in cursor.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()]
        #                         for sheet_name in df.keys():
        #                             df_sheet = df[sheet_name]
        #                             columns = df_sheet.columns.tolist()
        #                             if sheet_name in table_names:
        #                                 table_info = [row[1] for row in cursor.execute(f"PRAGMA table_info ({sheet_name})").fetchall()]
        #                                 mapping = Align_input(table_info, columns, self)
        #                                 mapping_db = mapping.get_mapping_db()
        #                                 mapping_file = mapping.get_mapping_excel()
        #                                 df_sheet = df_sheet[[mapping_file.get(col, col) for col in columns]]
        #                                 df_sheet = df_sheet.drop(columns=[col for col in table_info if col not in mapping_db.values()], axis=1)
        #                                 df_sheet.to_sql(sheet_name, conn, if_exists='replace')   
        #                 else:
        #                     return
        #             elif len(sheet_names) == 1 and len(table_names) > 1:
        #                 table_chooser = QInputDialog(self)
        #                 table_chooser.setLabelText("Select the table you want to import:")
        #                 table_chooser.setComboBoxItems(table_names)
        #                 table_chooser.setOkButtonText("Select")
        #                 table_chooser.setCancelButtonText("Cancel")
        #                 result = table_chooser.exec_()
        #                 if result == QDialog.Accepted:
        #                     df = pd.read_excel(fileName, sheet_name="Sheet1")
        #                     columns = df.columns.tolist()
        #                     conn = sqlite3.connect(".bin/src.db")
        #                     with conn:
        #                         cursor = conn.cursor()
        #                         selected_table = table_chooser.comboBox().currentText()
        #                         table_columns = [row[1] for row in cursor.execute(f"PRAGMA table_info ({selected_table})").fetchall()]
        #                         align_input = Align_input(table_columns, columns, self)
        #                         mapping_db = align_input.get_mapping_db()
        #                         mapping_file = align_input.get_mapping_excel()
        #                         df = df[[mapping_file.get(col, col) for col in columns]]
        #                         df = df.drop(columns=[col for col in table_columns if col not in mapping_db.values()], axis=1)
        #                         df.to_sql(selected_table, conn, if_exists='replace')               
        #                 else:
        #                     return
        #             elif len(sheet_names) == 1 and len(table_names) == 1:
        #                 df = pd.read_excel(fileName, sheet_name="Sheet1")
        #                 columns = df.columns.tolist()
        #                 conn = sqlite3.connect(".bin/src.db")
        #                 with conn:
        #                     cursor = conn.cursor()
        #                     table_names = [row[1] for row in cursor.execute(f"PRAGMA table_info ({table_names[0]})").fetchall()]
        #                     tmp = Align_input(table_names, columns, self)
        #                     mapping_db = tmp.get_mapping_db()
        #                     mapping_file = tmp.get_mapping_excel()
        #                     df = df[ [mapping_file.get(col, col) for col in columns] ]
        #                     df = df.drop(columns=[col for col in table_names if col not in mapping_db.values()], axis=1)
        #                     df.to_sql(table_names[0], conn, if_exists='replace')
        #         else:
        #             dialog = QMessageBox()
        #             dialog.setFont(costum_font)
        #             dialog.critical(self, "Error", "Not a Excel file! (.xls or .xlsx)", QMessageBox.Ok)
        #     else:
        #         dialog = QMessageBox()
        #         dialog.setFont(costum_font)
        #         dialog.critical(self, "Error", "No file has been setected!", QMessageBox.Ok)
                
    def settings(self) -> None:
        '''
        Opens the costum dialog Settings to change the settings of the application.
        '''
        Configuration(self)

    def export_data(self) -> None:
        '''
        This method opens a dialog to prompt the user to select the type of file he wants to export.
        Then it opens a file dialog to select the path and name of the file.
        After that it converts the data from the database to the selected file type and saves it.
        '''
        dialog = QInputDialog(self)
        dialog.setFont(costum_font)
        dialog.setLabelText("Select the type of file you want to export:")
        dialog.setComboBoxItems(["CSV", "Excel", "JSON", "SQL"])
        dialog.setOkButtonText("Select")
        dialog.setCancelButtonText("Cancel")
        result = dialog.exec_()
        if result == QDialog.Accepted:
            file_type = dialog.textValue()
            file_format = {"CSV": ".csv", "Excel": ".xlsx", "JSON": ".json", "SQL": ".sql"}
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
                if file_type == "CSV":
                    conn = sqlite3.connect(".bin/src.db")
                    with conn:
                        cursor = conn.cursor()
                        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
                        with pd.ExcelWriter("temp.xlsx") as writer:
                            for table_name in cursor.fetchall():
                                table_name = table_name[0]
                                df = pd.read_sql_query("SELECT * from " + table_name, conn)
                                df.to_excel(writer, sheet_name=table_name, index=False)
                        book = openpyxl.load_workbook("temp.xlsx")
                    with open(output_file, 'w', newline='') as f:
                        c = csv.writer(f)
                        for sheet in book:
                            for row in sheet.iter_rows(values_only=True):
                                c.writerow(row)
                    os.remove("temp.xlsx")
                elif file_type == "Excel":
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
                elif file_type == "SQL":
                    conn = sqlite3.connect(".bin/src.db")
                    with open(output_file, 'w') as f:
                        for line in conn.iterdump():
                            f.write('%s\n' % line)
        
    def backup_restore(self) -> None:
        '''
        This method opens a dialog to prompt the user to select the type of operation he wants to operate.
        Then it opens a file dialog to select the path and name of the file, depending on the operation.
        More info about the operations in the methods backup_database and restore_database.
        '''
        dialog = QInputDialog(self)
        dialog.setFont(costum_font)
        dialog.setLabelText("Select the type of operation you want to operate:")
        dialog.setComboBoxItems(["Backup", "Restore"])
        dialog.setOkButtonText("Select")
        dialog.setCancelButtonText("Cancel")
        dialog.setFont(costum_font)
        result = dialog.exec_()
        if result == QDialog.Accepted:
            file_type = dialog.textValue()
            if file_type == "Backup":
                self.backup_database()
            elif file_type == "Restore":
                self.restore_database()

    def drop_tables(self, conn : sqlite3.Connection):
        '''
        This method is auxiliary to the restore_database method.
        It drops all the tables in the database to execute the restore operation.
        '''
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        table_names = [row[0] for row in cursor.fetchall()]
        for table_name in table_names:
            if table_name != 'sqlite_sequence':
                conn.execute(f"DROP TABLE IF EXISTS {table_name};")
       
    def restore_database(self) -> None:
        '''
        This method opens a file dialog to select the backup file.
        Then it opens a dialog to prompt the user to confirm the operation.
        If the user confirms, it drops all the tables in the database and executes the backup file.
        '''
        file_dialog = QFileDialog()
        file_dialog.setAcceptMode(QFileDialog.AcceptOpen)
        file_dialog.setFileMode(QFileDialog.AnyFile)
        file_dialog.setDirectory(".")
        file_dialog.setNameFilter("Backup (*.sql)")
        if file_dialog.exec_() == QFileDialog.Accepted:
            restart_question_2 = QMessageBox.question(self, 'WARNING', "This will delete all the data in the database.\nMake sure the backup file is valid and up to date.\nDo you want to continue?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if restart_question_2 == QMessageBox.Yes:
                file_name = file_dialog.selectedFiles()[0]
                conn = sqlite3.connect(".bin/src.db")
                with conn:
                    self.drop_tables(conn)
                    with open(file_name, 'r') as f:
                        conn.executescript(f.read())
                self.go_tables_from_home()
                
    def backup_database(self) -> None:
        '''
        This method opens a file dialog to select the path and name of the backup file.
        Then executes the backup and saves it in the selected location.
        '''
        now = datetime.datetime.now().strftime("%Y-%m-%d")
        output_file = "database_dump" + now + ".sql"
        file_dialog = QFileDialog()
        file_dialog.setAcceptMode(QFileDialog.AcceptSave)
        file_dialog.setDefaultSuffix(".sql")
        file_dialog.setFileMode(QFileDialog.AnyFile)
        file_dialog.setDirectory(".")
        file_dialog.selectFile(output_file)
        if file_dialog.exec_() == QFileDialog.Accepted:
            output_file = file_dialog.selectedFiles()[0]
            conn = sqlite3.connect(".bin/src.db")
            with io.open(output_file, 'w') as p: 
          
                with conn:
                    for line in conn.iterdump(): 
                        
                        p.write('%s\n' % line)
            dialog = QMessageBox()
            dialog.setFont(costum_font)
            dialog.information(self, "Backup Successful", "The backup was sucedded.", QMessageBox.Ok)
                
    def edit_users(self) -> None:
        '''
        This method opens the EditUsers window to edit the users in the program.
        More info in the EditUsers class.
        '''
        EditUsers(self)



        
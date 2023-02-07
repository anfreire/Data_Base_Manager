from imports import *
from init_config import costum_font

class CodeVerify(QDialog):
    '''
    Dialog to verify the code sent to the user's email.
    It has 2 parameters: code and flag.
    The code is the code sent to the user's email.
    The flag is the flag that will be used to verify the code, and it will be used as a return value.
    If the code is valid, it will set the flag to True, and if it's not, it will set the flag to False.
    Its important to note that the flag must be initialized as False.
    The flag is acesseble through the get_flag() method.
    '''
    def __init__(self, code: str, flag: bool, parent=None) -> None:
        super().__init__(parent)
        '''
        Constructor of the Code Verify Dialog Layout.
        Executes the dialog in the last line.
        '''
        self.setWindowTitle("Verification Code")
        self.code = code
        self.flag = flag
        self.code_input = QLineEdit()
        code_label = QLabel("Code:")
        email_prompt = QLabel("Enter the code that was sent to your email\nIf you don't see it, it should be in your spam folder.")
        layout = QFormLayout()
        layout.addRow(email_prompt)
        layout.addRow(code_label, self.code_input)
        verify_button = QPushButton("Verify")
        cancel_button = QPushButton("Cancel")
        verify_button.clicked.connect(self.verify_code_)
        cancel_button.clicked.connect(self.reject)
        layout.addRow(verify_button, cancel_button)
        font = self.code_input.font()
        font.setPointSize(font.pointSize() + 4)
        self.code_input.setFont(costum_font)
        code_label.setFont(costum_font)
        verify_button.setFont(costum_font)
        cancel_button.setFont(costum_font)
        email_prompt.setFont(costum_font)
        layout.setVerticalSpacing(20)
        layout.setContentsMargins(40,40,40,40)
        self.setLayout(layout)
        self.exec()

    def verify_code_(self) -> None:
        '''
        Verifies the code entered by the user.
        Opens a message box if the code is invalid.
        Sets the flag to True if the code is valid, and to False if it's not, as explained in the class description.
        '''
        code = self.code_input.text()
        if code == self.code:
            self.flag = True
            self.accept()
        else:
            dialog = QMessageBox()
            dialog.setFont(costum_font)
            dialog.critical(None, "Error", "Invalid code, try again", QMessageBox.Ok)
            self.code_input.clear()
            self.flag = False

    def get_flag(self) -> bool:
        '''
        Returns the flag.
        The flag is True if the code is valid, and False if it's not, as explained in the class description.
        '''
        return self.flag


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
        self.username_input.setFont(costum_font)
        self.password_input.setFont(costum_font)
        username_label.setFont(costum_font)
        password_label.setFont(costum_font)
        add_button.setFont(costum_font)
        cancel_button.setFont(costum_font)
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
            dialog = QMessageBox()
            dialog.setFont(costum_font)
            dialog.critical(None, "Error", "User already registred!", QMessageBox.Ok)
            return
        elif username == None or username == '' or username.isspace() or username == 'username':
            dialog = QMessageBox()
            dialog.setFont(costum_font)
            dialog.critical(None, "Error", "Invalid username!", QMessageBox.Ok)
            return
        elif password == None or password.isspace() or password == '' or password == 'password':
            dialog = QMessageBox()
            dialog.setFont(costum_font)
            dialog.critical(None, "Error", "Invalid password!", QMessageBox.Ok)
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


'''
Macros for the Field Dialog
Information about the macros in the class description.
'''
ADD = 1
EDIT = 2

class FieldDialog(QDialog):
    '''
    This class is the dialog for displaying the fields in the Data Base and perfmorming operations on them.
    Uses the macros ADD and EDIT to determine if the dialog is being used to add a row or edit a row.
    This class methods get together to perform the operations described above, none of them return values for the user.
    The class methods contains various sqlite3 statements to perform the operations in the database.
    '''
    def __init__(self, parent):
        super().__init__(parent)
        '''
        Constructor of the Field Dialog Layout.
        '''
        self.parent = parent
        scroll_area = QScrollArea(self)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        widget = QWidget(scroll_area)
        scroll_area.setWidget(widget)
        scroll_area.setWidgetResizable(True)
        layout = QFormLayout(widget)
        self.fields = {}
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(scroll_area)
        self.setLayout(main_layout)
        self.unique_columns = []
        for i, column in enumerate(self.parent.column_names):
            field = QLineEdit()
            field.setFont(QFont("Ubuntu Thin", 18))
            field.setPlaceholderText(self.parent.column_types[i])
            field.setMinimumWidth(300)
            label = QLabel(f'{column}:')
            label.setFont(QFont("Ubuntu Thin", 18))
            field.adjustSize()
            label.adjustSize()
            layout.addRow(label, field)
            self.fields[column] = field
        self.buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, Qt.Horizontal, self)
        self.buttons.buttons()[0].setFixedSize(120, 40)
        self.buttons.buttons()[1].setFixedSize(120, 40) 
        self.buttons.buttons()[0].setFont(costum_font)
        self.buttons.buttons()[1].setFont(costum_font)
        self.buttons.rejected.connect(self.reject)
        layout.addRow(self.buttons)
        for column in self.parent.column_names:
            if self.is_column_unique(column):
                self.unique_columns.append(column)
    

    def get_values(self) -> dict:
        '''
        This method returns a dictionary with the values of the fields.
        '''
        values = {}
        for column, field in self.fields.items():
            values[column] = field.text()
        return values

    def is_column_unique(self, column: int) -> bool:
        '''
        This method checks if the column is unique, by the sqlite3 policy.
        Returns True if the column accepts repeated values, False otherwise.
        '''
        conn = sqlite3.connect(".bin/src.db")
        with conn:
            c = conn.cursor()
            query = f"SELECT COUNT(*) FROM (SELECT {column} FROM {self.parent.sheet_name} GROUP BY {column}) subquery"
            c.execute(query)
            count = c.fetchone()[0]
            return count

    def check_existing_values(self, flag : int = ADD | EDIT) -> bool:
        '''
        This method checks if the values of the fields are already in the database.
        Supports the modes ADD and EDIT.
        The modes are chosen by the macros ADD or EDIT.
        If the mode is ADD, it will check if the values are already in the database.
        If the mode is EDIT, it will check if the values are already in the database, except for the row that is being edited.
        Returns True if the values are not in the database, False otherwise.
        '''
        values = self.get_values()
        for i in range(self.parent.rowCount()):
            if flag == EDIT and i == self.parent.currentRow():
                continue
            for j in range(len(self.unique_columns)):
                if self.parent.item(i, j).text() == values[self.parent.column_names[j]] and flag == ADD:
                    self.parent.setSelectionBehavior(QAbstractItemView.SelectItems)
                    self.parent.scrollToItem(self.item(i, j))
                    self.parent.setCurrentItem(self.item(i, j), 
                        QtCore.QItemSelectionModel.SelectCurrent)
                    self.parent.setSelectionBehavior(QAbstractItemView.SelectRows)
                    dialog = QMessageBox()
                    dialog.setFont(costum_font)
                    dialog.warning(self, "Warning", f"The vaule {values[self.parent.column_names[j]]} already exists in the database for the column {self.unique_columns[j]}.", QMessageBox.Ok)
                    return False
        return True

    def try_to_insert(self) -> bool:
        '''
        This method tries to insert the values of the fields into the database.
        The values are allways a row, so it will try to insert a row into the database.
        If sucessful, it will return True, False otherwise.
        '''
        values = self.get_values()
        conn = sqlite3.connect(".bin/src.db")
        with conn:
            c = conn.cursor()
            c.execute(f"SELECT * from {self.parent.sheet_name} LIMIT 1")
            num_columns = len(c.description)
            try:
                sql_stmt = f"INSERT INTO {self.parent.sheet_name} VALUES ({','.join(['?'] * num_columns)})"
                c.execute(sql_stmt, tuple(values.values()))
                conn.commit()
            except Exception as e:
                dialog = QMessageBox()
                dialog.setFont(costum_font)
                dialog.warning(self, "Warning", f"One of the values you are trying to insert into the database does not match the data type expected for that column. Check the data type of the columns and try again.\n info: {e}", QMessageBox.Ok)
                return False
        return True

    def try_to_edit(self) -> bool:
        '''
        This method tries to edit a row in the database.
        The values will appear in the fields, and the user will be able to edit them, if he wants.
        If sucessful, it will return True, False otherwise.
        '''
        conn = sqlite3.connect('.bin/src.db')
        self.parent.get_row_id_in_db()
        row_id = self.parent.row_id
        values = list(self.get_values().values())
        with conn:
            try:
                cursor = conn.cursor()
                update_statement = "UPDATE {} SET ".format(self.parent.table_name)
                new_values = []
                for column_name, new_value in zip(self.parent.column_names, values):
                    update_statement += f"{column_name}=?, "
                    new_values.append(new_value)
                update_statement = update_statement[:-2] + " WHERE rowid=?"
                new_values.append(int(row_id))
                cursor.execute(update_statement, new_values)
                conn.commit()
            except Exception as e:
                dialog = QMessageBox()
                dialog.setFont(costum_font)
                dialog.warning(self, "Warning", f"One of the values you are trying to insert into the database does not match the data type expected for that column. Check the data type of the columns and try again.\n info: {e}", QMessageBox.Ok)
                return False   
        return True

    def add_row(self) -> None:
        '''
        This method is a connector to the try_to_insert method.
        '''
        if self.check_existing_values(ADD) and self.try_to_insert():
            self.parent.update_table()
            self.accept()

    def edit_row(self) -> None:
        '''
        This method is a connector to the try_to_edit method.
        '''
        if self.check_existing_values(EDIT) and  self.try_to_edit():
                self.parent.update_table()
                self.accept()

    def add_row_signal(self) -> None:
        '''
        This method is a connector to the add_row method.
        '''
        self.buttons.accepted.connect(lambda:self.add_row())
        self.show()
    
    def edit_row_signal(self) -> None:
        '''
        This method is a connector to the edit_row method.
        '''
        self.buttons.accepted.connect(lambda:self.edit_row())
        for i, column in enumerate(self.parent.column_names):
            self.fields[column].setText(str(self.parent.sheet_data[self.parent.currentRow()][i]))
        self.show()
          

class AddColumn(QDialog):
    '''
    This class is the costum dialog that will appear when the user wants to add a column to a table in the Data Base Editor.
    '''
    def __init__(self, parent, table_name):
        '''
        This method is the constructor of the class.
        It will create the dialog and all the widgets that will be inside it.
        All the widgets will be connected to the methods that will handle them.
        After that, it will show the dialog with the widgets.
        When the user clicks on the "Add Column" button, the method run_statement will be called.
        '''
        super().__init__()
        self.parent = parent
        self.table_name = str(table_name).strip().replace(" ", "_").replace("-", "_").replace(".", "_").replace("(", "_").replace(")", "_").replace("[", "_").replace("]", "_")
        self.setWindowTitle("Add Column")

        layout = QFormLayout()
        font_label = costum_font
        font_label.setWeight(QFont.Bold)
        font_label.setFamily("Ubuntu Thin")

        # COLUMN NAME
        column_name_line_edit = QLineEdit()
        column_name_line_edit.setFont(costum_font)
        label = QLabel("Column Name")
        label.setFont(font_label)
        layout.addRow(label, column_name_line_edit)

        # NULL or NOT NULL
        null_checkbox = QCheckBox()
        null_checkbox.setFont(QFont("Arial", 10))
        label = QLabel("NOT NULL")
        label.setFont(font_label)
        layout.addRow(label, null_checkbox)

        # DEFAULT
        default_line_edit = QLineEdit()
        default_line_edit.setFont(costum_font)
        label = QLabel("DEFAULT")
        label.setFont(font_label)
        layout.addRow(label, default_line_edit)

        # CHECK
        check_line_edit = QLineEdit()
        check_line_edit.setFont(costum_font)
        label = QLabel("CHECK")
        label.setFont(font_label)
        layout.addRow(label, check_line_edit)

        # COLLATE
        collate_combo_box = QComboBox()
        collate_combo_box.setFont(costum_font)
        collate_combo_box.addItems(["BINARY", "NOCASE", "RTRIM"])
        label = QLabel("COLLATE")
        label.setFont(font_label)
        layout.addRow(label, collate_combo_box)
        
        # Datatype
        datatype_combo_box = QComboBox()
        datatype_combo_box.setFont(costum_font)
        datatype_combo_box.addItems(["INTEGER", "REAL", "TEXT", "BLOB"])
        label = QLabel("Data Type")
        label.setFont(font_label)
        layout.addRow(label, datatype_combo_box)

        # Add buttons
        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttons.setFont(costum_font)
        layout.addRow(buttons)

        # Connect signals
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)

        self.setLayout(layout)
        if self.exec_() == QDialog.Accepted:
            column_name = column_name_line_edit.text().strip().replace(" ", "_").replace("-", "_").replace(".", "_").replace("(", "_").replace(")", "_").replace("[", "_").replace("]", "_")
            statement = "ALTER TABLE {} ADD COLUMN {}".format(self.table_name, column_name)
            if datatype_combo_box.currentText() in ["INTEGER", "REAL", "TEXT", "BLOB"]:
                statement += " {}".format(datatype_combo_box.currentText())
            if null_checkbox.isChecked():
                    statement += " NOT NULL"
            if check_line_edit.text():
                check_line_edit.setText(check_line_edit.text().replace("CHECK", ""))
                statement += " CHECK {}".format(check_line_edit.text())
            if collate_combo_box.currentText() != "BINARY":
                statement += " COLLATE {}".format(collate_combo_box.currentText())
            if default_line_edit.text().strip().upper().startswith("DEFAULT"):
                default_line_edit.setText(default_line_edit.text().replace("DEFAULT", ""))
                statement += " DEFAULT {}".format(default_line_edit.text())
            column_name_line_edit.setText("")
            self.run_statement(statement)

    def run_statement(self, statement: str) -> None:
        '''
        This method will run the statement that will be passed as an argument.
        If the statement couldn't be executed, it will show a warning message with the error.
        '''
        conn = sqlite3.connect('.bin/src.db')
        with conn:
            try:
                c = conn.cursor()
                c.execute(statement)
                conn.commit()
            except Exception as e:
                dialog = QMessageBox()
                dialog.setFont(costum_font)
                dialog.warning(self, "Couldn't execute the operation", str(e))
                return False
        return True

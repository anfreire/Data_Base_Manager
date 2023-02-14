'''
    @anfreire

    linktr.ee/anfreire
'''

from Sources.imports import *
from Auxiliary.Functions import *
from Sources.init_config import get_font

'''
    This module contains the dialog that will appear when the user wants to add or edit a row in a table in the Data Base Editor.
'''

'''
Macros for the Field Dialog
Information about the macros in the class description.
'''
ADD = 1
EDIT = 2

class RowDialog(QDialog):
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
        self.setModal(True)
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
        self.buttons.buttons()[0].setFont(get_font())
        self.buttons.buttons()[1].setFont(get_font())
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
                    self.parent.scrollToItem(self.parent.item(i, j))
                    self.parent.setCurrentItem(self.parent.item(i, j), 
                        QtCore.QItemSelectionModel.SelectCurrent)
                    self.parent.setSelectionBehavior(QAbstractItemView.SelectRows)
                    show_dialog(self, "Warning", f"The value {values[self.parent.column_names[j]]} already exists in the database for the column {self.unique_columns[j]}.", get_font())
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
                show_dialog(self, "Warning", f"One of the values you are trying to insert into the database does not match the data type expected for that column. Check the data type of the columns and try again.\n info: {e}", get_font())
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
                show_dialog(self, "Warning", f"One of the values you are trying to insert into the database does not match the data type expected for that column. Check the data type of the columns and try again.\n info: {e}", get_font())
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
'''
    @anfreire

    linktr.ee/anfreire
'''

from Sources.imports import *
from Auxiliary.Functions import *
from Sources.init_config import get_font

'''
    This module contains the dialog that will appear when the user wants to add a column to a table in the Data Base Editor.
'''

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
        '''
        This method initializes the parent class (QDialog).
        Sets the dialog inteface and executes it.
        At the end are the first protection conditions to check if the SQL statement is valid.
        '''
        self.parent = parent
        self.setModal(True)
        self.table_name = str(table_name).strip().replace(" ", "_").replace("-", "_").replace(".", "_").replace("(", "_").replace(")", "_").replace("[", "_").replace("]", "_")
        self.setWindowTitle("Add Column")

        layout = QFormLayout()
        font_label = copy.copy(get_font())
        font_label.setWeight(QFont.Bold)
        font_label.setFamily("Ubuntu Thin")

        # COLUMN NAME
        column_name_line_edit = QLineEdit()
        column_name_line_edit.setFont(get_font())
        label = QLabel("Column Name")
        label.setFont(font_label)
        layout.addRow(label, column_name_line_edit)

        # NULL or NOT NULL
        null_checkbox = QCheckBox()
        null_checkbox.setFont(get_font())
        label = QLabel("NOT NULL")
        label.setFont(font_label)
        layout.addRow(label, null_checkbox)

        # DEFAULT
        default_line_edit = QLineEdit()
        default_line_edit.setFont(get_font())
        label = QLabel("DEFAULT")
        label.setFont(font_label)
        layout.addRow(label, default_line_edit)

        # CHECK
        check_line_edit = QLineEdit()
        check_line_edit.setFont(get_font())
        label = QLabel("CHECK")
        label.setFont(font_label)
        layout.addRow(label, check_line_edit)

        # COLLATE
        collate_combo_box = QComboBox()
        collate_combo_box.setFont(get_font())
        collate_combo_box.addItems(["BINARY", "NOCASE", "RTRIM"])
        label = QLabel("COLLATE")
        label.setFont(font_label)
        layout.addRow(label, collate_combo_box)
        
        # Datatype
        datatype_combo_box = QComboBox()
        datatype_combo_box.setFont(get_font())
        datatype_combo_box.addItems(["INTEGER", "REAL", "TEXT", "BLOB"])
        label = QLabel("Data Type")
        label.setFont(font_label)
        layout.addRow(label, datatype_combo_box)

        # Add buttons
        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttons.setFont(get_font())
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

    def run_statement(self, statement: str) -> bool:
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
                show_dialog(self, "warning", f"Couldn't execute the operation\ninfo: {str(e)}", get_font())
                return False
        return True
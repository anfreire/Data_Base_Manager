from imports import *
from Sources.Classes import *
from Widgets.Dialogs import *
from Sources.Functions import *
from init_config import costum_font

class Editor(Widget):
    '''
    This class is the editor window.
    '''
    def __init__(self, parent=None) -> None:
        '''
        This method initializes the editor window.
        '''
        super().__init__(parent)
        self.start_editor_widgets()
        
    def start_editor_widgets(self) -> None:
        '''
        This method sets up the editor signals and slots.
        Sets the dialog to create a table.
        It shoul't be called more than once, only when the window is initialized, in the __init__ method.
        '''    
        disconnect_button(self.ui.Add_table_button)
        self.ui.Add_table_button.clicked.connect(lambda: dialog.show())
        disconnect_button(self.ui.Add_column_button)
        self.ui.Add_column_button.clicked.connect(lambda: self.create_column())
        disconnect_button(self.ui.Remove_Table_button)
        self.ui.Remove_Table_button.clicked.connect(lambda: self.delete_table())
        disconnect_button(self.ui.Remove_column_button)
        self.ui.Remove_column_button.clicked.connect(lambda: self.delete_column())
        dialog = QDialog()
        dialog.setFont(costum_font)
        self.variable = None
        dialog.setWindowTitle("Create Table")
        self.label = QtWidgets.QLabel("Enter table name:")
        self.entry = QtWidgets.QLineEdit()
        self.button = QtWidgets.QPushButton("Create Table", clicked=self.create_table)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.entry)
        layout.addWidget(self.button)
        dialog.setLayout(layout)

    def next_window_from_editor(self) -> None:
        '''
        This method is called when the user clicks the proceed button in the editor window when its registring and it doesnt have a database.
        It calls the next window, the configuration window.
        '''
        self.setup_config()
        self.go_config()
        
    def setup_editor(self) -> None:
        '''
        This method sets up the editor window, depending on the flag flags.login and the existence of the database that contains the user loggin information.
        '''
        if check_db_files_in_folder(".bin") == True or self.flags.login == True:
            self.ui.proceed_button_editor.hide()
            disconnect_button(self.ui.return_button_confirm_email_2)
            self.ui.return_button_confirm_email_2.clicked.connect(lambda: self.go_home())
        else:
            disconnect_button(self.ui.proceed_button_editor)
            self.ui.proceed_button_editor.clicked.connect(lambda: self.next_window_from_editor())
            disconnect_button(self.ui.return_button_confirm_email_2)
            self.ui.return_button_confirm_email_2.clicked.connect(lambda: self.go_start())
        self.update_editor()

    def go_editor(self) -> None:
        '''
        This method sets the Data Base Editor as the current Page.
        '''
        self.ui.stackedWidget.setCurrentWidget(self.ui.database_editor)
        
    def update_editor(self) -> None:
        '''
        This method updates the editor window, it updates the tree widget that contains the tables and columns.
        Clears the tree widget, gets the tables from the database and adds them to the tree widget.
        Then it gets the columns from the database and adds them to the tree widget.
        When the tree widget is updated, it expands all the items.
        '''
        self.ui.treeWidget.clear()
        self.ui.treeWidget.setHeaderHidden(True)
        self.ui.treeWidget.setFont(costum_font)
        conn = sqlite3.connect(".bin/src.db")
        with conn:
            cursor = conn.cursor()
            tables = cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%';").fetchall()
            for table in tables:
                item = QTreeWidgetItem([table[0]])
                columns = cursor.execute(f"PRAGMA table_info({table[0]});").fetchall()
                for column in columns:
                    child_item = QTreeWidgetItem([column[1]])
                    item.addChild(child_item)
                self.ui.treeWidget.addTopLevelItem(item)
        self.ui.treeWidget.expandAll()
            
    def create_table(self) -> None:
        '''
        This method creates a table in the database.
        It gets the table name from the entry widget, and creates the table in the database and updates the editor. (Tree widget)
        This method contains protection against bad table names.
        '''
        table_name = self.entry.text().strip().replace(" ", "_").replace("-", "_").replace(".", "_").replace("(", "_").replace(")", "_").replace("[", "_").replace("]", "_")
        conn = sqlite3.connect(".bin/src.db")
        c = conn.cursor()
        with conn:
            try:
                c.execute(f"CREATE TABLE {table_name} ({table_name}_id INTEGER PRIMARY KEY AUTOINCREMENT)")
                conn.commit()
                dialog.close()
                self.entry.setText("")
                self.update_editor()
            except Exception as e:
                dialog = QMessageBox()
                dialog.setFont(costum_font)
                dialog.critical(self, "Error", str(e), QMessageBox.Ok)
            
    def create_column(self) -> None:
        '''
        This method creates a column in the database.
        To add a column, opens a costum the costum dialog AddColumn that contains several widgets with different options.
        It gets the table name from the tree widget, and creates the column in the database and updates the editor. (Tree widget)
        This method contains protection against bad column names.
        The user has to select a table in the tree widget, otherwise it will show an error message if the user hasnt selected anything or selected a column.
        '''
        try:
            selected_table = self.ui.treeWidget.currentItem()
            if selected_table.text(0) == "":
                dialog = QMessageBox()
                dialog.setFont(costum_font)
                dialog.critical(self, "Error", "Please select a table", QMessageBox.Ok)
                return
            elif selected_table.parent() != None:
                dialog = QMessageBox()
                dialog.setFont(costum_font)
                dialog.critical(self, "Error", "Please select a table", QMessageBox.Ok)
                return
        except:
            dialog = QMessageBox()
            dialog.setFont(costum_font)
            dialog.critical(self, "Error", "Please select a table", QMessageBox.Ok)
            return
        AddColumn(self, selected_table.text(0))
        self.update_editor()

    def delete_table(self) -> None:
        '''
        This method deletes a table in the database.
        It gets the table name from the tree widget, and deletes the table in the database and updates the editor. (Tree widget)
        The user has to select a table in the tree widget, otherwise it will show an error message if the user hasnt selected anything or selected a column.
        '''
        conn = sqlite3.connect(".bin/src.db")
        try:
            selected_table = self.ui.treeWidget.currentItem()
            if selected_table.text(0) == "":
                dialog = QMessageBox()
                dialog.setFont(costum_font)
                dialog.critical(self, "Error", "Please select a table", QMessageBox.Ok)
                return
            elif selected_table.parent() != None:
                dialog = QMessageBox()
                dialog.setFont(costum_font)
                dialog.critical(self, "Error", "Please select a table", QMessageBox.Ok)
                return
        except:
            dialog = QMessageBox()
            dialog.setFont(costum_font)
            dialog.critical(self, "Error", "Please select a table", QMessageBox.Ok)
            return
        c = conn.cursor()
        restart_question_2 = QMessageBox.question(self, 'WARNING', f"The table {selected_table.text(0)}, all its columns and values will be deleted, do you want to proceed?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if restart_question_2 == QMessageBox.Yes:
            with conn:
                try:
                    c.execute(f"DROP TABLE IF EXISTS {selected_table.text(0)}")
                    conn.commit()
                except Exception as e:
                    dialog = QMessageBox()
                    dialog.setFont(costum_font)
                    dialog.critical(self, "Error", str(e), QMessageBox.Ok)
        self.update_editor()

    def delete_column(self) -> None:
        '''
        This method deletes a column in the database.
        It gets the column name from the tree widget, and deletes the column in the database and updates the editor. (Tree widget)
        The user has to select a column in the tree widget, otherwise it will show an error message if the user hasnt selected anything or selected a table.
        '''
        conn = sqlite3.connect(".bin/src.db")
        try:
            selected_column = self.ui.treeWidget.currentItem()
            if selected_column.text(0) == "":
                dialog = QMessageBox()
                dialog.setFont(costum_font)
                dialog.critical(self, "Error", "Please select a column", QMessageBox.Ok)
                return
            elif selected_column.parent() == None:
                dialog = QMessageBox()
                dialog.setFont(costum_font)
                dialog.critical(self, "Error", "Please select a column", QMessageBox.Ok)
                return
            selected_table = selected_column.parent().text(0)
        except:
            dialog = QMessageBox()
            dialog.setFont(costum_font)
            dialog.critical(self, "Error", "Please select a column", QMessageBox.Ok)
            return
        c = conn.cursor()
        restart_question_2 = QMessageBox.question(self, 'WARNING', f"The column {selected_column.text(0)} and values will be deleted, do you want to proceed?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if restart_question_2 == QMessageBox.Yes:
            with conn:
                try:
                    c.execute(f"ALTER TABLE {selected_table} DROP COLUMN {selected_column.text(0)}")
                    conn.commit()
                except Exception as e:
                    dialog = QMessageBox()
                    dialog.setFont(costum_font)
                    dialog.critical(self, "Error", str(e), QMessageBox.Ok)
        self.update_editor()
        
        
        

'''
    @anfreire

    linktr.ee/anfreire
'''

from Sources.imports import *
from Auxiliary.Functions import *
from Auxiliary.Classes import Events
from Widgets.AddColumn import AddColumn
from Sources.init_config import get_font

'''
    This module contains the code for the Data Base Editor page.
'''

class Editor(Events):
    '''
    This class is the editor window.
    '''
    def __init__(self, parent=None) -> None:
        '''
        This method initializes the parent class and starts the editor widgets.
        '''
        super().__init__(parent)
        self.start_editor_widgets()
        self.create_table_setup()
        
    def start_editor_widgets(self) -> None:
        '''
        This method connects the buttons to the methods.
        It shoul't be called more than once, only when the window is initialized, in the __init__ method.
        '''
        Add_Menu = QMenu(self.ui.Editor)
        Add_Menu.setFont(get_font())
        Action_AT = QAction("Add Table", self.ui.Editor)
        Action_AT.setFont(get_font())
        Action_AT.triggered.connect(lambda: self.create_table())
        Add_Menu.addAction(Action_AT)
        Action_AC = QAction("Add Column", self.ui.Editor)
        Action_AC.setFont(get_font())
        Action_AC.triggered.connect(lambda: self.create_column())
        Add_Menu.addAction(Action_AC)
        self.ui.button_add_editor.setMenu(Add_Menu)
        Remove_Menu = QMenu(self.ui.Editor)
        Remove_Menu.setFont(get_font())
        Action_RT = QAction("Remove Table", self.ui.Editor)
        Action_RT.setFont(get_font())
        Action_RT.triggered.connect(lambda: self.delete_table())
        Remove_Menu.addAction(Action_RT)
        Action_RC = QAction("Remove Column", self.ui.Editor)
        Action_RC.setFont(get_font())
        Action_RC.triggered.connect(lambda: self.delete_column())
        Remove_Menu.addAction(Action_RC)
        self.ui.button_remove_editor.setMenu(Remove_Menu)

    def next_window_from_editor(self) -> None:
        '''
        This method is called when the user clicks the proceed button in the editor window when its registring and it doesnt have a database.
        It calls the next window, the configuration window, that its the only navigation available for a user that is registering.
        '''
        self.setup_config()
        self.go_config()
        
    def setup_editor(self) -> None:
        '''
        This method sets up the editor window, depending on the flag flags.login and the existence of the database that contains the user loggin information.
        '''
        if check_db_files_in_folder(".bin") == True or self.flags.login == True:
            self.ui.button_proceed_editor.hide()
            disconnect_button(self.ui.button_return_editor).connect(lambda: self.return_tables())
        else:
            disconnect_button(self.ui.button_proceed_editor).connect(lambda: self.next_window_from_editor())
            disconnect_button(self.ui.button_return_editor).connect(lambda: self.go_start())
        self.update_editor()

    def go_editor(self) -> None:
        '''
        This method sets the Data Base Editor as the current Page.
        '''
        self.ui.treeWidget.setFont(get_font())
        self.ui.stackedWidget.setCurrentWidget(self.ui.Editor)
        
    def return_tables(self) -> None:
        '''
        This method returns to the tables window, that is the only navigation allowed from a registor user.
        '''
        self.open_database()
        self.go_tables()
        
    def update_editor(self) -> None:
        '''
        This method updates the editor window, it updates the tree widget that contains the tables and columns.
        Clears the tree widget, gets the tables from the database and adds them to the tree widget.
        Then it gets the columns from the database and adds them to the tree widget.
        When the tree widget is updated, it expands all the items.
        '''
        self.ui.treeWidget.clear()
        self.ui.treeWidget.setHeaderHidden(True)
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
    
    def create_table_setup(self) -> None:
        '''
        This method setups the dialog window that is used to create a table.
        More information about the dialog window in the method create_table.
        '''
        self.dialog = QDialog()
        self.dialog.setModal(True)
        self.dialog.setFont(get_font())
        self.dialog.setWindowTitle("Create Table")
        self.label = QtWidgets.QLabel("Enter table name:")
        self.entry = QtWidgets.QLineEdit()
        self.button = QtWidgets.QPushButton("Create Table", clicked=self.create_table_aux)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.entry)
        layout.addWidget(self.button)
        self.dialog.setLayout(layout)
        
    def create_table(self) -> None:
        '''
        This method displays the dialog window that is used to create a table.
        The dialog button its previously connected to the method create_table_aux, that creates the table in the database.
        '''
        self.dialog.show()
    
    def create_table_aux(self) -> None:
        '''
        This method creates a table in the database.
        It gets the table name from the method create_table, that creates a dialog window with the widgets to get the table name.
        This method contains protection against bad table names.
        After creating the table, it closes the dialog window, clears the entry widget and updates the editor window.
        '''
        table_name = self.entry.text().strip().replace(" ", "_").replace("-", "_").replace(".", "_").replace("(", "_").replace(")", "_").replace("[", "_").replace("]", "_")
        conn = sqlite3.connect(".bin/src.db")
        c = conn.cursor()
        with conn:
            try:
                c.execute(f"CREATE TABLE {table_name} ({table_name}_id INTEGER PRIMARY KEY AUTOINCREMENT)")
                conn.commit()
                self.dialog.close()
                self.update_editor()
            except Exception as e:
                show_dialog(self, "Error", f"info: {str(e)}", get_font())
            self.entry.setText("")
            
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
            if selected_table.text(0) == "" or selected_table.parent() != None:
                show_dialog(self, "Error", "Please select a table", get_font())
                return
        except:
            show_dialog(self, "Error", "Please select a table", get_font())
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
            if selected_table.text(0) == "" or selected_table.parent() != None:
                show_dialog(self, "Error", "Please select a table", get_font())
                return
        except:
            show_dialog(self, "Error", "Please select a table", get_font())
            return
        c = conn.cursor()
        confirm_dialog = show_question(self,  "warning", f"The table {selected_table.text(0)} and all its data will be deleted. Are you sure you want to delete this table?", get_font())
        if confirm_dialog.exec_() == True:
            with conn:
                try:
                    c.execute(f"DROP TABLE IF EXISTS {selected_table.text(0)}")
                    conn.commit()
                except Exception as e:
                    show_dialog(self, "Error", f"info: {str(e)}", get_font())
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
            if selected_column.text(0) == "" or selected_column.parent() == None:
                show_dialog(self, "Error", "Please select a column", get_font())
                return
            selected_table = selected_column.parent().text(0)
        except:
            show_dialog(self, "Error", "Please select a column", get_font())
            return
        c = conn.cursor()
        restart_question_2 = show_question(self,  "warning", f"The column {selected_column.text(0)} and values will be deleted, do you want to proceed?", get_font())
        if restart_question_2 == True:
            with conn:
                try:
                    c.execute(f"ALTER TABLE {selected_table} DROP COLUMN {selected_column.text(0)}")
                    conn.commit()
                except Exception as e:
                    show_dialog(self, "Error", f"info: {str(e)}", get_font())
        self.update_editor()
        
        
        

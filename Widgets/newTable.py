'''
    @anfreire

    linktr.ee/anfreire
'''

from Sources.imports import *
from Auxiliary.Functions import *
from Widgets.RowDialog import RowDialog
from Sources.init_config import get_font
from Widgets.ShortcutDialog import ShortcutDialog

'''
    This module contains the code for the new table widget.
    It will be used in the newTab widget.
'''

class newTable(QtWidgets.QTableWidget):
    '''
    This class creates a new table.
    The methods of this class mainly consist in sqlite3 commands and in signals and slots handling.
    '''
    def __init__(self, data, widgets, parent=None) -> None:
        super().__init__(parent)
        '''
        This method initializes the table with the data received as argument.
        '''
        self.parent = parent
        self.setup_vars(widgets, data)
        self.setup_table()
        self.connect_signals()
        self.add_actions()
        self.update_table()
        self.set_table()
        self.get_unique_columns()
        self.horizontalHeader().setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.horizontalHeader().setStretchLastSection(True)
        list_widgets = self.get_header_items()
        list_widgets.append(self.horizontalHeader())
        list_widgets.append(self.verticalHeader())
        self.widgets_table = get_initial_fonts_widgets(list_widgets)
        self.parent.tabWidgets.append(self.widgets_table)
        self.parent.resize_event_functions.append(self.resizeEvent_Table)
        
    def resizeEvent_Table(self, event: QResizeEvent) -> None:
        '''
        This function is called when the new tab widget is resized to resize the widgets.
        '''
        for widget in self.widgets_table.values():
            try:
                point_per_width = self.parent.initial_width / widget["initial_font"].pointSizeF()
                new_font = widget['widget'].font()
                new_font_size = (self.parent.width() / point_per_width)
                if int(new_font_size) > int(widget["initial_font"].pointSizeF()):
                    new_font_size = new_font_size * euler_function(new_font_size - widget["initial_font"].pointSizeF())
                new_font.setPointSizeF(new_font_size)
                widget['widget'].setFont(new_font)
            except:
                continue
        self.resizeColumnsToContents()
        self.resizeRowsToContents()
        self.horizontalHeader().setStretchLastSection(True)

    def get_header_items(self) -> list:
        header_items = []
        
        for i in range(self.columnCount()):
            header_items.append(self.horizontalHeaderItem(i))
            
        for i in range(self.rowCount()):
            header_items.append(self.verticalHeaderItem(i))
            
        return header_items

    def get_unique_columns(self) -> None:
        '''
        This method gets the unique columns.
        '''
        conn = sqlite3.connect(".bin/src.db")
        with conn:
            c = conn.cursor()
            query = f"PRAGMA table_info({self.sheet_name})"
            c.execute(query)
            column_info = c.fetchall()
            self.unique_columns = [info[1] for info in column_info if info[3] == 1]

    def setup_vars(self, widgets, data) -> None:
        '''
        This method initializes the variables.
        '''
        self.column_types = []
        self.sheet_data, self.sheet_name, self.table_name, self.column_names, self.column_info = data
        self.get_columns_types()
        self.search_input, self.combo_box, self.search_button, self.add_button = widgets

    def setup_table(self) -> None:
        '''
        This method sets the table.
        '''
        self.setColumnCount(0)
        self.setRowCount(0)
        self.column_type = []

    def connect_signals(self) -> None:
        '''
        This method connects the signals and slots.
        '''
        self.add_button.clicked.connect(lambda:RowDialog(parent=self).add_row_signal())
        self.search_button.clicked.connect(lambda:self.search())

    def add_actions(self) -> None:
        '''
        This method adds the actions to the right click menu.
        '''
        self.cellClicked.connect(lambda: self.showContextMenu())
        self.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.delete_row = QAction("Delete Row", self)
        self.delete_row.triggered.connect(self.delete_row_function)
        self.addAction(self.delete_row)
        self.edit_row = QAction("Edit Row", self)
        self.addAction(self.edit_row)
        self.edit_row.triggered.connect(self.edit_row_function)
        self.increase_font_size = QAction("Increase Font Size", self)
        self.increase_font_size.triggered.connect(self.increase_font_size_func)
        self.increase_font_size.setShortcutVisibleInContextMenu(False)
        self.addAction(self.increase_font_size)
        self.decrease_font_size = QAction("Decrease Font Size", self)
        self.decrease_font_size.triggered.connect(self.decrease_font_size_func)
        self.decrease_font_size.setShortcutVisibleInContextMenu(False)
        self.addAction(self.decrease_font_size)
        self.update_shortcuts()
        action = self.parentWidget().ui.menuSettings.actions()[3]
        action.triggered.disconnect()
        action.triggered.connect(lambda:self.change_shortcuts())

    def change_shortcuts(self):
        '''
        This method opens a dialog to set the shortcuts of the table.
        '''
        dialog = ShortcutDialog(self)
        dialog.setModal(True)
        dialog.setFont(get_font())
        dialog.exec_()
        if dialog.result() == 1:
            parent = self.parentWidget().parent.ui.tabWidget
            for i in range(parent.count()):
                table = parent.widget(i).findChild(newTable)
                table.update_shortcuts()

    def update_shortcuts(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        key_1 = config['DEFAULT']['Shortcut +']
        key_2 = config['DEFAULT']['Shortcut -']
        self.increase_font_size.setShortcut(QtGui.QKeySequence(key_1))
        self.decrease_font_size.setShortcut(QtGui.QKeySequence(key_2))
    
    def increase_font_size_func(self) -> None:
        '''
        This method increases the font size.
        It is called when the user presses the shortcut key. (CTRL + +)
        Resizes the columns and rows to fit the contents.
        Resizes the header to fit the contents.
        Sets the font size to the header.
        '''
        font = self.font()
        font.setPointSize(font.pointSize() + 1)
        self.setFont(font)
        self.horizontalHeader().setFont(font)
        self.resizeColumnsToContents()
        self.resizeRowsToContents()
        for header_item in enumerate(self.column_names):
            self.horizontalHeaderItem(header_item[0]).setFont(font)

    def decrease_font_size_func(self) -> None:
        '''
        This method decreases the font size.
        It is called when the user presses the shortcut key. (CTRL + -)
        Resizes the columns and rows to fit the contents.
        Resizes the header to fit the contents.
        Sets the font size to the header.
        '''
        font = self.font()
        font.setPointSize(font.pointSize() - 1)
        self.setFont(font)
        self.resizeColumnsToContents()
        self.resizeRowsToContents()
        for header_item in enumerate(self.column_names):
            self.horizontalHeaderItem(header_item[0]).setFont(font)

    def edit_row_function(self) -> None:
        '''
        This method edits adds row, from the right click menu.
        Opens the FieldDialog class.
        '''
        RowDialog(self).edit_row_signal()

    def get_row_id_in_db(self) -> None:
        '''
        This method gets the row id in the database.
        '''
        conn = sqlite3.connect('.bin/src.db')
        with conn:
            cursor = conn.cursor()
            selected_row = self.currentRow()
            selected_row_data = self.sheet_data[selected_row]
            selected_columns = [selected_row_data[self.column_names.index(column_name)] for column_name in self.column_names]
            conditions = []
            values = []
            for column_name, value in zip(self.column_names, selected_columns):
                if value == None:
                    conditions.append(f"{column_name} IS NULL")
                else:
                    conditions.append(f"{column_name}=?")
                    values.append(value)
            select_id_statement = f"SELECT rowid FROM {self.table_name} WHERE " + " AND ".join(conditions)
            cursor.execute(select_id_statement, values)
            self.row_id = cursor.fetchone()[0]

    def delete_row_function(self) -> None:
        '''
        This method deletes a row, from the right click menu.
        '''
        conn = sqlite3.connect('.bin/src.db')
        values_tmp = []
        for i in range(self.columnCount()):
            values_tmp.append(self.item(self.currentRow(), i).text())
        restart_question_2 = show_question(self,  "warning", f"The row containing this values: {str(values_tmp)} will be deleted, do you want to proceed?", get_font())
        if restart_question_2 == True:
            if self.rowCount() == 1:
                show_dialog(self, "error", "If you want to delete the table, please delete it in the Data Base Editor. If you want to delete the row, please add a new row first.", get_font())
                return
            with conn:
                cursor = conn.cursor()
                selected_row = self.currentRow()
                selected_row_data = self.sheet_data[selected_row]
                selected_columns = [selected_row_data[self.column_names.index(column_name)] for column_name in self.column_names]
                delete_statement = "DELETE FROM {} WHERE ".format(self.table_name)
                conditions = []
                values = []
                for column_name, value in zip(self.column_names, selected_columns):
                    if value == None:
                        conditions.append(f"{column_name} IS NULL")
                    else:
                        conditions.append(f"{column_name}=?")
                        values.append(value)
                delete_statement += " AND ".join(conditions)
                cursor.execute(delete_statement, values)
                conn.commit()
        self.update_table()

    def set_table(self) -> None:
        '''
        This method initializes the table.
        Its called when the table is created, from the init method.
        To update the table, use the update_table method.
        '''
        try:
            self.combo_box.clear()
            self.setRowCount(len(self.sheet_data))
            self.setColumnCount(len(self.sheet_data[0]))
            self.setHorizontalHeaderLabels(self.sheet_name)
            self.combo_box.addItem("All")
            table_font = copy.copy(get_font())
            self.setFont(table_font)
            for i, row in enumerate(self.sheet_data):
                for j, item in enumerate(row):
                    header_font = copy.copy(get_font())
                    header_font.setBold(True)
                    header_font.setPointSize(header_font.pointSize() + 2)
                    self.setItem(i, j, QTableWidgetItem(str(item)))
                    if i == 0:
                        self.setHorizontalHeaderItem(j, QTableWidgetItem(self.column_names[j]))
                        self.horizontalHeaderItem(j).setFont(header_font)
                        self.combo_box.addItem(self.column_names[j])
                    if j == 0:
                        self.setVerticalHeaderItem(i, QTableWidgetItem(str(i + 1)))
                        self.verticalHeaderItem(i).setFont(header_font)
                        
        except Exception as e:
            show_dialog(self, "error", f"Error: {self.sheet_name}", get_font())
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.resizeColumnsToContents()
        self.resizeRowsToContents()
        self.horizontalHeader().setStretchLastSection(True)

    def update_table(self) -> None:
        '''
        This method updates the table values.
        '''
        self.clear()
        conn = sqlite3.connect('.bin/src.db')
        with conn:
            c = conn.cursor()
            c.execute(f"SELECT * from {self.sheet_name};")
            self.sheet_data = c.fetchall()
            self.table_name = self.sheet_name
            self.column_names = [i[0] for i in c.description]
            self.column_info = [{"name": i[0], "type": type(i[0]).__name__} for i in c.description]
            self.set_table()

    def search(self) -> None:
        '''
        This method searches for a value in the table.
        If the value is found, it scrolls to the cell and selects it.
        If called again, it will search for the next value.
        Its connected to the search button.
        '''
        previous_row, previous_column = self.currentRow(), self.currentColumn()
        start_row = (previous_row + 1) % self.rowCount()
        for i in range(start_row, self.rowCount()):
            if self.combo_box.currentText() == "All" or self.combo_box.currentText() == "":
                for j in range(self.columnCount()):
                    if self.search_input.text().lower() in self.item(i, j).text().lower():
                        self.setSelectionBehavior(QAbstractItemView.SelectItems)
                        self.scrollToItem(self.item(i, j))
                        self.setCurrentItem(self.item(i, j), 
                            QtCore.QItemSelectionModel.SelectCurrent)
                        self.setSelectionBehavior(QAbstractItemView.SelectRows)
                        return
            else:
                j = self.column_names.index(self.combo_box.currentText())
                if self.search_input.text().lower() in self.item(i, j).text().lower():
                    self.setSelectionBehavior(QAbstractItemView.SelectItems)
                    self.scrollToItem(self.item(i, j))
                    self.setCurrentItem(self.item(i, j), 
                        QtCore.QItemSelectionModel.SelectCurrent)
                    self.setSelectionBehavior(QAbstractItemView.SelectRows)
                    return
        for i in range(0, previous_row):
            if self.combo_box.currentText() == "All" or self.combo_box.currentText() == "":
                for j in range(self.columnCount()):
                    if self.search_input.text().lower() in self.item(i, j).text().lower():
                        self.setSelectionBehavior(QAbstractItemView.SelectItems)
                        self.scrollToItem(self.item(i, j))
                        self.setCurrentItem(self.item(i, j), 
                            QtCore.QItemSelectionModel.SelectCurrent)
                        self.setSelectionBehavior(QAbstractItemView.SelectRows)
                        return
            else:
                j = self.column_names.index(self.combo_box.currentText())
                if self.search_input.text().lower() in self.item(i, j).text().lower():
                    self.setSelectionBehavior(QAbstractItemView.SelectItems)
                    self.scrollToItem(self.item(i, j))
                    self.setCurrentItem(self.item(i, j), 
                        QtCore.QItemSelectionModel.SelectCurrent)
                    self.setSelectionBehavior(QAbstractItemView.SelectRows)
                    return
        show_dialog(self, "info", f"Could not find {self.search_input.text()} in {self.sheet_name}", get_font())
        return

    def showContextMenu(self) -> None:
        '''
        This method is auxilary to the right click menu.
        '''
        self.setCurrentCell(self.currentRow(), self.currentColumn())

    def get_columns_types(self) -> None:
        '''
        This method "translates" the column types from sqlite3 to human readable, to present to user when adding or editing a row.
        '''
        for column in self.column_info:
            if column[2] == "NULL":
                self.column_types.append("NULL value")
            elif column[2] == "INTEGER":
                self.column_types.append("Whole Number")
            elif column[2] == "REAL":
                self.column_types.append("Decimal Number")
            elif column[2] == "TEXT":
                self.column_types.append("Text")
            elif column[2] == "BLOB":
                self.column_types.append("Binary Data")
            elif column[2].startswith("NVARCHAR"):
                max_length = column[2].split("(")[1].split(")")[0]
                self.column_types.append(f"Text (Maximum {max_length} Characters)")
            else:
                self.column_types.append("Unknown data type")

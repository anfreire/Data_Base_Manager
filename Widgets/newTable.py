from imports import *
from Widgets.Dialogs import *
from init_config import costum_font

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
        self.setup_vars(widgets, data)
        self.setup_table()
        self.connect_signals()
        self.add_actions()
        self.update_table()
        self.set_table()
        self.get_unique_columns()
        self.horizontalHeader().setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.horizontalHeader().setStretchLastSection(True)

    def get_unique_columns(self):
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
        self.add_button.clicked.connect(lambda:FieldDialog(parent=self).add_row_signal())
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
        self.increase_font_size.setShortcut(QtGui.QKeySequence.ZoomIn)
        self.increase_font_size.triggered.connect(self.increase_font_size_func)
        self.addAction(self.increase_font_size)
        self.decrease_font_size = QAction("Decrease Font Size", self)
        self.decrease_font_size.setShortcut(QtGui.QKeySequence.ZoomOut)
        self.decrease_font_size.triggered.connect(self.decrease_font_size_func)
        self.addAction(self.decrease_font_size)

    def increase_font_size_func(self) -> None:
        '''
        This method increases the font size.
        It is called when the user presses the shortcut key. (CTRL + +)
        '''
        font = self.font()
        font.setPointSize(font.pointSize() + 1)
        self.setFont(font)

    def decrease_font_size_func(self) -> None:
        '''
        This method decreases the font size.
        It is called when the user presses the shortcut key. (CTRL + -)
        '''
        font = self.font()
        font.setPointSize(font.pointSize() - 1)
        self.setFont(font)

    def edit_row_function(self) -> None:
        '''
        This method edits adds row, from the right click menu.
        Opens the FieldDialog class.
        '''
        FieldDialog(self).edit_row_signal()

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
        restart_question_2 = QMessageBox.question(self, 'WARNING', f"The row containing this values: {str(values_tmp)} will be deleted, do you want to proceed?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if restart_question_2 == QMessageBox.Yes:
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
            for i, row in enumerate(self.sheet_data):
                for j, item in enumerate(row):
                    self.setItem(i, j, QTableWidgetItem(str(item)))
                    if i == 0:
                        self.setHorizontalHeaderItem(j, QTableWidgetItem(self.column_names[j]))
                        self.combo_box.addItem(self.column_names[j])
        except Exception as e:
            dialog = QMessageBox()
            dialog.setFont(costum_font)
            dialog.critical(self, "Error", f"Error: {self.sheet_name}\n{e}")
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
        dialog = QMessageBox()
        dialog.setFont(costum_font)
        dialog.information(self, "Search", f"Could not find {self.search_input.text()} in {self.sheet_name}", QMessageBox.Ok)
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

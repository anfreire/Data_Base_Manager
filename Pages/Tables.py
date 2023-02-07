from imports import *
from Sources.Classes import *
from Widgets.newTab import newTab
from init_config import costum_font

class Tables(Widget):
    '''
    This class is the tables in the database Window.
    '''
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        '''
        This method initializes the parent class.
        '''

    def open_database(self) -> None:
        '''
        This method loads the database and adds the tables to the table widget.
        '''
        conn = sqlite3.connect(".bin/src.db")
        with conn:
            c = conn.cursor()
            c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%';")
            tables = c.fetchall()
            data = {}
            progress = QProgressDialog("Loading [1/2] ", "Cancel", 0, len(tables), self)
            progress.setWindowTitle("Loading [1/2] ")
            progress.setWindowModality(Qt.WindowModal)
            progress.setMinimumDuration(100)
            progress.setGeometry(50, 50, 400, 150)
            progress.setFont(costum_font)
            progress.show()
            for i, table_name in enumerate(tables):
                progress.setValue(i + 1)
                QApplication.processEvents()
                if progress.wasCanceled():
                    break
                progress.setLabelText(f"Loading table {table_name[0]}...")
                c.execute(f"PRAGMA table_info({table_name[0]});")
                column_info = c.fetchall()
                column_names = [column[1] for column in column_info]
                c.execute(f"SELECT * from {table_name[0]};")
                sheet_data = c.fetchall()
                data[table_name[0]] = (sheet_data, table_name[0], column_names, column_info)
            progress.close()
            progress = QProgressDialog("Processing [2/2] ", "Cancel", 0, len(data))
            progress.setFont(costum_font)
            progress.setWindowTitle("Processing [2/2] ")
            progress.setWindowModality(Qt.WindowModal)
            progress.setMinimumDuration(0)
            progress.setGeometry(50, 50, 400, 150)
            progress.show()
            for index, (sheet_name, sheet_info) in enumerate(data.items()):
                progress.setValue(index + 1)
                QApplication.processEvents()
                if progress.wasCanceled():
                    break
                label = QLabel(f"Processing table {sheet_name}...", self)
                label.setWordWrap(True)
                label.setAlignment(Qt.AlignCenter)
                label.setFont(costum_font)
                progress.setLabel(label)
                sheet_data, table_name, column_names, column_info = sheet_info
                new_data = (sheet_data, sheet_name, table_name, column_names, column_info)
                self.ui.tabWidget.addTab(newTab(new_data, self), table_name)
 
    
    def go_tables(self) -> None:
        '''
        This method goes to the tables window.
        '''
        self.set_middle_table_close_event()
        self.ui.stackedWidget.setCurrentWidget(self.ui.home)
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.tables)
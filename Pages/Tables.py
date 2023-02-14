'''
    @anfreire

    linktr.ee/anfreire
'''

from Sources.imports import *
from Auxiliary.Functions import *
from Auxiliary.Classes import Events
from Sources.init_config import get_font
from Widgets.newTab import newTab

'''
    This module contains the Database Tables page.
'''

class Tables(Events):
    '''
    This class is the tables in the database Window.
    '''
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        '''
        This method initializes the parent class.
        '''
    
    def resize_event_tabs(self, event) -> None:
        '''
        This method resizes the tabs when the window is resized.
        Its called after setting the tabs.  
        '''
        previous_font_size = 20
        point_per_with = self.initial_width / previous_font_size
        for i in range(self.ui.tabWidget.count()):
            tab_widget_font = copy.copy(get_font())
            new_font_size = (self.width() / point_per_with)
            if int(new_font_size) > int(previous_font_size):
                new_font_size = new_font_size * euler_function(new_font_size - previous_font_size)
            tab_widget_font.setPointSize(new_font_size)
            self.ui.tabWidget.tabBar().setFont(tab_widget_font)

    def open_database(self) -> None:
        '''
        This method loads the database and adds the tables to the table widget.
        Adds the table data to the table widget.
        Adds the resize events to the program resize event.
        '''
        conn = sqlite3.connect(".bin/src.db")
        self.ui.tabWidget.clear()
        self.tabBar_widgets = []
        with conn:
            c = conn.cursor()
            c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%';")
            tables = c.fetchall()
            data = {}
            progress = QProgressDialog("Loading [1/2] ", "Cancel", 0, len(tables), self)
            progress.setModal(True)
            progress.setWindowTitle("Loading [1/2] ")
            progress.setWindowModality(Qt.WindowModal)
            progress.setMinimumDuration(100)
            progress.setGeometry(50, 50, 400, 150)
            progress.setFont(get_font())
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
            progress.setModal(True)
            progress.setFont(get_font())
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
                label.setFont(get_font())
                progress.setLabel(label)
                sheet_data, table_name, column_names, column_info = sheet_info
                new_data = (sheet_data, sheet_name, table_name, column_names, column_info)
                tab_bar_font = copy.copy(get_font())
                tab_bar_font.setPointSize(20)
                self.ui.tabWidget.tabBar().setFont(tab_bar_font)
                self.ui.tabWidget.addTab(newTab(new_data, self), table_name)
                self.tabBar_widgets.append(self.ui.tabWidget.tabBar())
            self.resize_event_functions.append(self.resize_event_tabs)
        self.tabWidgets.append(get_initial_fonts_widgets(self.tabBar_widgets))
 
    def go_tables(self) -> None:
        '''
        This method goes to the tables window.
        Enables the actions menu.
        '''
        self.set_middle_table_close_event()
        self.ui.stackedWidget.setCurrentWidget(self.ui.Tables)
        self.turn_on_actions_menu()
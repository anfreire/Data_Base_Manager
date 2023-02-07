from imports import *
from Pages.Home import Home
from Pages.Start import Start
from Pages.Login import Login
from Pages.Editor import Editor
from Pages.Tables import Tables
from Pages.Config import Config
from Sources.Functions import *
from Pages.Confirm_Email import Confirm_Email


class DataBase(Start, Config, Login, Confirm_Email, Tables, Home, Editor):
    '''
    This class is the main class of the program.
    '''
    def __init__(self, parent=None):
        '''
        This is the constructor of the class.
        '''
        super().__init__(parent)
        self.choose_window()
        
    def choose_window(self) -> None:
        '''
        This function is used to choose the window to be shown.
        It selects if the window will go to login or will register the database.
        Its based on the existence of the database files.
        '''
        if check_db_files_in_folder(".bin"):
            self.set_default_close_event()
            self.setup_login()
            self.go_login()
        else:
            self.set_middle_config_close_event()
            self.go_start()

if __name__ == "__main__":
    # SETS THE THEME BASED ON THE CONFIG FILE
    config = configparser.ConfigParser()
    config.read('config.ini')
    current_theme = config['DEFAULT']['current_theme']
    app = QApplication(sys.argv)
    widget = DataBase()
    qdarktheme.setup_theme(current_theme)
    widget.show()
    sys.exit(app.exec())
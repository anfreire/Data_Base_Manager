'''
    @anfreire

    linktr.ee/anfreire
'''

from Sources.imports import *
from Pages.Login import Login
from Pages.Start import Start
from Pages.Editor import Editor
from Pages.Tables import Tables
from Pages.Config import Config
from Auxiliary.Functions import *
from Widgets.MenuBar import MenuBar
from Pages.ConfirmEmail import ConfirmEmail

'''
    This is the brain of the program.
'''

class DataBase(Login, Start, Editor, Tables, Config, ConfirmEmail, MenuBar):
    '''
    This class is the main class of the program.
    It is used to choose the window to be shown.
    Puts together all the pages of the program.
    '''
    def __init__(self, parent=None):
        '''
        This is the constructor of the parent classes (Pages) and the class itself.
        '''
        super().__init__(parent)
        self.choose_window()
        
    def choose_window(self) -> None:
        '''
        This function is used to choose the window to be shown.
        It selects if the window will go to login or will register the database.
        Its based on the existence of the database files in the folder ".bin".
        '''
        if check_db_files_in_folder(".bin"):
            self.set_default_close_event()
            self.setup_login()
            self.go_login()
        else:
            self.set_middle_config_close_event()
            self.go_start()
            
if __name__ == "__main__":
    '''
    This is the main function of the program.
    The program starts here.
    First, it check if there is a pending file to be deleted, in case the program was closed unexpectedly in the previous session.
    Then, loads the theme from the configuration file, starts the proram and sets the theme.
    '''
    if check_invisible_file('pending_delete'):
        remove_folder('.bin')
    config = configparser.ConfigParser()
    config.read('config.ini')
    current_theme = config['DEFAULT']['current_theme']
    app = QApplication(sys.argv)
    widget = DataBase()
    qdarktheme.setup_theme(current_theme)
    widget.show()
    sys.exit(app.exec())
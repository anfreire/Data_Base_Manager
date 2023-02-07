from imports import *
from Sources.Functions import *
from init_config import costum_font
from Sources.ui_form import Ui_Widget


class Flags:
    '''
    This class contains the flags that are used in this project.
    '''
    def __init__(self) -> None:
        '''
        This method initializes the flags.
        '''
        self.email_added = False
        self.email_confirmed = False
        self.db_file_added = False
        self.users_added = False
        self.encrypt_db = True
        self.create_db = False
        self.recover = False
        self.login = False


    def reset(self) -> None:
        '''
        This method resets the flags.
        '''
        self.email_added = False
        self.db_file_added = False
        self.users_added = False
        self.encrypt_db = True
        self.create_db = False
        

class Data:
    '''
    This class contains the data that is used in this project.
    '''
    def __init__(self) -> None:
        '''
        This method initializes the data.
        '''
        self.users = []
        self.passwrds = []
        self.code = ""
        self.email = ""
        self.config = 'T'

    def get_values(self) -> dict:
        '''
        This method returns the data as a dictionary.
        '''
        return self.__dict__
    
    def update_values(self, data: dict) -> None:
        '''
        This method updates the data with the data from the dictionary received as argument.
        '''
        for key, value in data.items():
            if key in ['users', 'passwrds']:
                value = ast.literal_eval(value)
            setattr(self, key, value)
    
    def reset(self) -> None:
        '''
        This method resets the data.
        '''
        self.users = []
        self.passwrds = []
        self.code = ""
        self.email = ""
        self.config = 'T'
        
    def generate_code(self) -> None:
        '''
        This method generates a random code that is used to encrypt the database and to recover the acess to the database.
        The code is 8 characters long and contains only letters.
        '''
        self.code = ''.join(random.choices(string.ascii_letters, k=8)) 
            

class Widget(QWidget):
    '''
    This class contains the methods that are used in all the pages, and all the pages inherit from this class.
    '''
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        '''
        This method initializes the widget.
        Creates the ui, the data objects and the flags objects that are used in this project.
        '''
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.data = Data()
        self.flags = Flags()
        
        
    def defaultCloseEvent(self, event) -> None:
        '''
        This method is called when the user clicks on the close button of the window.
        '''
        event.accept()
        
        
    def set_default_close_event(self) -> None:
        '''
        This method sets the default close event.
        '''
        self.closeEvent = lambda event: self.defaultCloseEvent(event)
        
        
    def register_CloseEvent(self, event) -> None:
        '''
        This method is called when the user clicks on the close button of the window.
        Removes the .bin folder created by the program in the register process, in case the user closes the window before finishing the process.
        '''
        remove_folder(".bin")
        event.accept()

    
    def recover_CloseEvent(self, event) -> None:
        '''
        This method is called when the user clicks on the close button of the window when recovering the password.
        '''
        dialog = QMessageBox()
        dialog.setFont(costum_font)
        dialog.warning(self, "Warning", "Don't close the window while recovering your password, it may cause data loss.\n Finish the process or come back to the login page.", QMessageBox.Ok)
        event.ignore()
        
        
    def table_CloseEvent(self, event) -> None:
        '''
        This method is called when the user clicks on the close button of the window, to encrypt the data before closing the window.
        '''
        self.data.update_values(retrieve_from_db())
        if self.data.config == 'T':
            encrypt_database(self.data)
        event.accept()
        
        
    def set_middle_recovery_close_event(self) -> None:
        '''
        This method sets the middle recovery close event.
        '''
        self.closeEvent = lambda event: self.recover_CloseEvent(event)


    def set_middle_config_close_event(self) -> None:
        '''
        This method sets the middle config close event.
        '''
        self.closeEvent = lambda event: self.register_CloseEvent(event)
        
        
    def set_middle_table_close_event(self) -> None:
        '''
        This method sets the middle database operations close event.
        '''
        self.closeEvent = lambda event: self.table_CloseEvent(event)
        
        

        
        
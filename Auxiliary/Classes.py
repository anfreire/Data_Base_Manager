'''
    @anfreire

    linktr.ee/anfreire
'''

from Sources.imports import *
from Auxiliary.Functions import *
from Sources.ui_form import Ui_MainWindow

'''
    This module contains the classes that are used in this project.
'''

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


class Events(QMainWindow):
    '''
    This class contains the methods that are used in all the pages, and all the pages inherit from this class.
    Assembles the data and the flags objects.
    Most of the events are in this class.
    The events are extremely important in this project, because they are used to update the ui, as well sets the behavior of the program when the user closes the window in the middle of a process.
    '''
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        '''
        This method initializes the widget.
        Creates the ui, the data objects and the flags objects that are used in this project.
        '''
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.main_window = self.ui.main_window
        self.data = Data()
        self.flags = Flags()
        self.get_values_resize_event()

    def update_events(self) -> None:
        '''
        This method updates the pending events of the application and for the tabWidget, if it exists.
        '''
        QApplication.processEvents()
        self.main_window.update()
        self.update()
        children = self.findChildren(QWidget, "newTab", Qt.FindChildrenRecursively)
        for child in children:
            child.update()
            child.tableWidget.update()

    def get_values_resize_event(self) -> None:
        '''
        This method gets the initial values of the widgets that are used in the resizeEvent method.
        '''
        self.initial_width = self.width()
        self.labels = {}
        for i in range(1, 17):
            label = getattr(self.ui, f"label_{i}")
            self.labels[i] = {"widget": label, "initial_font": label.font()}
        self.buttons_list = [self.ui.button_proceed_config, self.ui.button_proceed_confirm_email, self.ui.button_proceed_editor, self.ui.button_proceed_login, self.ui.button_proceed_start, self.ui.button_reset_confirm_email, self.ui.button_remove_editor, self.ui.button_add_editor, self.ui.button_recover_login]
        self.button_icons = [self.ui.button_return_login, self.ui.button_return_config, self.ui.button_return_editor, self.ui.button_return_config, self.ui.button_add_config, self.ui.button_password_login, self.ui.button_browse_config, self.ui.button_browse_config]
        self.widget_list = [self.ui.treeWidget, self.ui.listWidget, self.ui.input_email_config, self.ui.input_email_confirm_email, self.ui.input_password_login, self.ui.input_user_login, self.ui.input_email_confirm_email, self.ui.input_user_login, self.ui.menubar,self.ui.menuData_Base, self.ui.menuSettings]
        self.buttons = get_initial_fonts_widgets(self.buttons_list)
        self.icons = {}
        self.widgets = get_initial_fonts_widgets(self.widget_list)
        for i, button in enumerate(self.button_icons):
            self.icons[i] = {"button": button, "initial_icon_width": button.iconSize().width()}
        self.resize_event_functions = []
        self.resize_event_functions.append(self.resizeEvent_fun)

    def resizeEvent_fun(self, event: QResizeEvent) -> None:
        '''
        This method is called when the user resizes the window.
        Contains the form.ui widgets that are resized when the user resizes the window.
        '''
        resize_widgets(self, self.labels)
        resize_widgets(self, self.buttons)
        resize_widgets(self, self.widgets)
        for icon in self.icons.values():
            icon_ratio = self.initial_width / icon["initial_icon_width"]
            new_icon_width = self.width() / icon_ratio
            if new_icon_width > icon["initial_icon_width"]:
                new_icon_width = new_icon_width * euler_function(new_icon_width - icon["initial_icon_width"])
            icon['button'].setIconSize(QSize(new_icon_width, new_icon_width))
    
    def resizeEvent(self, event: QResizeEvent) -> None:
        '''
        This method is called when the user resizes the window.
        Executes all the functions in the resize_event_functions list that will be added in the course of the program.
        Replace the resizeEvent method of the QMainWindow class.
        '''
        for function in self.resize_event_functions:
            function(event)
        
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
        If it is not possible to remove the folder, it creates a file called ISO in the folder, so that the program knows that the folder was not removed, and it will remove it when the program is opened again.
        '''
        folder = '.bin'
        try:
            remove_folder(folder)
        except:
            if os.path.exists(folder):
                write_invisible_file('ISO')
        event.accept()
        
    def table_CloseEvent(self, event) -> None:
        '''
        This method is called when the user clicks on the close button of the window, to encrypt the data before closing the window.
        '''
        self.data.update_values(retrieve_from_db())
        if self.data.config == 'T':
            encrypt_database(self.data)
        event.accept()

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

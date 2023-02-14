'''
    @anfreire

    linktr.ee/anfreire
'''

from Sources.imports import *
from Auxiliary.Functions import *
from Auxiliary.Classes import Events
from Sources.init_config import get_font

'''
    This module contains the code for the Start page.
'''

class Start(Events):
    '''
    This class contains the methods that are used in the start page.
    '''
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        '''
        This method initializes the parent class and the start page widgets.
        '''
        self.show_warning = False
        self.data.reset()
        self.start_widgets_start()
        
    def start_widgets_start(self) -> None:
        '''
        This method sets the widgets of the start page.
        This method connects the signals and slots of the start page.
        It should only be called once.
        '''
        self.ui.slider_import_start.setTracking(True)
        self.ui.slider_encrypt_start.setTracking(True)
        self.ui.slider_import_start.valueChanged.connect(lambda:self.values_tracker())
        self.ui.slider_encrypt_start.valueChanged.connect(lambda:self.values_tracker())
        self.ui.button_proceed_start.clicked.connect(lambda:self.next_window_from_start())

    def empty_start(self) -> None:
        '''
        This method empties the start page widgets to their default values.
        '''
        self.ui.slider_encrypt_start.setValue(1)
        self.ui.slider_import_start.setValue(1)

    def go_start(self) -> None:
        '''
        This method sets the start page as the current page.
        '''
        self.ui.stackedWidget.setCurrentWidget(self.ui.Start)
        self.turn_off_actions_menu()

    def next_window_from_start(self) -> None:
        '''
        This method setups the next window, depending on the flag self.flags.create_db.
        The next window can be the register page or the recover page.
        '''
        if self.flags.create_db == True:
            create_folder('.bin')
            self.setup_editor()
            self.go_editor()
        else:
            self.setup_config()
            self.go_config()

    def values_tracker(self) -> None:
        '''
        This method assigns the values of the widgets to the flags, that will be used in the next windows.
        If the user chooses not to encrypt the database, it shows a warning, that is only shown once.
        '''
        if self.ui.slider_import_start.value() == 0:
            self.flags.create_db = True
        elif self.ui.slider_import_start.value() == 1:
            self.flags.create_db = False
        if self.ui.slider_encrypt_start.value() == 1:
            self.flags.encrypt_db = True
            self.data.config = 'T'
        elif self.ui.slider_encrypt_start.value() == 0:
            self.flags.encrypt_db = False
            self.data.config = 'F'
            if self.show_warning == False:
                show_dialog(self, "warning", "We strongly recommend you to encrypt your database!\nNo database is secure against SQL injections and other attacks.", get_font())
                self.show_warning = True
    
            
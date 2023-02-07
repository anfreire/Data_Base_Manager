from imports import *
from Sources.Classes import *
from Sources.Functions import *

class Start(Widget):
    '''
    This class contains the methods that are used in the start page.
    Connects the signals and slots of the start page.
    '''
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        '''
        This method initializes the start page widgets.
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
        self.ui.already_have_db_file_chooser_start.setTracking(True)
        self.ui.encrypt_chooser_start.setTracking(True)
        self.ui.already_have_db_file_chooser_start.valueChanged.connect(lambda:self.values_tracker())
        self.ui.encrypt_chooser_start.valueChanged.connect(lambda:self.values_tracker())
        self.ui.proceed_button_start.clicked.connect(lambda:self.next_window_from_start())

    def empty_start(self) -> None:
        '''
        This method empties the start page widgets to their default values.
        '''
        self.ui.already_have_db_file_chooser_start.setValue(0)
        self.ui.encrypt_chooser_start.setValue(0)

    def go_start(self) -> None:
        '''
        This method sets the start page as the current page.
        '''
        self.ui.stackedWidget.setCurrentWidget(self.ui.start)

    def next_window_from_start(self) -> None:
        '''
        This method setups the next window, depending on the flags, then goes to the next window.
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
        '''
        if self.ui.already_have_db_file_chooser_start.value() == 0:
            self.flags.create_db = False
        elif self.ui.already_have_db_file_chooser_start.value() == 1:
            self.flags.create_db = True
        if self.ui.encrypt_chooser_start.value() == 0:
            self.flags.encrypt_db = True
            self.data.config = 'T'
        elif self.ui.encrypt_chooser_start.value() == 1:
            self.flags.encrypt_db = False
            self.data.config = 'F'
            if self.show_warning == False:
                dialog = QMessageBox()
                dialog.setFont(costum_font)
                dialog.warning(self, "Warning", "We strongly recommend you to encrypt your database!\nNo database is secure against SQL injections and other attacks.", QMessageBox.Ok)
                self.show_warning = True
    
            
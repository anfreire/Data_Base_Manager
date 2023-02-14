'''
    @anfreire

    linktr.ee/anfreire
'''

from Sources.imports import *
from Auxiliary.Functions import *
from Sources.init_config import get_font

'''
    This module contains the dialog that will to verify the code sent to the user's email.
'''

class CodeVerify(QDialog):
    '''
    Dialog to verify the code sent to the user's email.
    It has 2 parameters: code and flag.
    The code is the code sent to the user's email.
    The flag is the flag that will be used to verify the code, and it will be used as a return value.
    If the code is valid, it will set the flag to True, and if it's not, it will set the flag to False.
    Its important to note that the flag must be initialized as False.
    The flag is acesseble through the get_flag() method.
    '''
    def __init__(self, code: str, flag: bool, parent=None) -> None:
        super().__init__(parent)
        '''
        Constructor of the Code Verify Dialog Layout.
        Executes the dialog in the last line.
        '''
        self.setWindowTitle("Verification Code")
        self.code = code
        self.setModal(True)
        self.flag = flag
        self.code_input = QLineEdit()
        code_label = QLabel("Code:")
        email_prompt = QLabel("Enter the code that was sent to your email\nIf you don't see it, it should be in your spam folder.")
        layout = QFormLayout()
        layout.addRow(email_prompt)
        layout.addRow(code_label, self.code_input)
        verify_button = QPushButton("Verify")
        cancel_button = QPushButton("Cancel")
        verify_button.clicked.connect(self.verify_code_)
        cancel_button.clicked.connect(self.reject)
        layout.addRow(verify_button, cancel_button)
        font = self.code_input.font()
        font.setPointSize(font.pointSize() + 4)
        self.code_input.setFont(get_font())
        code_label.setFont(get_font())
        verify_button.setFont(get_font())
        cancel_button.setFont(get_font())
        email_prompt.setFont(get_font())
        layout.setVerticalSpacing(20)
        layout.setContentsMargins(40,40,40,40)
        self.setLayout(layout)
        self.exec()

    def verify_code_(self) -> None:
        '''
        Verifies the code entered by the user.
        Opens a message box if the code is invalid.
        Sets the flag to True if the code is valid, and to False if it's not, as explained in the class description.
        '''
        code = self.code_input.text()
        if code == self.code:
            self.flag = True
            self.accept()
        else:
            show_dialog(self, "Error", "Invalid code, try again", get_font())
            self.code_input.clear()
            self.flag = False

    def get_flag(self) -> bool:
        '''
        Returns the flag.
        The flag is True if the code is valid, and False if it's not, as explained in the class description.
        '''
        return self.flag
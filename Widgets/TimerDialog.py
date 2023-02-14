'''
    @anfreire

    linktr.ee/anfreire
'''

from Sources.imports import *
from Auxiliary.Functions import *
from Sources.init_config import get_font

'''
    This module contains the dialog that will appear when the user wants to change the font of the application.
    It will show only to verify if the user really wants to change the font.
'''

class TimerDialog(QtWidgets.QDialog):
    '''
    This class is the costum dialog that will appear to confirm the font change.
    '''
    def __init__(self, parent=None):
        super().__init__(parent)
        '''
        This method is the constructor of the class.
        It will create the dialog and all the widgets that will be inside it.
        All the widgets will be connected to the methods that will handle them.
        After that, it will show the dialog with the widgets.
        This dialog will have a timer that will count down from 10 to 0.
        If the timer reaches 0, the dialog will be closed and the font will be reset to the previous one.
        If the user clicks on the "Yes" button, the dialog will be closed and the font will be kept.
        If the user clicks on the "No" button, the dialog will be closed and the font will be reset to the previous one.
        '''
        self.setFixedSize(500, 350)
        self.setModal(True)
        self.timer = QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.update_timer)
        self.lcd_number = QLCDNumber(self)
        self.lcd_number.setFixedSize(200, 50)
        self.lcd_number.setDigitCount(1)
        self.lcd_number.display(10)
        self.lcd_number.setMinimumSize(300, 100)
        self.label = QtWidgets.QLabel("Do you want to keep the font selected?\nAfter 10 seconds, the font will be reset to the previous one.")
        font = copy.copy(get_font())
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.adjustSize()
        button = QtWidgets.QPushButton("Yes")
        button.clicked.connect(self.accept)
        button2 = QtWidgets.QPushButton("No")
        button2.clicked.connect(self.reject)
        button.setFont(font)
        button2.setFont(font)
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.lcd_number, alignment=Qt.AlignHCenter)
        layout.addWidget(self.label, alignment=Qt.AlignHCenter)
        layout.addWidget(button)
        layout.addWidget(button2)
        self.setLayout(layout)
        self.timer.start()
    
    def update_timer(self) -> None:
        '''
        This method will update the timer.
        It will decrease the value of the timer by 1.
        If the value is 0, the timer will be stopped and the dialog will be closed, so the font will be reset to the previous one.
        '''
        value = self.lcd_number.value()
        value -= 1
        if value == 0:
            self.timer.stop()
            self.reject()
        else:
            self.lcd_number.display(value)
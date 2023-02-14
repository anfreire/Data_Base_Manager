'''
    @anfreire

    linktr.ee/anfreire
'''

from Sources.imports import *
from Auxiliary.Functions import *
from Sources.init_config import get_font

'''
    This module contains the dialog that will appear when the user wants to set the shortcuts for the actions in the Data Base Table.
'''

class ShortcutDialog(QtWidgets.QDialog):
    '''
    This class is the costum dialog that will appear when the user wants to set the shortcuts for the actions in the Data Base Table.
    '''
    def __init__(self, parent):
        super().__init__(parent)
        '''
        This method is the constructor of the parent class (QDialog) and sets the dialog interface.
        '''
        self.setWindowTitle("Set Shortcuts")
        self.setModal(True)
        self.setFont(get_font())
        self.setContentsMargins(20, 20, 20, 20)
        config = configparser.ConfigParser()
        config.read('config.ini')
        action1Shortcut = config['DEFAULT']['Shortcut +']
        action2Shortcut = config['DEFAULT']['Shortcut -']
        self.action1Shortcut = QtGui.QShortcut(QtGui.QKeySequence(action1Shortcut), self)
        self.action2Shortcut = QtGui.QShortcut(QtGui.QKeySequence(action2Shortcut), self)
        self.action1Button = QtWidgets.QPushButton(action1Shortcut)
        self.action1Button.clicked.connect(self.setAction1Shortcut)
        self.action2Button = QtWidgets.QPushButton(action2Shortcut)
        self.action2Button.clicked.connect(self.setAction2Shortcut)
        self.action1Button.setFont(get_font())
        self.action2Button.setFont(get_font())
        self.action1Button.setFixedSize(100, 30)
        self.action2Button.setFixedSize(100, 30)
        formLayout = QtWidgets.QFormLayout()
        label1 = QtWidgets.QLabel("Increase Table Font")
        label1.setFont(get_font())
        label2 = QtWidgets.QLabel("Decrease Table Font")
        label2.setFont(get_font())
        formLayout.addRow(label1, self.action1Button)
        formLayout.addRow(label2, self.action2Button)
        buttonBox = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel)
        buttonBox.accepted.connect(self.exit_dialog)
        buttonBox.rejected.connect(self.reject)
        buttonBox.button(QtWidgets.QDialogButtonBox.Ok).setFont(get_font())
        buttonBox.button(QtWidgets.QDialogButtonBox.Cancel).setFont(get_font())
        buttonBox.button(QtWidgets.QDialogButtonBox.Ok).setFixedSize(100, 30)
        buttonBox.button(QtWidgets.QDialogButtonBox.Cancel).setFixedSize(100, 30)
        mainLayout = QtWidgets.QVBoxLayout()
        mainLayout.addLayout(formLayout)
        mainLayout.addWidget(buttonBox)
        self.setLayout(mainLayout)
        self._keySequence = None
        
    def exit_dialog(self) -> None:
        '''
        This method is called when the user clicks on the "Ok" button. It checks if the shortcuts are valid and if they are, it saves them in the config file.
        '''
        new_key_1 = ""
        new_key_2 = ""
        if self.action1Button.text() == ("Ctrl" or "Shift" or "Alt") or self.action2Button.text() == ("Ctrl" or "Shift" or "Alt"):
            show_dialog(self, "warning", "You can't use Ctrl, Shift or Alt as a shortcut.\nAlso, you can't use the same shortcut for multiple actions.", get_font())
            return
        elif self.action1Button.text() == self.action2Button.text():
            show_dialog(self, "warning", "You can't use the same shortcut for multiple actions.", get_font())
            return
        elif self.action1Button.text() == "":
            new_key_1 = "StandardKey.ZoomIn"
        elif self.action2Button.text() == "":
            new_key_2 = "StandardKey.ZoomOut"
        else:
            new_key_1 = self.action1Button.text()
            new_key_2 = self.action2Button.text()
            config = configparser.ConfigParser()
            config.read('config.ini')
            config['DEFAULT']['Shortcut +'] = new_key_1
            config['DEFAULT']['Shortcut -'] = new_key_2
            with open('config.ini', 'w') as configfile:
                config.write(configfile)
        self.accept()

    def eventFilter_1(self, object: QObject, event: QEvent) -> bool:
        '''
        This method is called when the user presses a key while the focus is on the "Increase Table Font" button. It sets the shortcut for the action.
        '''
        if object == self.action1Button and event.type() == QtCore.QEvent.KeyPress:
            key = event.key()
            mod = event.modifiers()

            key_sequence = QtGui.QKeySequence(QtCore.Qt.Key(key) | QtCore.Qt.KeyboardModifier(mod))
            self.action1Shortcut.setKey(key_sequence)
            if key_sequence.toString() == "Ctrl+Control":
                self.action1Button.setText("Ctrl")
            elif key_sequence.toString() == "Shift+Shift":
                self.action1Button.setText("Shift")
            elif key_sequence.toString() == "Alt+Alt":
                self.action1Button.setText("Alt")
            else:
                self.action1Button.setText(key_sequence.toString())
            return True
        return super().eventFilter(object, event)
    
    def eventFilter_2(self, object: QObject, event: QEvent) -> bool:
        '''
        This method is called when the user presses a key while the focus is on the "Decrease Table Font" button. It sets the shortcut for the action.
        '''
        if object == self.action2Button and event.type() == QtCore.QEvent.KeyPress:
            key = event.key()
            mod = event.modifiers()
            if QtGui.QKeySequence(QtCore.Qt.Key(key) | QtCore.Qt.KeyboardModifier(mod)) == self.action1Shortcut.key():
                show_dialog(self, "Error", "The shortcut is already used for the other action.", get_font())
            key_sequence = QtGui.QKeySequence(QtCore.Qt.Key(key) | QtCore.Qt.KeyboardModifier(mod))
            self.action2Shortcut.setKey(key_sequence)
            if key_sequence.toString() == "Ctrl+Control":
                self.action2Button.setText("Ctrl")
            elif key_sequence.toString() == "Shift+Shift":
                self.action2Button.setText("Shift")
            elif key_sequence.toString() == "Alt+Alt":
                self.action2Button.setText("Alt")
            else:
                self.action2Button.setText(key_sequence.toString())
            return True
        return super().eventFilter(object, event)

    def setAction1Shortcut(self) -> None:
        '''
        This method is called when the user clicks on the "Increase Table Font" button. It sets the shortcut for the action.
        '''
        self._keySequence = QKeySequence()
        self.action1Shortcut.setKeys(self._keySequence)
        self.action1Button.setText(self._keySequence.toString())
        self.action1Button.installEventFilter(self)
        self.eventFilter = self.eventFilter_1
        self.action1Button.setFocus()

    def setAction2Shortcut(self) -> None:
        '''
        This method is called when the user clicks on the "Decrease Table Font" button. It sets the shortcut for the action.
        '''
        self._keySequence = QtGui.QKeySequence()
        self.action2Shortcut.setKeys(self._keySequence)
        self.action2Button.setText(self._keySequence.toString())
        self.action2Button.installEventFilter(self)
        self.eventFilter = self.eventFilter_2
        self.action2Button.setFocus()
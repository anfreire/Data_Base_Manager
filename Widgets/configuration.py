from imports import *
from Sources.Functions import *
from init_config import costum_font

class Ui_Dialog(object):
    '''
    Auto-generated code from Qt Designer.
    '''
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 400)
        Dialog.setMinimumSize(QtCore.QSize(400, 400))
        Dialog.setMaximumSize(QtCore.QSize(483, 400))
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(20, 0, 20, 20)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=Dialog)
        font = QtGui.QFont()
        font.setPointSize(19)
        self.label.setFont(costum_font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(parent=Dialog)
        font = QtGui.QFont()
        font.setPointSize(19)
        self.label_2.setFont(costum_font)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2, 0, QtCore.Qt.AlignmentFlag.AlignRight)
        self.horizontalScrollBar = QtWidgets.QScrollBar(parent=Dialog)
        self.horizontalScrollBar.setMinimumSize(QtCore.QSize(200, 0))
        self.horizontalScrollBar.setMaximum(1)
        self.horizontalScrollBar.setPageStep(1)
        self.horizontalScrollBar.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.horizontalScrollBar.setObjectName("horizontalScrollBar")
        self.horizontalLayout.addWidget(self.horizontalScrollBar)
        self.label_3 = QtWidgets.QLabel(parent=Dialog)
        font = QtGui.QFont()
        font.setPointSize(19)
        self.label_3.setFont(costum_font)
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line = QtWidgets.QFrame(parent=Dialog)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.label_5 = QtWidgets.QLabel(parent=Dialog)
        font = QtGui.QFont()
        font.setPointSize(19)
        self.label_5.setFont(costum_font)
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(20)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_6 = QtWidgets.QLabel(parent=Dialog)
        font = QtGui.QFont()
        font.setPointSize(19)
        self.label_6.setFont(costum_font)
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6, 0, QtCore.Qt.AlignmentFlag.AlignRight)
        self.horizontalScrollBar_2 = QtWidgets.QScrollBar(parent=Dialog)
        self.horizontalScrollBar_2.setMinimumSize(QtCore.QSize(200, 0))
        self.horizontalScrollBar_2.setMaximum(1)
        self.horizontalScrollBar_2.setPageStep(1)
        self.horizontalScrollBar_2.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.horizontalScrollBar_2.setObjectName("horizontalScrollBar_2")
        self.horizontalLayout_2.addWidget(self.horizontalScrollBar_2)
        self.label_4 = QtWidgets.QLabel(parent=Dialog)
        font = QtGui.QFont()
        font.setPointSize(19)
        self.label_4.setFont(costum_font)
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.line_2 = QtWidgets.QFrame(parent=Dialog)
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.label_7 = QtWidgets.QLabel(parent=Dialog)
        font = QtGui.QFont()
        font.setPointSize(19)
        self.label_7.setFont(costum_font)
        self.label_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.fontComboBox = QtWidgets.QFontComboBox(parent=Dialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.fontComboBox.setFont(costum_font)
        self.fontComboBox.setObjectName("fontComboBox")
        self.horizontalLayout_4.addWidget(self.fontComboBox)
        self.spinBox = QtWidgets.QSpinBox(parent=Dialog)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.spinBox.setFont(costum_font)
        self.spinBox.setMinimum(5)
        self.spinBox.setMaximum(30)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout_4.addWidget(self.spinBox)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Theme"))
        self.label_2.setText(_translate("Dialog", "Light"))
        self.label_3.setText(_translate("Dialog", "Dark"))
        self.label_5.setText(_translate("Dialog", "Encryption"))
        self.label_6.setText(_translate("Dialog", "Yes"))
        self.label_4.setText(_translate("Dialog", "No"))
        self.label_7.setText(_translate("Dialog", "Font"))

class Configuration(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        '''
        Constructor for the Configuration Dialog
        '''
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.parent = parent
        self.start_Configuration()

    def start_Configuration(self) -> None:
        '''
        This function is used to start the Configuration Dialog
        It should be called in the __init__ function, and not anywhere else
        Sets the widgets to the current configuration
        Sets the closeEvent to the closeEvent function, info about this can be found in the closeEvent function
        '''
        config = configparser.ConfigParser()
        config.read('config.ini')
        self.current_theme = config['DEFAULT']['current_theme']
        self.encryption = config['DEFAULT']['encryption']
        self.db_font = config['DEFAULT']['font']
        self.font_size = int(config['DEFAULT']['font_size'])
        self.closeEvent = self.closeEvent
        self.ui.horizontalScrollBar_2.valueChanged.connect(lambda: self.update_encryption())
        if self.current_theme == "light":
            self.ui.horizontalScrollBar.setValue(0)
        else:
            self.ui.horizontalScrollBar.setValue(1)
        if self.encryption == "True":
            self.ui.horizontalScrollBar_2.setValue(0)
        else:
            self.ui.horizontalScrollBar_2.setValue(1)
        self.ui.fontComboBox.setCurrentText(self.db_font)
        self.ui.spinBox.setValue(self.font_size)
        self.show()

    def closeEvent(self, event: QCloseEvent) -> None:
        '''
        This function is called when the user closes the Configuration Dialog
        It saves the current configuration to the config.ini file
        '''
        self.save_config()
        event.accept()
        
    def save_config(self) -> None:
        '''
        This function is used to save the current configuration to the config.ini file
        Its called when the user closes the Configuration Dialog
        '''
        current_theme = ["light", "dark"]
        enctyption = ["True", "False"]
        config = configparser.ConfigParser()
        config['DEFAULT'] = {'current_theme': current_theme[self.ui.horizontalScrollBar.value()],
                            'encryption': enctyption[self.ui.horizontalScrollBar_2.value()],
                            'font': self.ui.fontComboBox.currentText(),
                            'font_size': str(self.ui.spinBox.value()),}
        with open('config.ini', 'w') as configfile:
            config.write(configfile)
            
    def update_config(self, new_config) -> None:
        '''
        This function is used to update the encryption value in the user loggin information
        '''
        self.data.update_values(retrieve_from_db())
        conn = sqlite3.connect('.bin/log.db')
        with conn:
            c = conn.cursor()
            c.execute("SELECT users, passwrds, code, email, config, key FROM data")
            result = c.fetchone()
            users = result[0]
            passwrds = result[1]
            code = result[2]
            email = result[3]
            config = result[4]
            key = result[5]
        encrypted_config = encrypt(str(new_config).encode(), key)
        conn = sqlite3.connect('.bin/log.db')
        with conn:
            c = conn.cursor()
            c.execute("UPDATE data SET config = ?", (encrypted_config,))
            conn.commit()
        self.data['config'] = new_config
            
    def update_encryption(self) -> None:
        '''
        This function is auxillary to the update_config, connects the witgets to the update_config function.
        If the user wants to disable encryption, it will ask for confirmation
        '''
        if self.ui.horizontalScrollBar_2.value() == 0 and self.parent.data.config == 'F':
            self.update_config('T')
        elif self.ui.horizontalScrollBar_2.value() == 1 and self.parent.data.config == 'T':
            warning = QMessageBox.warning(self, "Warning", "Are you sure you want to disable encryption? This will make your data vulnerable to hackers.", QMessageBox.Yes | QMessageBox.No)
            if warning == QMessageBox.Yes:
                self.update_config('F')
            else:
                self.ui.horizontalScrollBar_2.setValue(0)    

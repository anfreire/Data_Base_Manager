from imports import *
from init_config import costum_font
from Widgets.newTable import newTable

class newTab(QWidget):
    '''
    This class contains the code for the new tab widget.
    Mainly, it contains the GUI code.
    '''
    def __init__(self, data, parent=None):
        super().__init__(parent)
        '''
        This is the constructor for the newTab class.
        '''
        self.parent = parent
        self.setupUi()
        self.create_table_widget(data)

    def setupUi(self):
        '''
        This function contains the GUI code for the new tab widget.
        It is called in the constructor.
        It should not be called anywhere else.
        '''
        self.setFont(costum_font)
        self.setObjectName("widget_table")
        self.gridLayout_4 = QtWidgets.QGridLayout(self)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setContentsMargins(20, 10, 20, 10)
        self.horizontalLayout_12.setSpacing(20)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.search_input = QtWidgets.QLineEdit(self)
        self.search_input.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Thin")
        font.setPointSize(16)
        font.setBold(False)
        self.search_input.setFont(costum_font)
        self.search_input.setText("")
        self.search_input.setObjectName("search_input")
        self.horizontalLayout_12.addWidget(self.search_input)
        self.combo_box = QtWidgets.QComboBox(self)
        self.combo_box.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Thin")
        font.setPointSize(18)
        font.setBold(False)
        self.combo_box.setFont(costum_font)
        self.combo_box.setObjectName("combo_box")
        self.horizontalLayout_12.addWidget(self.combo_box)
        self.search_button = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_button.sizePolicy().hasHeightForWidth())
        self.search_button.setSizePolicy(sizePolicy)
        self.search_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("PNG/SEARCH.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.search_button.setIcon(icon)
        self.search_button.setIconSize(QtCore.QSize(40, 40))
        self.search_button.setFlat(True)
        self.search_button.setObjectName("search_button")
        self.horizontalLayout_12.addWidget(self.search_button)
        self.line_2 = QtWidgets.QFrame(self)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_12.addWidget(self.line_2)
        self.add_button = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_button.sizePolicy().hasHeightForWidth())
        self.add_button.setSizePolicy(sizePolicy)
        self.add_button.setMinimumSize(QtCore.QSize(40, 40))
        self.add_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("PNG/ADD.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.add_button.setIcon(icon1)
        self.add_button.setIconSize(QtCore.QSize(40, 40))
        self.add_button.setFlat(True)
        self.add_button.setObjectName("add_button")
        self.horizontalLayout_12.addWidget(self.add_button)
        self.horizontalLayout_12.setStretch(1, 10)
        self.horizontalLayout_12.setStretch(2, 1)
        self.horizontalLayout_12.setStretch(3, 1)
        self.horizontalLayout_12.setStretch(4, 3)
        icon3 = QIcon()
        icon3.addFile(u"PNG/BACK_ARROW.png", QSize(), QIcon.Normal, QIcon.Off)
        self.return_button = QPushButton(self)
        self.return_button.setObjectName(u"return_button")
        self.return_button.setIcon(icon3)
        self.return_button.setIconSize(QSize(40, 40))
        self.return_button.setFlat(True)
        self.horizontalLayout_12.insertWidget(0, self.return_button)
        self.verticalLayout_11.addLayout(self.horizontalLayout_12)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_11.addLayout(self.verticalLayout_7)
        self.gridLayout_4.addLayout(self.verticalLayout_11, 0, 0, 1, 1)
        self.combo_box.setPlaceholderText("Search by")
        self.search_input.setPlaceholderText("Search here")
        self.return_button.clicked.connect(lambda:self.parent.go_home())
        
    def create_table_widget(self, data) -> None:
        '''
        This method creates the table widget.
        Passes the data retrieved from the db file, the search input, the combo box, the search button and the add button to the newTable class.
        It also sets the object name of the table widget.
        Its only called in the __init__ method of the class.
        It shouldn't be called anywhere else.
        '''
        self.tableWidget = newTable(data, (self.search_input, self.combo_box, self.search_button, self.add_button))
        self.tableWidget.setObjectName("tableWidget")
        self.verticalLayout_7.addWidget(self.tableWidget)

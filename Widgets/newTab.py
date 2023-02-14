'''
    @anfreire

    linktr.ee/anfreire
'''

from Sources.imports import *
from Auxiliary.Functions import *
from Widgets.newTable import newTable
from Sources.init_config import get_font

'''
    This module contains the code for the new tab widget.
    It will be used in the QTabWidget in the main window.
'''

class newTab(QWidget):
    '''
    This class contains the code for the new tab widget.
    '''
    def __init__(self, data, parent=None) -> None:
        super().__init__(parent)
        '''
        This is the constructor for the newTab class.
        '''
        self.parent = parent
        self.setupUi()
        self.create_table_widget(data)
        self.setup_resize_event_tab()
        self.parent.resize_event_functions.append(self.resizeEvent_Tab)
    
    def setupUi(self) -> None:
        '''
        This function contains the GUI code for the new tab widget.
        It is called in the constructor.
        It should not be called anywhere else.
        '''
        tab_widget_font = copy.copy(get_font())
        tab_widget_font.setPointSize(20)
        self.setFont(tab_widget_font)
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
        icon3 = QIcon()
        icon3.addFile(resource_path("Images/LOGOUT.png"), QSize(), QIcon.Normal, QIcon.Off)
        self.return_button = QPushButton(self)
        self.return_button.setObjectName(u"return_button")
        self.return_button.setIcon(icon3)
        self.return_button.setIconSize(QSize(40, 40))
        self.return_button.setFlat(True)
        self.horizontalLayout_12.addWidget(self.return_button)
        self.search_input = QtWidgets.QLineEdit(self)
        self.search_input.setMinimumSize(QtCore.QSize(0, 40))
        font = copy.copy(get_font())
        self.search_input.setFont(get_font())
        self.search_input.setText("")
        self.search_input.setObjectName("search_input")
        self.horizontalLayout_12.addWidget(self.search_input)
        self.combo_box = QtWidgets.QComboBox(self)
        self.combo_box.setMinimumSize(QtCore.QSize(0, 40))
        font = copy.copy(get_font())
        font.setPointSize(18)
        self.combo_box.setFont(get_font())
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
        icon.addPixmap(QtGui.QPixmap(resource_path("Images/SEARCH.png")), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.search_button.setIcon(icon)
        self.search_button.setIconSize(QtCore.QSize(40, 40))
        self.search_button.setFlat(True)
        self.search_button.setObjectName("search_button")
        self.search_input.returnPressed.connect(self.search_button.click)
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
        icon1.addPixmap(QtGui.QPixmap(resource_path("Images/ADD.png")), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.add_button.setIcon(icon1)
        self.add_button.setIconSize(QtCore.QSize(40, 40))
        self.add_button.setFlat(True)
        self.add_button.setObjectName("add_button")
        self.horizontalLayout_12.addWidget(self.add_button)
        self.horizontalLayout_12.setStretch(0, 0)
        self.horizontalLayout_12.setStretch(1, 1)
        self.horizontalLayout_12.setStretch(2, 1)
        self.horizontalLayout_12.setStretch(3, 0)
        self.horizontalLayout_12.setStretch(4, 0)
        self.verticalLayout_11.addLayout(self.horizontalLayout_12)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_11.addLayout(self.verticalLayout_7)
        self.gridLayout_4.addLayout(self.verticalLayout_11, 0, 0, 1, 1)
        self.combo_box.setPlaceholderText("Search by")
        self.search_input.setPlaceholderText("Search here")
        self.return_button.clicked.connect(lambda:self.logout())
    
    def setup_resize_event_tab(self) -> None:
        '''
        This function is called when the new tab widget is resized to get the needed values for the resize event.
        '''
        widgets = [self.search_input, self.combo_box, self.tableWidget]
        icons = [self.return_button, self.search_button]
        self.widgets_tab = get_initial_fonts_widgets(widgets)
        self.parent.tabWidgets.append(self.widgets_tab)
        self.icons_tab = {}
        for i, icon in enumerate(self.icons_tab):
            self.icons_tab[i] = {"button": icon, "initial_icon_width": icon.iconSize().width()}
            
    def resizeEvent_Tab(self, event: QResizeEvent) -> None:
        '''
        This function is called when the new tab widget is resized to resize the widgets.
        '''
        for widget in self.widgets_tab.values():
            point_per_width = self.parent.initial_width / widget["initial_font"].pointSizeF()
            new_font = widget['widget'].font()
            new_font_size = (self.parent.width() / point_per_width)
            if int(new_font_size) > int(widget["initial_font"].pointSizeF()):
                new_font_size = new_font_size * euler_function(new_font_size - widget["initial_font"].pointSizeF())
            new_font.setPointSizeF(new_font_size)
            widget['widget'].setFont(new_font)
        for icon in self.icons_tab.values():
            icon_ratio = self.parent.initial_width / icon["initial_icon_width"]
            new_icon_width = self.parent.width() / icon_ratio
            if self.parent.width() > self.parent.initial_width:
                new_icon_width = new_icon_width * euler_function(new_icon_width - icon["initial_icon_width"])
            icon['button'].setIconSize(QSize(new_icon_width, new_icon_width))

    def logout(self) -> None:
        '''
        This method logs the user out.
        It is called when the logout button is clicked.
        '''
        if self.parent.data.config == 'T':
            encrypt_database(self.parent.data)
        self.parent.empty_login()
        self.parent.setup_login()
        self.parent.go_login()
    
    def create_table_widget(self, data) -> None:
        '''
        This method creates the table widget.
        Passes the data retrieved from the db file, the search input, the combo box, the search button and the add button to the newTable class.
        It also sets the object name of the table widget.
        Its only called in the __init__ method of the class.
        It shouldn't be called anywhere else.
        '''
        self.tableWidget = newTable(data, (self.search_input, self.combo_box, self.search_button, self.add_button), self.parent)
        self.tableWidget.setObjectName("tableWidget")
        self.verticalLayout_7.addWidget(self.tableWidget)

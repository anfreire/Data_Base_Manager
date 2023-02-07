from imports import *
from init_config import costum_font
'''
    !    NOT USED IN THIS VERSION
'''
class Ui_Dialog(object):
    '''
    Auto-generated code for the align input window.
    '''
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(600, 500)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.database_list = QtWidgets.QListWidget(parent=Dialog)
        self.database_list.setObjectName("database_list")
        self.horizontalLayout_2.addWidget(self.database_list)
        self.input_list = QtWidgets.QListWidget(parent=Dialog)
        self.input_list.setDragEnabled(True)
        self.input_list.setDragDropMode(QtWidgets.QAbstractItemView.DragDropMode.InternalMove)
        self.input_list.setObjectName("input_list")
        self.horizontalLayout_2.addWidget(self.input_list)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ignore_c = QtWidgets.QPushButton(parent=Dialog)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.ignore_c.setFont(costum_font)
        self.ignore_c.setObjectName("ignore_c")
        self.horizontalLayout.addWidget(self.ignore_c)
        self.proceed = QtWidgets.QPushButton(parent=Dialog)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.proceed.setFont(costum_font)
        self.proceed.setObjectName("proceed")
        self.horizontalLayout.addWidget(self.proceed)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.ignore_c.setText(_translate("Dialog", "Ignore Column"))
        self.proceed.setText(_translate("Dialog", "Proceed"))

'''
    !    NOT USED IN THIS VERSION
'''
 
class Align_input(QtWidgets.QDialog):
    '''
    Still needs to be implemented.
    Class not used in the current version.
    '''
    def __init__(self, db, excel, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.db = db
        self.excel = list(excel)
        for i in self.db:
            self.ui.database_list.addItem(i)
        for i in self.excel:
            self.ui.input_list.addItem(i)
        self.ui.ignore_c.clicked.connect(lambda: self.ignore())
        self.show()
        self.ui.proceed.clicked.connect(lambda: self.accept())
        self.ui.input_list.setFont(costum_font)
        self.ui.database_list.setFont(costum_font)
        self.ui.input_list.setWindowTitle("Excel Columns")
        self.ui.database_list.setWindowTitle("Database Columns")
        self.ui.input_list.setAlternatingRowColors(True)
        self.ui.database_list.setAlternatingRowColors(True)

    '''
        !    NOT USED IN THIS VERSION
    '''     
        
    def ignore(self) -> None:
        '''
        Removes the selected item from the list.
        Protects against selecting both lists at the same time.
        '''
        if self.ui.input_list.currentItem() is not None and self.ui.database_list.currentItem() is not None:
            dialog = QMessageBox()
            dialog.setFont(costum_font)
            dialog.critical(self, "Error", "Please select only one column from either list")
            self.ui.input_list.setCurrentRow(-1)
            self.ui.database_list.setCurrentRow(-1)
        else:
            if self.ui.input_list.currentItem() is not None:
                self.ui.input_list.takeItem(self.ui.input_list.currentRow())
                self.ui.input_list.setCurrentRow(-1)
            elif self.ui.database_list.currentItem() is not None:
                self.ui.database_list.takeItem(self.ui.database_list.currentRow())
                self.ui.database_list.setCurrentRow(-1)

    '''
       !    NOT USED IN THIS VERSION
    '''
    
    def get_mapping_excel(self) -> dict:
        '''
        Returns a dictionary with the excel column names as keys and the database column names as values.
        '''
        rearranged_list = []
        for i in range(self.ui.input_list.count()):
            rearranged_list.append(self.ui.input_list.item(i).text())
        mapping = {self.excel[i]: rearranged_list[i] for i in range(len(self.excel))}
        return mapping
    
    def get_mapping_db(self) -> dict:
        '''
        Returns a dictionary with the database column names as keys and the excel column names as values.
        '''
        rearranged_list = []
        for i in range(self.ui.database_list.count()):
            rearranged_list.append(self.ui.database_list.item(i).text())
        mapping = {self.db[i]: rearranged_list[i] for i in range(len(self.db))}
        return mapping

'''
    @anfreire

    linktr.ee/anfreire
'''

from Sources.imports import *
from Auxiliary.Functions import *
from Widgets.AddUser import AddUser
from Sources.init_config import get_font

'''
    This module contains the dialog that will appear when the user wants to edit the users when its already registered.
'''

class Ui_Dialog(object):
    '''
    Auto-generated code from Qt Designer.
    '''
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(300, 200)
        Dialog.setMinimumSize(QtCore.QSize(300, 200))
        Dialog.setMaximumSize(QtCore.QSize(300, 200))
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.listWidget = QtWidgets.QListWidget(parent=Dialog)
        self.listWidget.setMinimumSize(QtCore.QSize(150, 160))
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.listWidget, 0, 0, 2, 1)
        self.add_user_button_2 = QtWidgets.QPushButton(parent=Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_user_button_2.sizePolicy().hasHeightForWidth())
        self.add_user_button_2.setSizePolicy(sizePolicy)
        self.add_user_button_2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(resource_path("Images/ADD_USER.webp")), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.add_user_button_2.setIcon(icon)
        self.add_user_button_2.setIconSize(QtCore.QSize(40, 40))
        self.add_user_button_2.setFlat(True)
        self.add_user_button_2.setObjectName("add_user_button_2")
        self.gridLayout.addWidget(self.add_user_button_2, 0, 1, 1, 1)
        self.delete_button = QtWidgets.QPushButton(parent=Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delete_button.sizePolicy().hasHeightForWidth())
        self.delete_button.setSizePolicy(sizePolicy)
        self.delete_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(resource_path("Images/Delete.png")), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.delete_button.setIcon(icon1)
        self.delete_button.setIconSize(QtCore.QSize(40, 40))
        self.delete_button.setFlat(True)
        self.delete_button.setObjectName("delete_button")
        self.gridLayout.addWidget(self.delete_button, 1, 1, 1, 1)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))

class EditUsers(QtWidgets.QDialog):
    '''
    This class is used to edit the users.
    Its acessible from the Data Base Home.
    '''
    def __init__(self, parent=None):
        '''
        This method initializes the class.
        Sets the close event to the newcloseEvent method.
        Gets the data from the parent.
        Shows the Dialog.
        '''
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.setModal(True)
        self.parent = parent
        self.parent.data.update_values(retrieve_from_db())
        self.data = self.parent.data
        self.tmp_flag = True
        self.ui.setupUi(self)
        self.ui.add_user_button_2.clicked.connect(lambda: self.update_user_lists())
        self.ui.delete_button.clicked.connect(lambda: self.delete_user())
        self.closeEvent = self.newcloseEvent
        for user in self.data.users:
            if self.ui.listWidget.findItems(user, Qt.MatchExactly):
                continue
            user = QListWidgetItem(user)
            user.setFont(get_font())
            user.setTextAlignment(Qt.AlignCenter)
            self.ui.listWidget.addItem(user)
        self.show()
    
    def update_users(self, new_users, new_passwrds) -> None:
        '''
        This function is used to update the user and password information in the database
        '''
        self.data = self.parent.data
        self.data.update_values(retrieve_from_db())
        conn = sqlite3.connect('.bin/log.db')
        with conn:
            c = conn.cursor()
            c.execute("SELECT users, passwrds, code, email, config, key FROM data")
            result = c.fetchone()
            code = result[2]
            email = result[3]
            config = result[4]
            key = result[5]
        encrypted_users = encrypt(str(new_users).encode(), key)
        encrypted_passwrds = encrypt(str(new_passwrds).encode(), key)
        conn = sqlite3.connect('.bin/log.db')
        with conn:
            c = conn.cursor()
            c.execute("UPDATE data SET users = ?, passwrds = ?", (encrypted_users, encrypted_passwrds))
            conn.commit()
        self.data.users = new_users
        self.data.passwrds = new_passwrds
        self.parent.data = self.data
    
    def newcloseEvent(self, event: QCloseEvent) -> None:
        '''
        This method is called when the window is closed.
        It saves the new users to the database.
        '''
        
        self.update_users(self.data.users, self.data.passwrds)
        event.accept()
        self.parent.data.update_values(retrieve_from_db())
        
    def delete_user(self) -> None:
        '''
        This method deletes the user from the list widget and the corresponding data.
        '''
        question = show_question(self,  "question", f"Are you sure you want to delete this user?", get_font())
        if question == True:
            if len(self.parent.data.users) == 1:
                show_dialog(self, "Error", "You can't delete the last user.", get_font())
                return
            user = self.ui.listWidget.currentItem()
            if user is None:
                show_dialog(self, "Error", "Please select a user to delete.", get_font())
                return
            user = user.text()
            index = self.data.users.index(user)
            self.parent.data.users.pop(index)
            self.parent.data.passwrds.pop(index)
            self.ui.listWidget.takeItem(self.ui.listWidget.currentRow())
        self.ui.listWidget.clearSelection()
        for user in self.data.users:
            if self.ui.listWidget.findItems(user, Qt.MatchExactly):
                continue
            user = QListWidgetItem(user)
            user.setFont(get_font())
            user.setTextAlignment(Qt.AlignCenter)
            self.ui.listWidget.addItem(user)

    def update_user_lists(self) -> None:
        '''
        This method updates the user list widget, opens a dialog to add users, updates the loggin data and the corresponding flag.
        '''
        self.data.users, self.data.passwrds, self.tmp_flag = AddUser(self.data.users, self.data.passwrds, self.tmp_flag).get_values()
        for user in self.data.users:
            if self.ui.listWidget.findItems(user, Qt.MatchExactly):
                continue
            user = QListWidgetItem(user)
            user.setFont(get_font())
            user.setTextAlignment(Qt.AlignCenter)
            self.ui.listWidget.addItem(user)

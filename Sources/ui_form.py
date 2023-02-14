'''
    @anfreire

    linktr.ee/anfreire
'''

from Sources.imports import *
from Sources.init_config import get_font

'''
    This class is used to create the main window of the program.
    It was created using Qt Designer.
    Few changes were made to the code.
    No code should be added to this class.
    Qt Generated code should remain untouched.
'''
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QSize(800, 600))
        self.main_window = MainWindow
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stackedWidget = QStackedLayout(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(10, 10, 664, 589))
        self.Start = QWidget()
        self.Start.setObjectName(u"Start")
        self.gridLayout_2 = QGridLayout(self.Start)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(20)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(20, 20, 20, 20)
        self.label_2 = QLabel(self.Start)
        self.label_2.setObjectName(u"label_2")
        font = copy.copy(get_font())
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 2, 1, 1, 1)

        self.button_proceed_start = QPushButton(self.Start)
        self.button_proceed_start.setObjectName(u"button_proceed_start")
        self.button_proceed_start.setFont(font)

        self.gridLayout.addWidget(self.button_proceed_start, 8, 1, 1, 1, Qt.AlignHCenter)

        self.label_3 = QLabel(self.Start)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 4, 1, 1, 1)

        self.line_4 = QFrame(self.Start)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_4, 1, 1, 1, 1)

        self.label_15 = QLabel(self.Start)
        self.label_15.setObjectName(u"label_15")
        font1 = copy.copy(get_font())
        font1.setPointSize(60)
        self.label_15.setFont(font1)
        self.label_15.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_15, 0, 0, 1, 3)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_11)

        self.label_7 = QLabel(self.Start)
        self.label_7.setObjectName(u"label_7")
        font2 = copy.copy(get_font())
        font2.setPointSize(15)
        self.label_7.setFont(font2)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_7, 0, Qt.AlignLeft|Qt.AlignBottom)

        self.label_6 = QLabel(self.Start)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_6, 0, Qt.AlignRight|Qt.AlignBottom)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_12)

        self.horizontalLayout_8.setStretch(0, 1)
        self.horizontalLayout_8.setStretch(1, 1)
        self.horizontalLayout_8.setStretch(2, 1)
        self.horizontalLayout_8.setStretch(3, 1)

        self.verticalLayout_3.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_10)

        self.slider_encrypt_start = QSlider(self.Start)
        self.slider_encrypt_start.setObjectName(u"slider_encrypt_start")
        self.slider_encrypt_start.setMinimumSize(QSize(0, 20))
        self.slider_encrypt_start.setMaximum(1)
        self.slider_encrypt_start.setPageStep(1)
        self.slider_encrypt_start.setValue(1)
        self.slider_encrypt_start.setTracking(True)
        self.slider_encrypt_start.setOrientation(Qt.Horizontal)
        self.slider_encrypt_start.setTickPosition(QSlider.TicksAbove)
        self.slider_encrypt_start.setTickInterval(0)

        self.horizontalLayout_4.addWidget(self.slider_encrypt_start)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 2)
        self.horizontalLayout_4.setStretch(2, 1)

        self.verticalLayout_3.addLayout(self.horizontalLayout_4)


        self.gridLayout.addLayout(self.verticalLayout_3, 5, 0, 1, 3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_13)

        self.label_4 = QLabel(self.Start)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font2)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_4, 0, Qt.AlignLeft|Qt.AlignBottom)

        self.label_5 = QLabel(self.Start)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_5, 0, Qt.AlignRight|Qt.AlignBottom)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_14)

        self.horizontalLayout_9.setStretch(0, 1)
        self.horizontalLayout_9.setStretch(1, 1)
        self.horizontalLayout_9.setStretch(2, 1)
        self.horizontalLayout_9.setStretch(3, 1)

        self.verticalLayout_4.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_15)

        self.slider_import_start = QSlider(self.Start)
        self.slider_import_start.setObjectName(u"slider_import_start")
        self.slider_import_start.setMinimumSize(QSize(0, 20))
        self.slider_import_start.setMaximum(1)
        self.slider_import_start.setPageStep(1)
        self.slider_import_start.setValue(1)
        self.slider_import_start.setTracking(True)
        self.slider_import_start.setOrientation(Qt.Horizontal)
        self.slider_import_start.setTickPosition(QSlider.TicksAbove)

        self.horizontalLayout_10.addWidget(self.slider_import_start)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_16)

        self.horizontalLayout_10.setStretch(0, 1)
        self.horizontalLayout_10.setStretch(1, 2)
        self.horizontalLayout_10.setStretch(2, 1)

        self.verticalLayout_4.addLayout(self.horizontalLayout_10)


        self.gridLayout.addLayout(self.verticalLayout_4, 3, 0, 1, 3)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.Start)
        self.Config = QWidget()
        self.Config.setObjectName(u"Config")
        self.gridLayout_4 = QGridLayout(self.Config)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setSpacing(20)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(20, 20, 20, 20)
        self.label_8 = QLabel(self.Config)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_8, 0, 1, 1, 1, Qt.AlignHCenter)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_10 = QLabel(self.Config)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_10, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.button_browse_config = QPushButton(self.Config)
        self.button_browse_config.setObjectName(u"button_browse_config")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_browse_config.sizePolicy().hasHeightForWidth())
        self.button_browse_config.setSizePolicy(sizePolicy)
        self.button_browse_config.setMinimumSize(QSize(50, 50))
        icon = QIcon()
        icon.addFile(resource_path("Images/FOLDER.png"), QSize(), QIcon.Normal, QIcon.Off)
        self.button_browse_config.setIcon(icon)
        self.button_browse_config.setIconSize(QSize(50, 50))
        self.button_browse_config.setFlat(True)

        self.verticalLayout.addWidget(self.button_browse_config, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.listWidget = QListWidget(self.Config)
        self.listWidget.setObjectName(u"listWidget")

        self.horizontalLayout_2.addWidget(self.listWidget, 0, Qt.AlignVCenter)

        self.button_add_config = QPushButton(self.Config)
        self.button_add_config.setObjectName(u"button_add_config")
        sizePolicy.setHeightForWidth(self.button_add_config.sizePolicy().hasHeightForWidth())
        self.button_add_config.setSizePolicy(sizePolicy)
        self.button_add_config.setMinimumSize(QSize(50, 50))
        icon1 = QIcon()
        icon1.addFile(resource_path("Images/ADD_USER.webp"), QSize(), QIcon.Normal, QIcon.Off)
        self.button_add_config.setIcon(icon1)
        self.button_add_config.setIconSize(QSize(50, 50))
        self.button_add_config.setFlat(True)

        self.horizontalLayout_2.addWidget(self.button_add_config, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_2.setStretch(0, 3)
        self.horizontalLayout_2.setStretch(1, 2)
        self.horizontalLayout_2.setStretch(2, 1)

        self.gridLayout_3.addLayout(self.horizontalLayout_2, 3, 0, 1, 3)

        self.button_return_config = QPushButton(self.Config)
        self.button_return_config.setObjectName(u"button_return_config")
        sizePolicy.setHeightForWidth(self.button_return_config.sizePolicy().hasHeightForWidth())
        self.button_return_config.setSizePolicy(sizePolicy)
        self.button_return_config.setMinimumSize(QSize(50, 50))
        icon2 = QIcon()
        icon2.addFile(resource_path("Images/BACK_ARROW.png"), QSize(), QIcon.Normal, QIcon.Off)
        self.button_return_config.setIcon(icon2)
        self.button_return_config.setIconSize(QSize(50, 50))
        self.button_return_config.setFlat(True)

        self.gridLayout_3.addWidget(self.button_return_config, 0, 0, 1, 1, Qt.AlignLeft|Qt.AlignTop)

        self.button_proceed_config = QPushButton(self.Config)
        self.button_proceed_config.setObjectName(u"button_proceed_config")
        self.button_proceed_config.setFont(font)

        self.gridLayout_3.addWidget(self.button_proceed_config, 4, 1, 1, 1, Qt.AlignHCenter)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.label_9 = QLabel(self.Config)
        self.label_9.setObjectName(u"label_9")
        font3 = copy.copy(get_font())
        font3.setPointSize(18)
        self.label_9.setFont(font3)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_9, 0, Qt.AlignRight|Qt.AlignVCenter)

        self.input_email_config = QLineEdit(self.Config)
        self.input_email_config.setObjectName(u"input_email_config")
        font_input = copy.copy(get_font())
        font_input.setPointSize(13)
        self.input_email_config.setFont(font_input)

        self.horizontalLayout.addWidget(self.input_email_config, 0, Qt.AlignVCenter)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 2)
        self.horizontalLayout.setStretch(3, 1)

        self.gridLayout_3.addLayout(self.horizontalLayout, 2, 0, 1, 3)

        self.line = QFrame(self.Config)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line, 1, 1, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.Config)
        self.Confirm_Email = QWidget()
        self.Confirm_Email.setObjectName(u"Confirm_Email")
        self.gridLayout_10 = QGridLayout(self.Confirm_Email)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setSpacing(20)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(20, 20, 20, 20)
        self.label_12 = QLabel(self.Confirm_Email)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font1)
        self.label_12.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.label_12, 0, 1, 1, 1, Qt.AlignHCenter)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)

        self.label_14 = QLabel(self.Confirm_Email)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font)
        self.label_14.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_14, 0, Qt.AlignRight|Qt.AlignVCenter)

        self.input_email_confirm_email = QLineEdit(self.Confirm_Email)
        self.input_email_confirm_email.setObjectName(u"input_email_confirm_email")
        self.input_email_confirm_email.setFont(font2)

        self.horizontalLayout_5.addWidget(self.input_email_confirm_email, 0, Qt.AlignVCenter)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)

        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 1)
        self.horizontalLayout_5.setStretch(2, 2)
        self.horizontalLayout_5.setStretch(3, 1)

        self.gridLayout_9.addLayout(self.horizontalLayout_5, 2, 0, 1, 3)

        self.button_proceed_confirm_email = QPushButton(self.Confirm_Email)
        self.button_proceed_confirm_email.setObjectName(u"button_proceed_confirm_email")
        self.button_proceed_confirm_email.setFont(font)

        self.gridLayout_9.addWidget(self.button_proceed_confirm_email, 3, 1, 1, 1, Qt.AlignHCenter)

        self.button_reset_confirm_email = QPushButton(self.Confirm_Email)
        self.button_reset_confirm_email.setObjectName(u"button_reset_confirm_email")
        self.button_reset_confirm_email.setFont(font)
        self.button_reset_confirm_email.setStyleSheet(u"color: white; background-color: red")

        self.gridLayout_9.addWidget(self.button_reset_confirm_email, 3, 0, 1, 1, Qt.AlignLeft|Qt.AlignBottom)

        self.button_return_confirm_email = QPushButton(self.Confirm_Email)
        self.button_return_confirm_email.setObjectName(u"button_return_confirm_email")
        sizePolicy.setHeightForWidth(self.button_return_confirm_email.sizePolicy().hasHeightForWidth())
        self.button_return_confirm_email.setSizePolicy(sizePolicy)
        self.button_return_confirm_email.setMinimumSize(QSize(50, 50))
        self.button_return_confirm_email.setIcon(icon2)
        self.button_return_confirm_email.setIconSize(QSize(50, 50))
        self.button_return_confirm_email.setFlat(True)

        self.gridLayout_9.addWidget(self.button_return_confirm_email, 0, 0, 1, 1, Qt.AlignLeft|Qt.AlignTop)

        self.line_2 = QFrame(self.Confirm_Email)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_9.addWidget(self.line_2, 1, 1, 1, 1)


        self.gridLayout_10.addLayout(self.gridLayout_9, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.Confirm_Email)
        self.Login = QWidget()
        self.Login.setObjectName(u"Login")
        self.gridLayout_12 = QGridLayout(self.Login)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setSpacing(20)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(20, 20, 20, 20)
        self.button_proceed_login = QPushButton(self.Login)
        self.button_proceed_login.setObjectName(u"button_proceed_login")
        self.button_proceed_login.setFont(font)

        self.gridLayout_11.addWidget(self.button_proceed_login, 4, 1, 1, 1, Qt.AlignHCenter)

        self.line_5 = QFrame(self.Login)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.gridLayout_11.addWidget(self.line_5, 1, 1, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_8)

        self.label_1 = QLabel(self.Login)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setFont(font3)
        self.label_1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_1, 0, Qt.AlignRight|Qt.AlignVCenter)

        self.input_password_login = QLineEdit(self.Login)
        self.input_password_login.setObjectName(u"input_password_login")
        self.input_password_login.setFont(font2)

        self.horizontalLayout_7.addWidget(self.input_password_login, 0, Qt.AlignVCenter)

        self.button_password_login = QPushButton(self.Login)
        self.button_password_login.setObjectName(u"button_password_login")
        self.button_password_login.setEnabled(True)
        sizePolicy.setHeightForWidth(self.button_password_login.sizePolicy().hasHeightForWidth())
        self.button_password_login.setSizePolicy(sizePolicy)
        self.button_password_login.setMinimumSize(QSize(50, 50))
        icon3 = QIcon()
        icon3.addFile(resource_path("Images/EYE_PASSWORD.png"), QSize(), QIcon.Normal, QIcon.Off)
        self.button_password_login.setIcon(icon3)
        self.button_password_login.setIconSize(QSize(50, 50))
        self.button_password_login.setFlat(True)

        self.horizontalLayout_7.addWidget(self.button_password_login, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_9)

        self.horizontalLayout_7.setStretch(0, 2)
        self.horizontalLayout_7.setStretch(1, 2)
        self.horizontalLayout_7.setStretch(2, 4)
        self.horizontalLayout_7.setStretch(3, 1)
        self.horizontalLayout_7.setStretch(4, 1)

        self.gridLayout_11.addLayout(self.horizontalLayout_7, 3, 0, 1, 3)

        self.button_return_login = QPushButton(self.Login)
        self.button_return_login.setObjectName(u"button_return_login")
        sizePolicy.setHeightForWidth(self.button_return_login.sizePolicy().hasHeightForWidth())
        self.button_return_login.setSizePolicy(sizePolicy)
        self.button_return_login.setMinimumSize(QSize(50, 50))
        self.button_return_login.setIcon(icon2)
        self.button_return_login.setIconSize(QSize(50, 50))
        self.button_return_login.setFlat(True)

        self.gridLayout_11.addWidget(self.button_return_login, 0, 0, 1, 1, Qt.AlignLeft|Qt.AlignTop)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_6)

        self.label_16 = QLabel(self.Login)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font3)
        self.label_16.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_16, 0, Qt.AlignRight|Qt.AlignBottom)

        self.input_user_login = QLineEdit(self.Login)
        self.input_user_login.setObjectName(u"input_user_login")
        self.input_user_login.setFont(font2)

        self.horizontalLayout_6.addWidget(self.input_user_login, 0, Qt.AlignBottom)

        self.pushButton_10 = QPushButton(self.Login)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setEnabled(False)
        sizePolicy.setHeightForWidth(self.pushButton_10.sizePolicy().hasHeightForWidth())
        self.pushButton_10.setSizePolicy(sizePolicy)
        self.pushButton_10.setMinimumSize(QSize(50, 50))
        self.pushButton_10.setIconSize(QSize(50, 50))
        self.pushButton_10.setFlat(True)

        self.horizontalLayout_6.addWidget(self.pushButton_10, 0, Qt.AlignLeft)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_7)

        self.horizontalLayout_6.setStretch(0, 2)
        self.horizontalLayout_6.setStretch(1, 2)
        self.horizontalLayout_6.setStretch(2, 4)
        self.horizontalLayout_6.setStretch(3, 1)
        self.horizontalLayout_6.setStretch(4, 1)

        self.gridLayout_11.addLayout(self.horizontalLayout_6, 2, 0, 1, 3)

        self.label_13 = QLabel(self.Login)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font1)
        self.label_13.setAlignment(Qt.AlignCenter)

        self.gridLayout_11.addWidget(self.label_13, 0, 1, 1, 1, Qt.AlignHCenter)

        self.button_recover_login = QPushButton(self.Login)
        self.button_recover_login.setObjectName(u"button_recover_login")
        self.button_recover_login.setFont(font)

        self.gridLayout_11.addWidget(self.button_recover_login, 5, 1, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)


        self.gridLayout_12.addLayout(self.gridLayout_11, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.Login)
        self.Editor = QWidget()
        self.Editor.setObjectName(u"Editor")
        self.gridLayout_8 = QGridLayout(self.Editor)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setSpacing(20)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(20, 20, 20, 20)
        self.button_proceed_editor = QPushButton(self.Editor)
        self.button_proceed_editor.setObjectName(u"button_proceed_editor")
        self.button_proceed_editor.setFont(font)

        self.gridLayout_7.addWidget(self.button_proceed_editor, 3, 1, 1, 1, Qt.AlignHCenter)

        self.button_return_editor = QPushButton(self.Editor)
        self.button_return_editor.setObjectName(u"button_return_editor")
        sizePolicy.setHeightForWidth(self.button_return_editor.sizePolicy().hasHeightForWidth())
        self.button_return_editor.setSizePolicy(sizePolicy)
        self.button_return_editor.setMinimumSize(QSize(50, 50))
        self.button_return_editor.setIcon(icon2)
        self.button_return_editor.setIconSize(QSize(50, 50))
        self.button_return_editor.setFlat(True)

        self.gridLayout_7.addWidget(self.button_return_editor, 0, 0, 1, 1, Qt.AlignLeft|Qt.AlignTop)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.treeWidget = QTreeWidget(self.Editor)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1")
        self.treeWidget.setHeaderItem(__qtreewidgetitem)
        self.treeWidget.setObjectName(u"treeWidget")
        tree_widget_font = copy.copy(get_font())
        tree_widget_font.setPointSize(20)
        self.treeWidget.setFont(tree_widget_font)

        self.horizontalLayout_3.addWidget(self.treeWidget)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.button_add_editor = QToolButton(self.Editor)
        self.button_add_editor.setObjectName(u"button_add_editor")
        self.button_add_editor.setFont(font)
        self.button_add_editor.setPopupMode(QToolButton.InstantPopup)

        self.verticalLayout_2.addWidget(self.button_add_editor, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.button_remove_editor = QToolButton(self.Editor)
        self.button_remove_editor.setObjectName(u"button_remove_editor")
        self.button_remove_editor.setFont(font)
        self.button_remove_editor.setPopupMode(QToolButton.InstantPopup)
        self.button_remove_editor.setAutoRaise(False)

        self.verticalLayout_2.addWidget(self.button_remove_editor, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.horizontalLayout_3.setStretch(0, 3)
        self.horizontalLayout_3.setStretch(1, 1)

        self.gridLayout_7.addLayout(self.horizontalLayout_3, 2, 0, 1, 3)

        self.label_11 = QLabel(self.Editor)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font1)
        self.label_11.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.label_11, 0, 1, 1, 1, Qt.AlignHCenter)

        self.line_3 = QFrame(self.Editor)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout_7.addWidget(self.line_3, 1, 1, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_7, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.Editor)
        self.Tables = QWidget()
        self.Tables.setObjectName(u"Tables")
        self.gridLayout_6 = QGridLayout(self.Tables)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.tabWidget = QTabWidget(self.Tables)
        self.tabWidget.setObjectName(u"tabWidget")

        self.gridLayout_5.addWidget(self.tabWidget, 0, 0, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_5, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.Tables)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 27))
        font4 = copy.copy(get_font())
        font4.setPointSize(14)
        self.menubar.setFont(font4)
        self.menuData_Base = QMenu(self.menubar)
        self.menuData_Base.setObjectName(u"menuData_Base")
        self.menuSettings = QMenu(self.menubar)
        self.menuSettings.setObjectName(u"menuSettings")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuData_Base.menuAction())
        self.menubar.addSeparator()
        self.menubar.addSeparator()
        self.menubar.addSeparator()
        self.menubar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        system_tray = QSystemTrayIcon(MainWindow)
        system_tray.setToolTip(QCoreApplication.translate("MainWindow", u"Data Base Manager", None))
        system_tray.setIcon(QIcon(resource_path("Images/ENTER_DB.png")))
        system_tray.show()
        MenuItem = QMenu()
        MenuItem.addAction(QAction("Show", MainWindow, triggered=MainWindow.show))
        system_tray.activated.connect(MainWindow.show)
        MenuItem.addAction(QAction("Exit", MainWindow, triggered=MainWindow.close))
        system_tray.setContextMenu(MenuItem)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowIcon(QIcon(resource_path("Images/ENTER_DB.png")))
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Data Base Manager", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Import Existing Database", None))
        self.button_proceed_start.setText(QCoreApplication.translate("MainWindow", u"Proceed", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Encrypt Database", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Data Base Setup", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"No", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Yes", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"No", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Yes", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Data Base\n"
"Configuration", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Data Base File", None))
        self.button_browse_config.setText("")
        self.button_add_config.setText("")
        self.button_return_config.setText("")
        self.button_proceed_config.setText(QCoreApplication.translate("MainWindow", u"Proceed", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Email for access recovery:", None))
        self.input_email_config.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Data Base\n"
"Recovery", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Email:", None))
        self.input_email_confirm_email.setText("")
        self.button_proceed_confirm_email.setText(QCoreApplication.translate("MainWindow", u"Proceed", None))
        self.button_reset_confirm_email.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.button_return_confirm_email.setText("")
        self.button_proceed_login.setText(QCoreApplication.translate("MainWindow", u"Proceed", None))
        self.label_1.setText(QCoreApplication.translate("MainWindow", u"Password:", None))
        self.input_password_login.setText("")
        self.button_password_login.setText("")
        self.button_return_login.setText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Username:", None))
        self.input_user_login.setText("")
        self.pushButton_10.setText("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Data Base\n"
"Login", None))
        self.button_recover_login.setText(QCoreApplication.translate("MainWindow", u"Recover access", None))
        self.button_proceed_editor.setText(QCoreApplication.translate("MainWindow", u"Proceed", None))
        self.button_return_editor.setText("")
        self.button_add_editor.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.button_remove_editor.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Data Base\n"
"Editor", None))
        self.menuData_Base.setTitle(QCoreApplication.translate("MainWindow", u"Data Base", None))
        self.menuSettings.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
    # retranslateUi


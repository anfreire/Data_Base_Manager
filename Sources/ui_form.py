from imports import *

class Ui_Widget(object):
    '''
    Auto-generated code for the UI.
    '''
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(800, 600)
        Widget.setMinimumSize(QSize(800, 600))
        self.stackedWidget = QStackedLayout(Widget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 0, 836, 623))
        self.login = QWidget()
        self.login.setObjectName(u"login")
        self.gridLayout_2 = QGridLayout(self.login)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_login = QLabel(self.login)
        self.label_login.setObjectName(u"label_login")
        font = QFont()
        font.setFamilies([u"Ubuntu Thin"])
        font.setPointSize(90)
        self.label_login.setFont(font)
        self.label_login.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_login)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_13)

        self.verticalSpacer_4 = QSpacerItem(40, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.horizontalLayout_7.addItem(self.verticalSpacer_4)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.username = QLabel(self.login)
        self.username.setObjectName(u"username")
        font1 = QFont()
        font1.setFamilies([u"Ubuntu Thin"])
        font1.setPointSize(23)
        self.username.setFont(font1)
        self.username.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.username)

        self.username_input_login = QLineEdit(self.login)
        self.username_input_login.setObjectName(u"username_input_login")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.username_input_login.sizePolicy().hasHeightForWidth())
        self.username_input_login.setSizePolicy(sizePolicy)
        self.username_input_login.setMinimumSize(QSize(250, 30))
        font2 = QFont()
        font2.setFamilies([u"Ubuntu Thin"])
        font2.setPointSize(15)
        font2.setBold(False)
        self.username_input_login.setFont(font2)
        self.username_input_login.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.username_input_login)


        self.verticalLayout_3.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.password = QLabel(self.login)
        self.password.setObjectName(u"password")
        self.password.setFont(font1)
        self.password.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.password)

        self.password_input_login = QLineEdit(self.login)
        self.password_input_login.setObjectName(u"password_input_login")
        sizePolicy.setHeightForWidth(self.password_input_login.sizePolicy().hasHeightForWidth())
        self.password_input_login.setSizePolicy(sizePolicy)
        self.password_input_login.setMinimumSize(QSize(250, 30))
        self.password_input_login.setFont(font2)
        self.password_input_login.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.password_input_login)


        self.verticalLayout_3.addLayout(self.horizontalLayout_8)


        self.horizontalLayout_7.addLayout(self.verticalLayout_3)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_3)

        self.see_password_button = QPushButton(self.login)
        self.see_password_button.setObjectName(u"see_password_button")
        sizePolicy.setHeightForWidth(self.see_password_button.sizePolicy().hasHeightForWidth())
        self.see_password_button.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u"PNG/EYE_PASSWORD.png", QSize(), QIcon.Normal, QIcon.Off)
        self.see_password_button.setIcon(icon)
        self.see_password_button.setIconSize(QSize(40, 40))
        self.see_password_button.setFlat(True)

        self.verticalLayout_5.addWidget(self.see_password_button)


        self.horizontalLayout_7.addLayout(self.verticalLayout_5)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_14)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_19)

        self.authenticate_button_login = QPushButton(self.login)
        self.authenticate_button_login.setObjectName(u"authenticate_button_login")
        sizePolicy.setHeightForWidth(self.authenticate_button_login.sizePolicy().hasHeightForWidth())
        self.authenticate_button_login.setSizePolicy(sizePolicy)
        font3 = QFont()
        font3.setFamilies([u"Ubuntu Thin"])
        font3.setPointSize(21)
        self.authenticate_button_login.setFont(font3)

        self.horizontalLayout_10.addWidget(self.authenticate_button_login)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_20)


        self.verticalLayout_2.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_21)

        self.forgot_password_button_login = QPushButton(self.login)
        self.forgot_password_button_login.setObjectName(u"forgot_password_button_login")
        sizePolicy.setHeightForWidth(self.forgot_password_button_login.sizePolicy().hasHeightForWidth())
        self.forgot_password_button_login.setSizePolicy(sizePolicy)
        self.forgot_password_button_login.setFont(font3)

        self.horizontalLayout_11.addWidget(self.forgot_password_button_login)

        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_22)


        self.verticalLayout_2.addLayout(self.horizontalLayout_11)

        self.verticalLayout_2.setStretch(0, 20)
        self.verticalLayout_2.setStretch(1, 4)
        self.verticalLayout_2.setStretch(2, 4)
        self.verticalLayout_2.setStretch(3, 4)

        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.login)
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.stackedWidget_2 = QStackedLayout(self.home)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2.setGeometry(QRect(9, 9, 648, 484))
        self.tables = QWidget()
        self.tables.setObjectName(u"tables")
        self.gridLayout_5 = QGridLayout(self.tables)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, -1, -1)
        self.tabWidget = QTabWidget(self.tables)
        self.tabWidget.setObjectName(u"tabWidget")
        font4 = QFont()
        font4.setFamilies([u"Ubuntu Thin"])
        font4.setPointSize(17)
        font4.setBold(True)
        self.tabWidget.setFont(font4)

        self.horizontalLayout_3.addWidget(self.tabWidget)


        self.gridLayout_5.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)

        self.stackedWidget_2.addWidget(self.tables)
        self.home_db = QWidget()
        self.home_db.setObjectName(u"home_db")
        self.gridLayout_8 = QGridLayout(self.home_db)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(20, 20, 20, 20)
        self.logout_db_button = QPushButton(self.home_db)
        self.logout_db_button.setObjectName(u"logout_db_button")
        sizePolicy.setHeightForWidth(self.logout_db_button.sizePolicy().hasHeightForWidth())
        self.logout_db_button.setSizePolicy(sizePolicy)
        self.logout_db_button.setMinimumSize(QSize(50, 50))
        icon1 = QIcon()
        icon1.addFile(u"PNG/LOGOUT.png", QSize(), QIcon.Normal, QIcon.Off)
        self.logout_db_button.setIcon(icon1)
        self.logout_db_button.setIconSize(QSize(50, 50))
        self.logout_db_button.setFlat(True)

        self.horizontalLayout_12.addWidget(self.logout_db_button)

        self.email_label_config_3 = QLabel(self.home_db)
        self.email_label_config_3.setObjectName(u"email_label_config_3")
        self.email_label_config_3.setFont(font1)
        self.email_label_config_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_12.addWidget(self.email_label_config_3)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_7)

        self.line = QFrame(self.home_db)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_12.addWidget(self.line)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_8)

        self.email_label_config_2 = QLabel(self.home_db)
        self.email_label_config_2.setObjectName(u"email_label_config_2")
        self.email_label_config_2.setFont(font1)
        self.email_label_config_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_12.addWidget(self.email_label_config_2)

        self.enter_the_database_db_button = QPushButton(self.home_db)
        self.enter_the_database_db_button.setObjectName(u"enter_the_database_db_button")
        sizePolicy.setHeightForWidth(self.enter_the_database_db_button.sizePolicy().hasHeightForWidth())
        self.enter_the_database_db_button.setSizePolicy(sizePolicy)
        self.enter_the_database_db_button.setMinimumSize(QSize(50, 50))
        icon2 = QIcon()
        icon2.addFile(u"PNG/ENTER_DB.png", QSize(), QIcon.Normal, QIcon.Off)
        self.enter_the_database_db_button.setIcon(icon2)
        self.enter_the_database_db_button.setIconSize(QSize(50, 50))
        self.enter_the_database_db_button.setFlat(True)

        self.horizontalLayout_12.addWidget(self.enter_the_database_db_button)


        self.verticalLayout_16.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setSpacing(20)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(20, 20, 20, 20)
        self.settings_db_button = QPushButton(self.home_db)
        self.settings_db_button.setObjectName(u"settings_db_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.settings_db_button.sizePolicy().hasHeightForWidth())
        self.settings_db_button.setSizePolicy(sizePolicy1)
        font5 = QFont()
        font5.setFamilies([u"Ubuntu Thin"])
        font5.setPointSize(20)
        font5.setBold(True)
        self.settings_db_button.setFont(font5)

        self.horizontalLayout_21.addWidget(self.settings_db_button)

        self.edit_users_home_db_button = QPushButton(self.home_db)
        self.edit_users_home_db_button.setObjectName(u"edit_users_home_db_button")
        sizePolicy1.setHeightForWidth(self.edit_users_home_db_button.sizePolicy().hasHeightForWidth())
        self.edit_users_home_db_button.setSizePolicy(sizePolicy1)
        self.edit_users_home_db_button.setFont(font5)

        self.horizontalLayout_21.addWidget(self.edit_users_home_db_button)


        self.verticalLayout_16.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setSpacing(20)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(20, 20, 20, 20)
        self.backup_restore_db_button = QPushButton(self.home_db)
        self.backup_restore_db_button.setObjectName(u"backup_restore_db_button")
        sizePolicy1.setHeightForWidth(self.backup_restore_db_button.sizePolicy().hasHeightForWidth())
        self.backup_restore_db_button.setSizePolicy(sizePolicy1)
        self.backup_restore_db_button.setFont(font5)

        self.horizontalLayout_23.addWidget(self.backup_restore_db_button)

        self.edit_db_db_button = QPushButton(self.home_db)
        self.edit_db_db_button.setObjectName(u"edit_db_db_button")
        sizePolicy1.setHeightForWidth(self.edit_db_db_button.sizePolicy().hasHeightForWidth())
        self.edit_db_db_button.setSizePolicy(sizePolicy1)
        self.edit_db_db_button.setFont(font5)

        self.horizontalLayout_23.addWidget(self.edit_db_db_button)


        self.verticalLayout_16.addLayout(self.horizontalLayout_23)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setSpacing(20)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(20, 20, 20, 20)
        self.import_data_from_different_file_formats_home_db_button = QPushButton(self.home_db)
        self.import_data_from_different_file_formats_home_db_button.setObjectName(u"import_data_from_different_file_formats_home_db_button")
        sizePolicy1.setHeightForWidth(self.import_data_from_different_file_formats_home_db_button.sizePolicy().hasHeightForWidth())
        self.import_data_from_different_file_formats_home_db_button.setSizePolicy(sizePolicy1)
        self.import_data_from_different_file_formats_home_db_button.setFont(font5)

        self.horizontalLayout_20.addWidget(self.import_data_from_different_file_formats_home_db_button)

        self.export_data_specific_file_format_home_db_button = QPushButton(self.home_db)
        self.export_data_specific_file_format_home_db_button.setObjectName(u"export_data_specific_file_format_home_db_button")
        sizePolicy1.setHeightForWidth(self.export_data_specific_file_format_home_db_button.sizePolicy().hasHeightForWidth())
        self.export_data_specific_file_format_home_db_button.setSizePolicy(sizePolicy1)
        self.export_data_specific_file_format_home_db_button.setFont(font5)

        self.horizontalLayout_20.addWidget(self.export_data_specific_file_format_home_db_button)


        self.verticalLayout_16.addLayout(self.horizontalLayout_20)


        self.horizontalLayout_25.addLayout(self.verticalLayout_16)


        self.gridLayout_8.addLayout(self.horizontalLayout_25, 0, 0, 1, 1)

        self.stackedWidget_2.addWidget(self.home_db)
        self.stackedWidget.addWidget(self.home)
        self.config = QWidget()
        self.config.setObjectName(u"config")
        self.gridLayout = QGridLayout(self.config)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.return_button_config = QPushButton(self.config)
        self.return_button_config.setObjectName(u"return_button_config")
        icon3 = QIcon()
        icon3.addFile(u"PNG/BACK_ARROW.png", QSize(), QIcon.Normal, QIcon.Off)
        self.return_button_config.setIcon(icon3)
        self.return_button_config.setIconSize(QSize(40, 40))
        self.return_button_config.setFlat(True)

        self.verticalLayout_17.addWidget(self.return_button_config, 0, Qt.AlignLeft)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_6)


        self.horizontalLayout_24.addLayout(self.verticalLayout_17)

        self.label_config = QLabel(self.config)
        self.label_config.setObjectName(u"label_config")
        font6 = QFont()
        font6.setFamilies([u"Ubuntu Thin"])
        font6.setPointSize(75)
        self.label_config.setFont(font6)
        self.label_config.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_24.addWidget(self.label_config, 0, Qt.AlignHCenter)

        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.horizontalSpacer_12 = QSpacerItem(40, 40, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.verticalLayout_18.addItem(self.horizontalSpacer_12)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_18.addItem(self.verticalSpacer_7)


        self.horizontalLayout_24.addLayout(self.verticalLayout_18)

        self.horizontalLayout_24.setStretch(0, 1)
        self.horizontalLayout_24.setStretch(1, 10)
        self.horizontalLayout_24.setStretch(2, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_24)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.email_label_config = QLabel(self.config)
        self.email_label_config.setObjectName(u"email_label_config")
        self.email_label_config.setFont(font1)
        self.email_label_config.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.email_label_config)

        self.email_input_config = QLineEdit(self.config)
        self.email_input_config.setObjectName(u"email_input_config")
        sizePolicy.setHeightForWidth(self.email_input_config.sizePolicy().hasHeightForWidth())
        self.email_input_config.setSizePolicy(sizePolicy)
        self.email_input_config.setMinimumSize(QSize(350, 30))
        self.email_input_config.setFont(font2)
        self.email_input_config.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.email_input_config)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, -1, 50, -1)
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(50, -1, -1, -1)
        self.password_label_2 = QLabel(self.config)
        self.password_label_2.setObjectName(u"password_label_2")
        self.password_label_2.setFont(font1)
        self.password_label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_6.addWidget(self.password_label_2, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.browse_db_file_button = QPushButton(self.config)
        self.browse_db_file_button.setObjectName(u"browse_db_file_button")
        sizePolicy.setHeightForWidth(self.browse_db_file_button.sizePolicy().hasHeightForWidth())
        self.browse_db_file_button.setSizePolicy(sizePolicy)
        icon4 = QIcon()
        icon4.addFile(u"PNG/FOLDER.png", QSize(), QIcon.Normal, QIcon.Off)
        self.browse_db_file_button.setIcon(icon4)
        self.browse_db_file_button.setIconSize(QSize(40, 40))
        self.browse_db_file_button.setFlat(True)

        self.verticalLayout_6.addWidget(self.browse_db_file_button, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.horizontalLayout_4.addLayout(self.verticalLayout_6)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)

        self.listWidget = QListWidget(self.config)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_4.addWidget(self.listWidget)

        self.add_user_button = QPushButton(self.config)
        self.add_user_button.setObjectName(u"add_user_button")
        sizePolicy.setHeightForWidth(self.add_user_button.sizePolicy().hasHeightForWidth())
        self.add_user_button.setSizePolicy(sizePolicy)
        icon5 = QIcon()
        icon5.addFile(u"PNG/ADD_USER.webp", QSize(), QIcon.Normal, QIcon.Off)
        self.add_user_button.setIcon(icon5)
        self.add_user_button.setIconSize(QSize(40, 40))
        self.add_user_button.setFlat(True)

        self.horizontalLayout_4.addWidget(self.add_user_button)

        self.horizontalLayout_4.setStretch(0, 10)
        self.horizontalLayout_4.setStretch(1, 1)
        self.horizontalLayout_4.setStretch(2, 8)
        self.horizontalLayout_4.setStretch(3, 2)

        self.horizontalLayout_6.addLayout(self.horizontalLayout_4)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)

        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 5)
        self.horizontalLayout_6.setStretch(2, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_9)

        self.proceed_button_config = QPushButton(self.config)
        self.proceed_button_config.setObjectName(u"proceed_button_config")
        sizePolicy.setHeightForWidth(self.proceed_button_config.sizePolicy().hasHeightForWidth())
        self.proceed_button_config.setSizePolicy(sizePolicy)
        self.proceed_button_config.setFont(font3)

        self.horizontalLayout_5.addWidget(self.proceed_button_config)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_10)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.verticalLayout.setStretch(1, 2)
        self.verticalLayout.setStretch(2, 4)
        self.verticalLayout.setStretch(3, 2)

        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.config)
        self.database_editor = QWidget()
        self.database_editor.setObjectName(u"database_editor")
        self.gridLayout_4 = QGridLayout(self.database_editor)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, -1, -1, 20)
        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.return_button_confirm_email_2 = QPushButton(self.database_editor)
        self.return_button_confirm_email_2.setObjectName(u"return_button_confirm_email_2")
        self.return_button_confirm_email_2.setIcon(icon3)
        self.return_button_confirm_email_2.setIconSize(QSize(40, 40))
        self.return_button_confirm_email_2.setFlat(True)

        self.verticalLayout_21.addWidget(self.return_button_confirm_email_2, 0, Qt.AlignLeft)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_21.addItem(self.verticalSpacer_10)


        self.horizontalLayout_27.addLayout(self.verticalLayout_21)

        self.label_5 = QLabel(self.database_editor)
        self.label_5.setObjectName(u"label_5")
        font7 = QFont()
        font7.setFamilies([u"Ubuntu Thin"])
        font7.setPointSize(80)
        self.label_5.setFont(font7)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_27.addWidget(self.label_5, 0, Qt.AlignHCenter)

        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.horizontalSpacer_16 = QSpacerItem(40, 40, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.verticalLayout_22.addItem(self.horizontalSpacer_16)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_22.addItem(self.verticalSpacer_11)


        self.horizontalLayout_27.addLayout(self.verticalLayout_22)

        self.horizontalLayout_27.setStretch(0, 1)
        self.horizontalLayout_27.setStretch(1, 10)
        self.horizontalLayout_27.setStretch(2, 1)

        self.verticalLayout_7.addLayout(self.horizontalLayout_27)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setSpacing(20)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(20, -1, 0, 20)
        self.treeWidget = QTreeWidget(self.database_editor)
        self.treeWidget.setObjectName(u"treeWidget")

        self.horizontalLayout_18.addWidget(self.treeWidget)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setSpacing(20)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(20, 20, 20, 20)
        self.Add_table_button = QPushButton(self.database_editor)
        self.Add_table_button.setObjectName(u"Add_table_button")
        sizePolicy.setHeightForWidth(self.Add_table_button.sizePolicy().hasHeightForWidth())
        self.Add_table_button.setSizePolicy(sizePolicy)
        self.Add_table_button.setMinimumSize(QSize(190, 40))
        self.Add_table_button.setMaximumSize(QSize(190, 40))
        self.Add_table_button.setFont(font3)

        self.verticalLayout_10.addWidget(self.Add_table_button)

        self.Remove_Table_button = QPushButton(self.database_editor)
        self.Remove_Table_button.setObjectName(u"Remove_Table_button")
        sizePolicy.setHeightForWidth(self.Remove_Table_button.sizePolicy().hasHeightForWidth())
        self.Remove_Table_button.setSizePolicy(sizePolicy)
        self.Remove_Table_button.setMinimumSize(QSize(190, 40))
        self.Remove_Table_button.setMaximumSize(QSize(190, 40))
        font8 = QFont()
        font8.setFamilies([u"Ubuntu Thin"])
        font8.setPointSize(19)
        self.Remove_Table_button.setFont(font8)

        self.verticalLayout_10.addWidget(self.Remove_Table_button)

        self.Add_column_button = QPushButton(self.database_editor)
        self.Add_column_button.setObjectName(u"Add_column_button")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.Add_column_button.sizePolicy().hasHeightForWidth())
        self.Add_column_button.setSizePolicy(sizePolicy2)
        self.Add_column_button.setMinimumSize(QSize(190, 40))
        self.Add_column_button.setMaximumSize(QSize(190, 40))
        self.Add_column_button.setFont(font3)

        self.verticalLayout_10.addWidget(self.Add_column_button)

        self.Remove_column_button = QPushButton(self.database_editor)
        self.Remove_column_button.setObjectName(u"Remove_column_button")
        sizePolicy.setHeightForWidth(self.Remove_column_button.sizePolicy().hasHeightForWidth())
        self.Remove_column_button.setSizePolicy(sizePolicy)
        self.Remove_column_button.setMinimumSize(QSize(190, 40))
        self.Remove_column_button.setMaximumSize(QSize(190, 40))
        font9 = QFont()
        font9.setFamilies([u"Ubuntu Thin"])
        font9.setPointSize(17)
        self.Remove_column_button.setFont(font9)

        self.verticalLayout_10.addWidget(self.Remove_column_button)


        self.horizontalLayout_18.addLayout(self.verticalLayout_10)


        self.verticalLayout_7.addLayout(self.horizontalLayout_18)

        self.proceed_button_editor = QPushButton(self.database_editor)
        self.proceed_button_editor.setObjectName(u"proceed_button_editor")
        sizePolicy.setHeightForWidth(self.proceed_button_editor.sizePolicy().hasHeightForWidth())
        self.proceed_button_editor.setSizePolicy(sizePolicy)
        self.proceed_button_editor.setFont(font3)

        self.verticalLayout_7.addWidget(self.proceed_button_editor, 0, Qt.AlignHCenter)


        self.gridLayout_4.addLayout(self.verticalLayout_7, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.database_editor)
        self.start = QWidget()
        self.start.setObjectName(u"start")
        self.gridLayout_9 = QGridLayout(self.start)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(-1, -1, -1, 22)
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(20, 20, 20, 20)
        self.label_3 = QLabel(self.start)
        self.label_3.setObjectName(u"label_3")
        font10 = QFont()
        font10.setFamilies([u"Ubuntu Thin"])
        font10.setPointSize(63)
        self.label_3.setFont(font10)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_3)

        self.email_label_2 = QLabel(self.start)
        self.email_label_2.setObjectName(u"email_label_2")
        self.email_label_2.setFont(font1)
        self.email_label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.email_label_2)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setSpacing(20)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(20, 20, 20, 20)
        self.email_label_6 = QLabel(self.start)
        self.email_label_6.setObjectName(u"email_label_6")
        font11 = QFont()
        font11.setFamilies([u"Ubuntu Thin"])
        font11.setPointSize(25)
        self.email_label_6.setFont(font11)
        self.email_label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.email_label_6)

        self.already_have_db_file_chooser_start = QScrollBar(self.start)
        self.already_have_db_file_chooser_start.setObjectName(u"already_have_db_file_chooser_start")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.already_have_db_file_chooser_start.sizePolicy().hasHeightForWidth())
        self.already_have_db_file_chooser_start.setSizePolicy(sizePolicy3)
        self.already_have_db_file_chooser_start.setMinimumSize(QSize(350, 0))
        self.already_have_db_file_chooser_start.setMaximum(1)
        self.already_have_db_file_chooser_start.setPageStep(1)
        self.already_have_db_file_chooser_start.setOrientation(Qt.Horizontal)

        self.horizontalLayout_14.addWidget(self.already_have_db_file_chooser_start, 0, Qt.AlignHCenter)

        self.email_label_7 = QLabel(self.start)
        self.email_label_7.setObjectName(u"email_label_7")
        self.email_label_7.setMinimumSize(QSize(0, 0))
        font12 = QFont()
        font12.setFamilies([u"Ubuntu Thin"])
        font12.setPointSize(20)
        self.email_label_7.setFont(font12)
        self.email_label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.email_label_7)


        self.verticalLayout_8.addLayout(self.horizontalLayout_14)

        self.email_label_3 = QLabel(self.start)
        self.email_label_3.setObjectName(u"email_label_3")
        self.email_label_3.setFont(font1)
        self.email_label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.email_label_3)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setSpacing(20)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(20, 20, 20, 20)
        self.email_label_4 = QLabel(self.start)
        self.email_label_4.setObjectName(u"email_label_4")
        font13 = QFont()
        font13.setFamilies([u"Ubuntu Thin"])
        font13.setPointSize(18)
        self.email_label_4.setFont(font13)
        self.email_label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.email_label_4)

        self.encrypt_chooser_start = QScrollBar(self.start)
        self.encrypt_chooser_start.setObjectName(u"encrypt_chooser_start")
        sizePolicy3.setHeightForWidth(self.encrypt_chooser_start.sizePolicy().hasHeightForWidth())
        self.encrypt_chooser_start.setSizePolicy(sizePolicy3)
        self.encrypt_chooser_start.setMinimumSize(QSize(350, 0))
        self.encrypt_chooser_start.setMaximum(1)
        self.encrypt_chooser_start.setPageStep(1)
        self.encrypt_chooser_start.setOrientation(Qt.Horizontal)

        self.horizontalLayout_13.addWidget(self.encrypt_chooser_start, 0, Qt.AlignHCenter)

        self.email_label_5 = QLabel(self.start)
        self.email_label_5.setObjectName(u"email_label_5")
        self.email_label_5.setMinimumSize(QSize(0, 0))
        self.email_label_5.setFont(font11)
        self.email_label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.email_label_5)


        self.verticalLayout_8.addLayout(self.horizontalLayout_13)


        self.verticalLayout_9.addLayout(self.verticalLayout_8)

        self.proceed_button_start = QPushButton(self.start)
        self.proceed_button_start.setObjectName(u"proceed_button_start")
        sizePolicy.setHeightForWidth(self.proceed_button_start.sizePolicy().hasHeightForWidth())
        self.proceed_button_start.setSizePolicy(sizePolicy)
        self.proceed_button_start.setFont(font3)

        self.verticalLayout_9.addWidget(self.proceed_button_start, 0, Qt.AlignHCenter)


        self.gridLayout_9.addLayout(self.verticalLayout_9, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.start)
        self.reset = QWidget()
        self.reset.setObjectName(u"reset")
        self.gridLayout_3 = QGridLayout(self.reset)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.return_button_confirm_email = QPushButton(self.reset)
        self.return_button_confirm_email.setObjectName(u"return_button_confirm_email")
        self.return_button_confirm_email.setIcon(icon3)
        self.return_button_confirm_email.setIconSize(QSize(40, 40))
        self.return_button_confirm_email.setFlat(True)

        self.verticalLayout_19.addWidget(self.return_button_confirm_email, 0, Qt.AlignLeft)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_19.addItem(self.verticalSpacer_8)


        self.horizontalLayout_26.addLayout(self.verticalLayout_19)

        self.label_4 = QLabel(self.reset)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font7)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_26.addWidget(self.label_4, 0, Qt.AlignHCenter)

        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.horizontalSpacer_15 = QSpacerItem(40, 40, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.verticalLayout_20.addItem(self.horizontalSpacer_15)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_20.addItem(self.verticalSpacer_9)


        self.horizontalLayout_26.addLayout(self.verticalLayout_20)

        self.horizontalLayout_26.setStretch(0, 1)
        self.horizontalLayout_26.setStretch(1, 10)
        self.horizontalLayout_26.setStretch(2, 1)

        self.verticalLayout_4.addLayout(self.horizontalLayout_26)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalSpacer_29 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_29)

        self.main_label_email_confirm = QLabel(self.reset)
        self.main_label_email_confirm.setObjectName(u"main_label_email_confirm")
        font14 = QFont()
        font14.setFamilies([u"Ubuntu Thin"])
        font14.setPointSize(25)
        font14.setBold(False)
        self.main_label_email_confirm.setFont(font14)
        self.main_label_email_confirm.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_15.addWidget(self.main_label_email_confirm)

        self.horizontalSpacer_30 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_30)


        self.verticalLayout_4.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalSpacer_31 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_31)

        self.label_chooser = QLabel(self.reset)
        self.label_chooser.setObjectName(u"label_chooser")
        self.label_chooser.setFont(font1)
        self.label_chooser.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_16.addWidget(self.label_chooser)

        self.input_email_confirm = QLineEdit(self.reset)
        self.input_email_confirm.setObjectName(u"input_email_confirm")
        sizePolicy.setHeightForWidth(self.input_email_confirm.sizePolicy().hasHeightForWidth())
        self.input_email_confirm.setSizePolicy(sizePolicy)
        self.input_email_confirm.setMinimumSize(QSize(350, 30))
        self.input_email_confirm.setFont(font2)
        self.input_email_confirm.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_16.addWidget(self.input_email_confirm)

        self.horizontalSpacer_32 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_32)


        self.verticalLayout_4.addLayout(self.horizontalLayout_16)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalSpacer_33 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_33)

        self.confirm_email_button = QPushButton(self.reset)
        self.confirm_email_button.setObjectName(u"confirm_email_button")
        sizePolicy.setHeightForWidth(self.confirm_email_button.sizePolicy().hasHeightForWidth())
        self.confirm_email_button.setSizePolicy(sizePolicy)
        self.confirm_email_button.setFont(font3)

        self.horizontalLayout_17.addWidget(self.confirm_email_button)

        self.horizontalSpacer_34 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_34)


        self.verticalLayout_4.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(20)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(12, 10, 0, 12)
        self.reset_db_button_confirm_email = QPushButton(self.reset)
        self.reset_db_button_confirm_email.setObjectName(u"reset_db_button_confirm_email")
        sizePolicy.setHeightForWidth(self.reset_db_button_confirm_email.sizePolicy().hasHeightForWidth())
        self.reset_db_button_confirm_email.setSizePolicy(sizePolicy)
        self.reset_db_button_confirm_email.setFont(font3)

        self.horizontalLayout_2.addWidget(self.reset_db_button_confirm_email)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_6)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.horizontalLayout_2.addItem(self.verticalSpacer)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.verticalLayout_4.setStretch(1, 2)
        self.verticalLayout_4.setStretch(2, 2)
        self.verticalLayout_4.setStretch(3, 1)
        self.verticalLayout_4.setStretch(4, 2)

        self.gridLayout_3.addLayout(self.verticalLayout_4, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.reset)

        self.retranslateUi(Widget)

        self.stackedWidget.setCurrentIndex(3)
        self.stackedWidget_2.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Data Base", None))
        self.label_login.setText(QCoreApplication.translate("Widget", u"Data Base\n"
"Login", None))
        self.username.setText(QCoreApplication.translate("Widget", u"Username:", None))
        self.username_input_login.setText("")
        self.password.setText(QCoreApplication.translate("Widget", u" Password:", None))
        self.password_input_login.setText("")
        self.see_password_button.setText("")
        self.authenticate_button_login.setText(QCoreApplication.translate("Widget", u"Authenticate", None))
        self.forgot_password_button_login.setText(QCoreApplication.translate("Widget", u"I forgot the credentials", None))
        self.logout_db_button.setText("")
        self.email_label_config_3.setText(QCoreApplication.translate("Widget", u"Sign Out", None))
        self.email_label_config_2.setText(QCoreApplication.translate("Widget", u"Enter the Data Base", None))
        self.enter_the_database_db_button.setText("")
        self.settings_db_button.setText(QCoreApplication.translate("Widget", u"Configure \n"
"the program", None))
        self.edit_users_home_db_button.setText(QCoreApplication.translate("Widget", u"Edit Data\n"
"Base Users ", None))
        self.backup_restore_db_button.setText(QCoreApplication.translate("Widget", u"Backup/Restore\n"
" the Data Base", None))
        self.edit_db_db_button.setText(QCoreApplication.translate("Widget", u"Edit the \n"
"Data Base", None))
        self.import_data_from_different_file_formats_home_db_button.setText(QCoreApplication.translate("Widget", u"Import data from\n"
"different file formats ", None))
        self.export_data_specific_file_format_home_db_button.setText(QCoreApplication.translate("Widget", u"Export data in\n"
"different file formats ", None))
        self.return_button_config.setText("")
        self.label_config.setText(QCoreApplication.translate("Widget", u"Data Base\n"
"Configuration", None))
        self.email_label_config.setText(QCoreApplication.translate("Widget", u"Email for acess recovery:", None))
        self.email_input_config.setText("")
        self.password_label_2.setText(QCoreApplication.translate("Widget", u"Locate the \n"
"database file", None))
        self.browse_db_file_button.setText("")
        self.add_user_button.setText("")
        self.proceed_button_config.setText(QCoreApplication.translate("Widget", u"Proceed", None))
        self.return_button_confirm_email_2.setText("")
        self.label_5.setText(QCoreApplication.translate("Widget", u"Data Base\n"
"Editor", None))
        self.Add_table_button.setText(QCoreApplication.translate("Widget", u"Add Table", None))
        self.Remove_Table_button.setText(QCoreApplication.translate("Widget", u"Remove Table", None))
        self.Add_column_button.setText(QCoreApplication.translate("Widget", u"Add Column", None))
        self.Remove_column_button.setText(QCoreApplication.translate("Widget", u" Remove Column", None))
        self.proceed_button_editor.setText(QCoreApplication.translate("Widget", u"Proceed", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"Data Base Setup", None))
        self.email_label_2.setText(QCoreApplication.translate("Widget", u"Do you have a Data Base File already? (.db) ", None))
        self.email_label_6.setText(QCoreApplication.translate("Widget", u"Yes", None))
        self.email_label_7.setText(QCoreApplication.translate("Widget", u"No\n"
"(create one)", None))
        self.email_label_3.setText(QCoreApplication.translate("Widget", u"Do you want to encrypt the Data Base?", None))
        self.email_label_4.setText(QCoreApplication.translate("Widget", u"Yes\n"
"(Recommended)", None))
        self.email_label_5.setText(QCoreApplication.translate("Widget", u"No", None))
        self.proceed_button_start.setText(QCoreApplication.translate("Widget", u"Proceed", None))
        self.return_button_confirm_email.setText("")
        self.label_4.setText(QCoreApplication.translate("Widget", u"Data Base\n"
"Recovery", None))
        self.main_label_email_confirm.setText(QCoreApplication.translate("Widget", u"Enter the email address you\n"
"previously assigned for recovery. ", None))
        self.label_chooser.setText(QCoreApplication.translate("Widget", u"Email:", None))
        self.input_email_confirm.setText("")
        self.confirm_email_button.setText(QCoreApplication.translate("Widget", u"Recover the Database", None))
        self.reset_db_button_confirm_email.setText(QCoreApplication.translate("Widget", u"Reset the Database", None))
    # retranslateUi

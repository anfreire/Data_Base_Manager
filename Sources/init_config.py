'''
    @anfreire

    linktr.ee/anfreire
'''

from Sources.imports import *
'''
This module contains the code that initializes the configuration file.
Get the font from the configuration file.
All the program widgets will use this font.
'''

'''
    This condition checks if the configuration file exists.
    If it doesn't exist, it creates it.
'''
if not os.path.exists('config.ini'):
    config = configparser.ConfigParser()
    config['DEFAULT'] = {'current_theme': 'light',
                    'encryption': 'True',
                    'font': 'Arial',
                    'Shortcut +': 'Ctrl++',
                    'Shortcut -': 'Ctrl+-',}
    with open('config.ini', 'w') as configfile:
        config.write(configfile)

'''
    This function is used to get the font from the configuration file.
    This exception is used to check if the font setting in the configuration file is valid.
    If it is not valid, it will alert the user and use the default font.
    It is used all over the program.
'''
def get_font():
    try:
        config = configparser.ConfigParser()
        config.read('config.ini')
        font = config['DEFAULT']['font']
        font_size = 18
        costum_font = QFont(font, font_size)
    except:
        costum_font = QFont("Arial", 18)
        dialog = QMessageBox()
        dialog.setFont(costum_font)
        dialog.setModal(True)
        dialog.setStandardButtons(QMessageBox.Ok)
        dialog.setDefaultButton(QMessageBox.Ok)
        dialog.setIcon(QMessageBox.Critical)
        dialog.setWindowIcon(QMessageBox.Critical)
        dialog.setWindowTitle("Error")
        dialog.setText("Could not load the font {font}.\n The default font will be used instead.")
        dialog.exec_()
    return costum_font

'''
    This variable assigns the font to the variable costum_font.
    It is used all over the program, as the import of the module.
'''
costum_font = get_font()
        
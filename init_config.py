from imports import *

if not os.path.exists('config.ini'):
    config = configparser.ConfigParser()
    config['DEFAULT'] = {'current_theme': 'light',
                    'encryption': 'True',
                    'font': 'Arial',
                    'font_size': '16'}
    with open('config.ini', 'w') as configfile:
        config.write(configfile)
        
config = configparser.ConfigParser()
config.read('config.ini')
font = config['DEFAULT']['font']
font_size = int(config['DEFAULT']['font_size'])
try:
    costum_font = QFont(font, font_size)
except:
    dialog = QMessageBox()
    dialog.critical(None, "Error", f"Could not load the font {font}.\n The default font will be used instead.", QMessageBox.Ok)
    costum_font = QFont("Arial", 16)
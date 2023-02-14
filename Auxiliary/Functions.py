'''
    @anfreire

    linktr.ee/anfreire
'''

from Sources.imports import *

'''
    This module contains all the functions used in the program.
    It is imported in almost all the modules, if not all.
'''

'''
    This assignmenet is purely for documentation purposes.
'''
Data = TypeVar('Data')


def encrypt(data: str, key: bytes) -> bytes:
    '''
    Encrypt the data using the key
    This function returns a bytes object
    This function is auxiliary to the save_to_db function
    '''
    cipher = Fernet(key)
    encrypted_data = cipher.encrypt(data)
    return encrypted_data

def decrypt(encrypted_data: bytes, key: bytes) -> bytes:
    '''
    Decrypt the data using the key
    This function returns a bytes object
    This function is auxiliary to the retrieve_from_db function
    '''
    cipher = Fernet(key)
    decrypted_data = cipher.decrypt(encrypted_data)
    return decrypted_data

def save_to_db(data: Data) -> None:
    '''
    This function saves the encrypted loggin data to an SQLite3 database called log.db
    The data is encrypted using a generated key
    The key is stored in the same file in the last column
    '''
    key = Fernet.generate_key()
    encrypted_users = encrypt(str(data.users).encode(), key)
    encrypted_passwrds = encrypt(str(data.passwrds).encode(), key)
    encrypted_code = encrypt(data.code.encode(), key)
    encrypted_email = encrypt(data.email.encode(), key)
    encrypted_config = encrypt(str(data.config).encode(), key)
    if not os.path.exists('.bin'):
        os.mkdir('.bin')
    conn = sqlite3.connect('.bin/log.db')
    with conn:
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS data (users BLOB, passwrds BLOB, code BLOB, email BLOB, config BLOB, key BLOB)''')
        c.execute("INSERT INTO data (users, passwrds, code, email, config, key) VALUES (?, ?, ?, ?, ?, ?)", (encrypted_users, encrypted_passwrds, encrypted_code, encrypted_email, encrypted_config, key))
        conn.commit()

def retrieve_from_db() -> dict:
    '''
    This function retrieves the encrypted loggin data from the SQLite3 database called log.db
    The data is decrypted using the key
    This function returns a dictionary
    '''
    conn = sqlite3.connect('.bin/log.db')
    with conn:
        c = conn.cursor()
        c.execute("SELECT users, passwrds, code, email, config, key FROM data")
        result = c.fetchone()
        data = {
            'users': decrypt(result[0], result[5]).decode(),
            'passwrds': decrypt(result[1], result[5]).decode(),
            'code': decrypt(result[2], result[5]).decode(),
            'email': decrypt(result[3], result[5]).decode(),
            'config': decrypt(result[4], result[5]).decode()
        }
        return data
    
def encrypt_database(data: Data) -> None:
    '''
    This function encrypts the database using the Fernet algorithm.
    The key is derived from the the recovery code geneated at the first time the program is run and sent to the user's email.
    The key its stored in different encrypted database file called log.db, that contains the user loggin data.
    '''
    data.update_values(retrieve_from_db())
    db_file = '.bin/src.db'
    salt = b'\x9d\x01\x05\x08\x12\x08\x15\x19'
    kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256,
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )
    key = base64.urlsafe_b64encode(kdf.derive((data.code).encode()))
    
    f = Fernet(key)
    
    with open(db_file, 'rb') as fp:
            data = fp.read()
    
    encrypted_data = f.encrypt(data)

    with open(db_file, 'wb') as f:
        f.write(encrypted_data)
        
def decrypt_database(data: any) -> None:
    '''
    This function decrypts the database using the Fernet algorithm.
    The key is derived from the the recovery code geneated at the first time the program is run and sent to the user's email.
    The key its stored in different encrypted database file called log.db, that contains the user loggin data.
    '''
    data.update_values(retrieve_from_db())
    db_file = '.bin/src.db'
    salt = b'\x9d\x01\x05\x08\x12\x08\x15\x19'
    kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256,
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )
    key = base64.urlsafe_b64encode(kdf.derive((data.code).encode()))
    f = Fernet(key)
    with open(db_file, 'rb') as fp:
            data = fp.read()
    decrypted_data = f.decrypt(data)
    with open(db_file, 'wb') as fp:
        fp.write(decrypted_data)

def disconnect_button(button: QPushButton) -> QPushButton.clicked:
    '''
    Disconnects the button passed as argument from any signal.
    Returns the button.clicked signal
    '''
    try:
        button.clicked.disconnect()
    except:
        pass
    return button.clicked
    
def send_email(data: Data, email_from: str, password: str) -> None:
    '''
    Sends an email using the SMTP protocol
    '''
    msg = EmailMessage()
    msg.set_content(f"Your verification code is: {data.code}.\n Please, do not reply to this email.")
    msg['Subject'] = 'Data Base Confirmation Code'
    msg['From'] = email_from
    msg['To'] = data.email
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email_from, password)
    server.send_message(msg)
    server.quit()
    
def is_email_valid(email: str) -> bool:
    '''
    Checks if the email is valid
    Returns True if it is valid, False otherwise
    Uses a regular expression
    '''
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    match = re.match(pattern, email)
    if match:
        return True
    else:
        return False

def create_folder(name: str) -> None:
    '''
    This function creates a hidden folder with the name passed as argument.
    If the folder already exists, it does nothing.
    '''
    directory = name
    if not os.path.exists(directory):
        os.mkdir(directory)
        if platform.system() == "Windows":
            os.system(f'attrib +h {directory}')
    
def remove_folder(name: str) -> None:
    '''
    This function removes a folder with the name passed as argument.
    If the folder does not exist, it does nothing.
    '''
    directory = name
    if os.path.exists(directory):
        shutil.rmtree(directory)

def check_db_files_in_folder(name: str) -> None:
    '''
    This function checks if there are any .db files in the folder passed as argument.
    If there are, it returns True.
    '''
    return any(glob.glob(os.path.join(name, "*.db")))

def write_invisible_file(file_name : str) -> None:
    '''
    This function creates a hidden file with the name passed as argument.
    If has protection against system differences.
    '''
    file_path = ".bin/" + file_name
    with open(file_path, 'w') as f:
        f.write(" ")
    if platform.system() == "Windows":
        os.system(f'attrib +h {file_path}')
    elif platform.system() == "Linux":
        os.rename(file_path, ".bin/." + file_name)
    
def check_invisible_file(file_name : str) -> bool:
    '''
    This function checks if there is a hidden file with the name passed as argument.
    If has protection against system differences.
    '''
    if platform.system() == "Linux":
        file_name = "." + file_name
    file_path = ".bin/" + file_name
    return os.path.exists(file_path) and not os.path.isfile(file_path + '/' + file_name)

def get_initial_fonts_widgets(widgets: list) -> dict:
    '''
    This function returns a dictionary with the initial font of each widget passed as argument.
    '''
    intial_font = {}
    
    for i, widget in enumerate(widgets):
        try:
            intial_font[i] = {"widget": widget, "initial_font": widget.font()}
        except:
            continue
    return intial_font

def euler_function(x: float) -> float:
    '''
    This function is used to make the font size grow slower.
    Its used in the resize_widgets function.
    With the euler number, i could get this function to first return a value close to 1, and then to return a value close to 0.7, as the font size grows.
    '''
    return 0.99 - 0.29 * (1 - math.exp(-x / 20.0))

def resize_widgets(self, widgets: dict) -> None:
    '''
    This function resizes the widgets passed as argument.
    It uses the initial font of each widget to calculate the new font size.
    It also uses the euler function to make the font size grow slower.
    Its called every time the window is resized.
    The event ResizeEvent is used to call this function.
    '''
    for widget in widgets.values():
        point_per_width = self.initial_width / widget["initial_font"].pointSizeF()
        new_font = widget['widget'].font()
        new_font_size = (self.width() / point_per_width)
        if int(new_font_size) > int(widget["initial_font"].pointSizeF()):
            new_font_size = new_font_size * euler_function(new_font_size - widget["initial_font"].pointSizeF())
        new_font.setPointSizeF(new_font_size)
        widget['widget'].setFont(new_font)
        
def show_dialog(parent: QWidget, type: str, text: str, font) -> None:
    '''
    This function shows a dialog with the text passed as argument.
    The type of dialog is passed as argument.
    The font is passed as argument.
    '''
    dialog = QMessageBox(parent)
    dialog.setFont(font)
    dialog.setModal(True)
    dialog.setStandardButtons(QMessageBox.Ok)
    dialog.setDefaultButton(QMessageBox.Ok)
    dialog.setWindowIcon(QIcon(resource_path("Images/ENTER_DB.png")))
    if type.lower() == "error":
        dialog.setIcon(QMessageBox.Icon.Critical)
        dialog.setWindowTitle("Error")
    elif type.lower() == "warning":
        dialog.setIcon(QMessageBox.Icon.Warning)
        dialog.setWindowTitle("Warning")
    elif type.lower() == "info":
        dialog.setIcon(QMessageBox.Icon.Information)
        dialog.setWindowTitle("Info")
    dialog.setText(text)
    dialog.exec_()
    
def show_question(parent: QWidget, type: str, text: str, font) -> bool:
    '''
    This function shows a question dialog with the text passed as argument.
    The type of dialog is passed as argument.
    The font is passed as argument.
    Returns True if the user clicks Yes, False otherwise.
    '''
    dialog = QMessageBox(parent)
    dialog.setFont(font)
    dialog.setModal(True)
    dialog.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    dialog.setDefaultButton(QMessageBox.No)
    dialog.setWindowIcon(QIcon(resource_path("Images/ENTER_DB.png")))
    if type.lower() == "question":
        dialog.setIcon(QMessageBox.Icon.Question)
        dialog.setWindowTitle("Question")
    elif type.lower() == "warning":
        dialog.setIcon(QMessageBox.Icon.Warning)
        dialog.setWindowTitle("Warning")
    dialog.setText(text)
    return dialog.exec_() == QMessageBox.Yes
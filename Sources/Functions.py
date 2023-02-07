from imports import *
Data = TypeVar('Data') # To prevent circular imports


'''

Encrypts and decrypts the data using the Fernet algorithm.

'''
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



'''

Auxiliary functions.

'''

def disconnect_button(button: QPushButton) -> None:
    '''
    Disconnects the button passed as argument from any signal.
    '''
    try:
        button.clicked.disconnect()
    except:
        pass
    
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
    This function creates a folder with the name passed as argument.
    If the folder already exists, it does nothing.
    '''
    directory = name
    if not os.path.exists(directory):
        os.mkdir(directory)
    
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



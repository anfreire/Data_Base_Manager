'''
    @anfreire

    linktr.ee/anfreire
'''

'''
    This file contains all the imports used in the project.
    It is used to make the code more readable and easier to maintain.
'''
import re
import io
import os
import sys
import ast
import csv
import json
import math
import copy
import glob
import time
import shutil
import ctypes
import string
import base64
import random
import smtplib
import sqlite3
import platform
import openpyxl
import datetime
import schedule
import dicttoxml
import subprocess
import qdarktheme
import configparser
import pandas as pd
from pathlib import Path
from typing import TypeVar
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from cryptography.fernet import Fernet
from email.message import EmailMessage
from PySide6 import QtCore, QtGui, QtWidgets
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

'''
    This function is used to get the path of local files.
    It is used mainly to the pyinstaller compilation.
'''
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
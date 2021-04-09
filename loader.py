import zipfile
from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog
from tkinter import font
from random import randrange
from pygame import mixer
import json
import time
import sqlite3


from music import music
from config.default import *
from lang.init import *
from extract.base import *
from extract.msg import *
from extract.ui import *
from lang.ui import *
from music.music import * 
from home.main import *
from home.login import *
from db.crud import*
from db.optimize import *
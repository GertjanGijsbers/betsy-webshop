__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"

from models import *
from create_database import *
import os
from peewee import * 
from datetime import datetime

# create database when this doesn't excists
if os.path.exists('webshop.db') == False:
    create_database()

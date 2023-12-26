import mysql.connector
import os
from dotenv import load_dotenv
import re

load_dotenv()


def connection_db():
    cnx = mysql.connector.connect(
        user=os.getenv("USER"),
        password=os.getenv("PASSWORD"),
        host=os.getenv("HOST"),
        database=os.getenv("DATABASE"),
    )
    return cnx


def is_correct_url(user_url):
    reg = r"https?:\/\/www\..+\/.*"
    is_url = bool(re.search(reg, user_url))
    return is_url

import mysql.connector
import os
from dotenv import load_dotenv
import re

load_dotenv()


def connection_db():
    if os.getenv("TESTING") == "True":
        cnx = mysql.connector.connect(
            user=os.getenv("USER_TEST"),
            password=os.getenv("PASSWORD_TEST"),
            host=os.getenv("HOST_TEST"),
            database=os.getenv("DATABASE_TEST"),
        )
        # yield cnx
        # cnx.close()
        return cnx
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

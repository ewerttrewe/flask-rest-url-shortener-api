# conftest.py
# conftest.py file:
import pytest
import mysql.connector
import os

from api.api import app
from dotenv import load_dotenv
from flask import Flask

load_dotenv()


@pytest.fixture()
def set_up_database_connection():
    cnx = mysql.connector.connect(
        user=os.getenv("USER_TEST"),
        password=os.getenv("PASSWORD_TEST"),
        host=os.getenv("HOST_TEST"),
        database=os.getenv("DATABASE_TEST"),
    )
    yield cnx
    cnx.close()


@pytest.fixture()
def client():
    with app.test_client() as client:
        yield client


# @pytest.fixture
# def tear_down_database_connection():
#     pass

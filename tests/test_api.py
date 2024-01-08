# test_api.py
# test_api.py file:
import pytest
from unittest.mock import patch
from conftest import client, set_up_database_connection
import json
import os


class TestUrlShortenerAPI:
    def test_post(self, client, set_up_database_connection):
        dummy_data = {"longUrl": "https://www.facebook.com/"}
        os.environ["TESTING"] = "True"
        test_db_connection = set_up_database_connection
        # with patch("api.api.connection_db", return_value=test_db_connection):
        #     response = client.post("/api/post-org-url", json=dummy_data)
        response = client.post("/api/post-org-url", json=dummy_data)
        assert response.status_code == 200

    def test_get(self):
        pass

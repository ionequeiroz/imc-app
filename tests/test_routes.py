import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app

from app import app

def test_index_get():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code== 200

def test_index_post():
    client = app.test_client()
    response = client.get('/', data={"peso": "70", "altura": "1.75"})
    assert response.status_code == 200
    assert b"IMC" in response.data
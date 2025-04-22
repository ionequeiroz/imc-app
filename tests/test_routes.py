import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app


def test_index_get():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200


def test_index_post():
    client = app.test_client()
    response = client.post('/', data={"peso": "70", "altura": "1.75"})
    assert response.status_code == 200
    assert b"IMC" in response.data


def test_index_post_sem_peso():
    client = app.test_client()
    response = client.post('/', data={'altura': '1.75'}) #tese Discord
    assert response.status_code == 200
    assert b"Por favor, preencha todos os campos" in response.data


def test_index_post_sem_altura():
    client = app.test_client()
    response = client.post('/', data={'peso': '70'})
    assert response.status_code == 200
    assert b"Por favor, preencha todos os campos" in response.data


def test_index_post_valores_invalidos():
    client = app.test_client()
    response = client.post('/', data={'peso': 'abc', 'altura': 'xyz'})
    assert response.status_code == 200
    assert b"Insira valores num" in response.data


def test_index_post_com_zero():
    client = app.test_client()
    response = client.post('/', data={'peso': '0', 'altura': '0'})
    assert response.status_code == 200
    assert b"maiores que zero" in response.data or b"Erro" in response.data


def test_index_post_valores_negativos():
    client = app.test_client()
    response = client.post('/', data={'peso': '-70', 'altura': '-1.75'})
    assert response.status_code == 200
    assert b"maiores que zero" in response.data or b"Erro" in response.data

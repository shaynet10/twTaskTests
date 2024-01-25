from support.http_requests import http_get,http_put,http_post,http_delete
from support.general import is_valid_json

username='admin'
password='admin'


def test_valid_response():
    response = http_get('http://localhost:8000/players?1=1&page=1', username, password)
    assert response.status_code == 200
    assert is_valid_json(response.content) == True

def test_delete_doesnt_return_data():
    response = http_delete('http://localhost:8000/players?1=1&page=1', username, password)
    assert is_valid_json(response.content) == False

def test_post_doesnt_return_data():
    response = http_post('http://localhost:8000/players?1=1&page=1', username, password)
    assert is_valid_json(response.content) == False

def test_put_doesnt_return_data():
    response = http_put('http://localhost:8000/players?1=1&page=1', username, password)
    assert is_valid_json(response.content) == False

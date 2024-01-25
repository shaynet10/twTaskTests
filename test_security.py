from support.http_requests import http_get
from support.general import is_valid_json

username='admin'
password='admin'
url_page1='http://localhost:8000/players?page=1'
url_page_big_query='http://localhost:8000/players?page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&page=1&'

def test_cannot_get_data_for_password_admin2():
    response = http_get(url_page1, username, 'admin2')
    assert is_valid_json(response.content) == False, 'data should be empty for wrong password'

def test_cannot_get_data_for_password_user():
    response = http_get(url_page1, username, 'user')
    assert is_valid_json(response.content) == False, 'data should be empty for wrong password'

def test_cannot_get_data_for_password_space():
    response = http_get(url_page1, username, ' ')
    assert is_valid_json(response.content) == False, 'data should be empty for wrong password'

def test_cannot_get_data_for_empty_password():
    response = http_get(url_page1, username, '')
    assert is_valid_json(response.content) == False, 'data should be empty for empty password'

def test_big_query_doesnt_return_data():
    response = http_get(url_page_big_query, username, password)
    assert is_valid_json(response.content) == False, 'data should be empty for big query: ' + url_page_big_query

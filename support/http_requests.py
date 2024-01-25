# http_request.py
import requests

def http_get(url, username, password):
    response = requests.get(url, auth=(username, password))
    return response

def http_post(url, username, password):
    response = requests.post(url, auth=(username, password))
    return response

def http_put(url, username, password):
    response = requests.put(url, auth=(username, password))
    return response

def http_delete(url, username, password):
    response = requests.delete(url, auth=(username, password))
    return response


def json_http_get(url, username, password):
    response = http_get(url, username, password)
    data = response.json()
    return data
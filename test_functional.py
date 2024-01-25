from support.http_requests import json_http_get
from support.general import is_valid_json

username='admin'
password='admin'
url_page1='http://localhost:8000/players?page=1'
url_page2='http://localhost:8000/players?page=2'
url_pageHugeNumber='http://localhost:8000/players?page=1000000000000000000';
url_pageWithNullNames='http://localhost:8000/players?page=17';

def assert_no_empty_name(obj):
    assert 'Name' in obj, "Name doesn't exist in player"
    assert obj['Name'] != '', "player " + str(obj['ID']) + " has an empty name"

def assert_valid_id(obj):
    assert 'ID' in obj, "ID doesn't exist in player"
    assert isinstance(obj['ID'], (int)), str(obj['ID']) + " is not an int"
    assert obj['ID'] >= 0, 'ID < 0, which is not a valid id'

def test_no_empty_name():
    data = json_http_get(url_page1, username, password)
    for player in data:
       assert_no_empty_name(player)

def test_valid_ids():
    data = json_http_get(url_page1, username, password)
    for player in data:
        assert_valid_id(player)

def test_the_same_results_for_the_same_call():
    data1 = json_http_get(url_page1, username, password)
    data2 = json_http_get(url_page1, username, password)
    assert data1 == data2

def test_that_every_name_appear_once():
    data = json_http_get(url_page1, username, password)
    names = set()
    for player in data:
        if player['Name'] != '':
            is_in_set = player['Name'] in names
            assert is_in_set == False, player['Name'] + ' exists twice in ' + str(data)
            names.add(player['Name'])

def test_no_missing_values_between_calls():
    data1 = json_http_get(url_page1, username, password)
    data2 = json_http_get(url_page2, username, password)
    lastId1 = data1[len(data1) - 1]['ID']
    firstId2 = data2[0]['ID']
    assert int(lastId1) + 1 == int(firstId2)

def test_name_doesnt_appear_in_two_calls():
    data1 = json_http_get(url_page1, username, password)
    data2 = json_http_get(url_page2, username, password)
    names1 = set()
    for player in data1:
        names1.add(player['Name'])

    for player in data2:
        if player['Name'] != '':
            in_set = player['Name'] in names1
            assert in_set == False, (player['Name'] +
                                     ' from page 2, exists also in page 1 DATA1: ' +
                                     str(data1) +
                                     ' DATA2: ' +
                                     str(data2))


def test_huge_page_number_Should_not_return_data():
    data = json_http_get(url_pageHugeNumber, username, password)
    if isinstance(data, list):
        assert len(data) == 0, url_pageHugeNumber + ' should not return data'


def test_null_data_should_not_be_in_names():
    data = json_http_get(url_pageWithNullNames, username, password)
    for player in data:
        assert player['Name'] != 'null', 'Player ' + str(player['ID']) + ' has name = "null"'
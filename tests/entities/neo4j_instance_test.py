# pytest読み込み
import pytest
import datetime

import entities
from entities.neo4j_instance import Neo4jInstance

@pytest.fixture
def test_data():
    return {
        'int_key': 1,
        'float_key': 1.8,
        'str_key': 'str',
        'bool_true_key': True,
        'bool_false_key': False,
        'date_key': '2018-03-21',
        'datetime_key': '2018-03-21T01:01:01+0900',
        'none_key': None,
    }

###################################################
# Premitive
###################################################
def test_set_now(test_data):
    my_instance = Neo4jInstance(properties = test_data)
    my_instance.set_now()
    assert isinstance(my_instance.now, datetime.datetime)

###################################################
# Public Use
###################################################
def test_init(mocker, test_data):
    neo4j_instance = Neo4jInstance(properties = test_data)

    assert isinstance(neo4j_instance.properties['int_key'], entities.neo4j_property_int.Neo4jPropertyInt)
    assert isinstance(neo4j_instance.properties['float_key'], entities.neo4j_property_float.Neo4jPropertyFloat)
    assert isinstance(neo4j_instance.properties['str_key'], entities.neo4j_property_str.Neo4jPropertyStr)
    assert isinstance(neo4j_instance.properties['bool_true_key'], entities.neo4j_property_bool.Neo4jPropertyBool)
    assert neo4j_instance.properties['bool_true_key'].value == True
    assert isinstance(neo4j_instance.properties['bool_false_key'], entities.neo4j_property_bool.Neo4jPropertyBool)
    assert neo4j_instance.properties['bool_false_key'].value == False
    assert isinstance(neo4j_instance.properties['date_key'], entities.neo4j_property_date.Neo4jPropertyDate)
    assert isinstance(neo4j_instance.properties['datetime_key'], entities.neo4j_property_datetime.Neo4jPropertyDatetime)
    assert 'none_key' not in neo4j_instance.properties
    assert isinstance(neo4j_instance.properties['created'], entities.neo4j_property_datetime.Neo4jPropertyDatetime)
    assert isinstance(neo4j_instance.properties['modified'], entities.neo4j_property_datetime.Neo4jPropertyDatetime)

###################################################
# Public Use
###################################################
def test_encypher(test_data):
    expected = 'int_key: 1, float_key: 1.8, str_key: "str", bool_true_key: True, bool_false_key: False, date_key: date("2018-03-21"), datetime_key: datetime("2018-03-21T01:01:01+0900"), created: datetime("2020-08-14T02:12:08+0900"), modified: datetime("2020-08-14T02:12:08+0900")'

    # Set the fixed created, modified values to match the expected data
    test_data['created'] = "2020-08-14T02:12:08+0900"
    test_data['modified'] = "2020-08-14T02:12:08+0900"
    neo4j_instance = Neo4jInstance(properties = test_data)
    result = neo4j_instance.encypher()
    assert result == expected

    neo4j_instance = Neo4jInstance(properties = test_data)
    result = neo4j_instance.encypher(True)
    assert result == '{ ' + expected + ' }'

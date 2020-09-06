# pytest読み込み
import pytest

import entities
from entities.node import Node

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
# Public Use
###################################################
def test_init(test_data):
    labels = ['Person', 'Company']
    node = Node(labels, properties = test_data)

    assert node.labels == labels
    assert isinstance(node.properties['int_key'], entities.neo4j_property_int.Neo4jPropertyInt)
    assert isinstance(node.properties['float_key'], entities.neo4j_property_float.Neo4jPropertyFloat)
    assert isinstance(node.properties['str_key'], entities.neo4j_property_str.Neo4jPropertyStr)
    assert isinstance(node.properties['bool_true_key'], entities.neo4j_property_bool.Neo4jPropertyBool)
    assert node.properties['bool_true_key'].value == True
    assert isinstance(node.properties['bool_false_key'], entities.neo4j_property_bool.Neo4jPropertyBool)
    assert node.properties['bool_false_key'].value == False
    assert isinstance(node.properties['date_key'], entities.neo4j_property_date.Neo4jPropertyDate)
    assert isinstance(node.properties['datetime_key'], entities.neo4j_property_datetime.Neo4jPropertyDatetime)
    assert 'none_key' not in node.properties
    assert isinstance(node.properties['created'], entities.neo4j_property_datetime.Neo4jPropertyDatetime)
    assert isinstance(node.properties['modified'], entities.neo4j_property_datetime.Neo4jPropertyDatetime)


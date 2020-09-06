# pytest読み込み
import pytest

import entities
from entities.relationship_frame import RelationshipFrame

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
    rel_type = 'RELTYPE'
    target_fields_in = 'hoge'
    target_values_in = 'hage'
    target_fields_out = 'foo'
    target_values_out = 'bar'
    directed = True
    relationship = RelationshipFrame(rel_type, target_fields_in, target_values_in, target_fields_out, target_values_out, properties = test_data, directed = directed)

    assert relationship.type == rel_type
    assert relationship.target_fields_in == target_fields_in
    assert relationship.target_values_in == target_values_in
    assert relationship.target_fields_out == target_fields_out
    assert relationship.target_values_out == target_values_out
    assert isinstance(relationship.properties['int_key'], entities.neo4j_property_int.Neo4jPropertyInt)
    assert isinstance(relationship.properties['float_key'], entities.neo4j_property_float.Neo4jPropertyFloat)
    assert isinstance(relationship.properties['str_key'], entities.neo4j_property_str.Neo4jPropertyStr)
    assert isinstance(relationship.properties['bool_true_key'], entities.neo4j_property_bool.Neo4jPropertyBool)
    assert relationship.properties['bool_true_key'].value == True
    assert isinstance(relationship.properties['bool_false_key'], entities.neo4j_property_bool.Neo4jPropertyBool)
    assert relationship.properties['bool_false_key'].value == False
    assert isinstance(relationship.properties['date_key'], entities.neo4j_property_date.Neo4jPropertyDate)
    assert isinstance(relationship.properties['datetime_key'], entities.neo4j_property_datetime.Neo4jPropertyDatetime)
    assert 'none_key' not in relationship.properties
    assert isinstance(relationship.properties['created'], entities.neo4j_property_datetime.Neo4jPropertyDatetime)
    assert isinstance(relationship.properties['modified'], entities.neo4j_property_datetime.Neo4jPropertyDatetime)
    assert relationship.directed

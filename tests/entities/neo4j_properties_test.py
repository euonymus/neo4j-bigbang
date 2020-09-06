# pytest読み込み
import pytest
import datetime

import entities
from entities.neo4j_properties import generalization, neo4j_properties

def test_generalization():
    none_result = generalization('foo', [1,2,3])
    assert none_result is False

    int_result = generalization('foo', 1)
    assert isinstance(int_result, entities.neo4j_property_int.Neo4jPropertyInt)
    assert int_result.value == 1

    int_result2 = generalization('foo', 1.00000000000000)
    assert isinstance(int_result, entities.neo4j_property_int.Neo4jPropertyInt)
    assert int_result2.value == 1

    float_result = generalization('foo', 1.8)
    assert isinstance(float_result, entities.neo4j_property_float.Neo4jPropertyFloat)
    assert float_result.value == 1.8

    true_result = generalization('foo', True)
    assert isinstance(float_result, entities.neo4j_property_bool.Neo4jPropertyBool)
    assert true_result.value

    true_result2 = generalization('foo', 'True')
    assert isinstance(true_result2, entities.neo4j_property_bool.Neo4jPropertyBool)
    assert true_result2.value

    false_result = generalization('foo', False)
    assert isinstance(false_result, entities.neo4j_property_bool.Neo4jPropertyBool)
    assert not false_result.value

    false_result2 = generalization('foo', 'False')
    assert isinstance(false_result2, entities.neo4j_property_bool.Neo4jPropertyBool)
    assert not false_result2.value

    str_result = generalization('foo', 'str')
    assert isinstance(str_result, entities.neo4j_property_str.Neo4jPropertyStr)
    assert str_result.value == 'str'

    date_result = generalization('foo', '2015-07-15')
    assert isinstance(date_result, entities.neo4j_property_date.Neo4jPropertyDate)
    assert date_result.value == datetime.datetime.strptime('2015-07-15', '%Y-%m-%d').date()

    datetime_result = generalization('foo', '2015-07-15T10:37:34+0900')
    assert isinstance(datetime_result, entities.neo4j_property_datetime.Neo4jPropertyDatetime)
    assert datetime_result.value == datetime.datetime.strptime('2015-07-15 10:37:34', '%Y-%m-%d %H:%M:%S')


def test_neo4j_properties():
    properties = {
        'a': 1,
        'b': '2',
        'c': '2015-07-15 10:37:34',
        'd': '2018-03-21'
    }
    result = neo4j_properties(properties)
    assert isinstance(result['a'], entities.neo4j_property_int.Neo4jPropertyInt)
    assert isinstance(result['b'], entities.neo4j_property_str.Neo4jPropertyStr)
    assert isinstance(result['c'], entities.neo4j_property_datetime.Neo4jPropertyDatetime)
    assert isinstance(result['d'], entities.neo4j_property_date.Neo4jPropertyDate)

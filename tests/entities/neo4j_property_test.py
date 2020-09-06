# pytest読み込み
import pytest
import datetime

from entities.neo4j_property import Neo4jProperty

###################################################
# Run Time Converter
###################################################
# parametized fixture
@pytest.mark.parametrize(( "value, expected"), [
    (None, 'null'),
    (1.8, '"1.8"'),
    ('str', '"str"'),
    (True, '"True"'),
    (False, '"False"'),
    (0, '"0"'),
    ('0', '"0"'),
])
def test_enstring(value, expected):
    neo4j_property =  Neo4jProperty('foo', value)
    assert neo4j_property.enstring() == expected

# parametized fixture
@pytest.mark.parametrize(( "key, value, expected"), [
    ("foo", 1.8, 'foo: "1.8"'),
    ("foo", 'str', 'foo: "str"'),
    ("foo", None, 'foo: null'),
])
def test_encypher(key, value, expected):
    neo4j_property =  Neo4jProperty(key, value)
    assert neo4j_property.encypher() == expected
    
###################################################
# Public Use
###################################################
# parametized fixture
@pytest.mark.parametrize(( "key, value"), [
    ('int_key', 1),
    ('float_key', 1.8),
    ('str_key', 'str'),
    ('bool_true_key', True),
    ('bool_false_key', False),
    ('date_key', '2018-03-21'),
    ('datetime_key', '2018-03-21T01:01:01+0900'),
    ('none_key', None),
])
def test_init(key, value):
    neo4j_property = Neo4jProperty(key, value)
    assert neo4j_property.key == key
    assert neo4j_property.value == value

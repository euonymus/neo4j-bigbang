# pytest読み込み
import pytest

from entities.neo4j_property_int import Neo4jPropertyInt

###################################################
# Converter
###################################################
# parametized fixture
@pytest.mark.parametrize(( "value, expected"), [
    (1.8, None),
    ('str', None),
    (None, None),
    (True, None),
    (False, None),
    ('0', None),
    (0, 0),
    (1.0, 1),
    (-1, -1),
])
def test_generalization_by_type(value, expected):
    assert Neo4jPropertyInt.generalization_by_type(value) == expected

###################################################
# Run Time Converter
###################################################
# parametized fixture
@pytest.mark.parametrize(( "value, expected"), [
    ('str', 'None'),
    (1, '1'),
])
def test_enstring_by_type(value, expected):
    neo4j_property =  Neo4jPropertyInt('foo', value)
    assert neo4j_property.enstring_by_type() == expected

# parametized fixture
@pytest.mark.parametrize(( "value, expected"), [
    ('str', 'foo: null'),
    (None, 'foo: null'),
    (1, 'foo: 1'),
    (-1, 'foo: -1'),
])
def test_encypher(value, expected):
    neo4j_property =  Neo4jPropertyInt('foo', value)
    assert neo4j_property.encypher() == expected

    
###################################################
# Type Checker
###################################################
# parametized fixture
@pytest.mark.parametrize(( "property, expected"), [
    ('str', False),
    (None, False),
    (True, False),
    (False, False),
    ('1', False),
    (1, True),
    (1.0, True),
])
def test_is_int(property, expected):
    assert Neo4jPropertyInt.is_int(property) == expected


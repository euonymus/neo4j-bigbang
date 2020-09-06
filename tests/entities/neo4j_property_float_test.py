# pytest読み込み
import pytest

from entities.neo4j_property_float import Neo4jPropertyFloat

###################################################
# Converter
###################################################
# parametized fixture
@pytest.mark.parametrize(( "value, expected"), [
    ('str', None),
    (None, None),
    (True, None),
    (False, None),
    ('0', None),
    (0, None),
    (1.0, None),
    (0.1, 0.1),
    (1.1, 1.1),
    (-1.1, -1.1),
])
def test_generalization_by_type(value, expected):
    assert Neo4jPropertyFloat.generalization_by_type(value) == expected

###################################################
# Run Time Converter
###################################################
# parametized fixture
@pytest.mark.parametrize(( "value, expected"), [
    ('str', 'None'),
    (1, 'None'),
    (1.1, '1.1'),
    (-1.1, '-1.1'),
])
def test_enstring_by_type(value, expected):
    neo4j_property =  Neo4jPropertyFloat('foo', value)
    assert neo4j_property.enstring_by_type() == expected

# parametized fixture
@pytest.mark.parametrize(( "value, expected"), [
    ('str', 'foo: null'),
    (None, 'foo: null'),
    (1, 'foo: null'),
    (1.1, 'foo: 1.1'),
    (-1.1, 'foo: -1.1'),
])
def test_encypher(value, expected):
    neo4j_property =  Neo4jPropertyFloat('foo', value)
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
    ('1.1', False),
    (1, False),
    (1.0, False),
    (1.1, True),
])
def test_is_float(property, expected):
    assert Neo4jPropertyFloat.is_float(property) == expected


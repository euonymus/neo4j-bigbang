# pytest読み込み
import pytest

from entities.neo4j_property_bool import Neo4jPropertyBool

###################################################
# Converter
###################################################
# parametized fixture
@pytest.mark.parametrize(( "property, expected"), [
    (1.8, None),
    ('str', None),
    (None, None),
    (True, True),
    (False, False),
    ('1', True),
    ('true', True),
    ('TRUE', True),
    ('True', True),
    ('0', False),
    ('false', False),
    ('FALSE', False),
    ('False', False),
    (1, True),
    (0, False),
 ])
def test_enbool(property, expected):
    assert Neo4jPropertyBool.enbool(property) == expected

# parametized fixture
@pytest.mark.parametrize(( "value, expected"), [
    (None, None),
    (0, None),
    ('0', None),
    ('True', True),
    (True, True),
    (False, False),
])
def test_generalization_by_type(value, expected):
    assert Neo4jPropertyBool.generalization_by_type(value) == expected

###################################################
# Run Time Converter
###################################################
# parametized fixture
@pytest.mark.parametrize(( "value, expected"), [
    ('str', 'None'),
    (1, 'None'),
    (True, 'True'),
])
def test_enstring_by_type(value, expected):
    neo4j_property =  Neo4jPropertyBool('foo', value)
    assert neo4j_property.enstring_by_type() == expected

# parametized fixture
@pytest.mark.parametrize(( "value, expected"), [
    ('str', 'foo: null'),
    (None, 'foo: null'),
    (1, 'foo: null'),
    ('TRUE', 'foo: True'),
    (False, 'foo: False'),
])
def test_encypher(value, expected):
    neo4j_property =  Neo4jPropertyBool('foo', value)
    assert neo4j_property.encypher() == expected

    
###################################################
# Type Checker
###################################################
# parametized fixture
@pytest.mark.parametrize(( "property, expected"), [
    (1, False),
    ('str', False),
    (None, False),
    (True, True),
    (False, True),
    ('true', True),
    ('false', True),
    ('True', True),
    ('False', True),
    ('TRUE', True),
    ('FALSE', True),
])
def test_is_bool(property, expected):
    assert Neo4jPropertyBool.is_bool(property) == expected


# pytest読み込み
import pytest

from entities.neo4j_property_str import Neo4jPropertyStr

###################################################
# Converter
###################################################
# parametized fixture
@pytest.mark.parametrize(( "value, expected"), [
    (1, None),
    (None, None),
    (True, None),
    (False, None),
    ('str', 'str'),
])
def test_generalization_by_type(value, expected):
    assert Neo4jPropertyStr.generalization_by_type(value) == expected

###################################################
# Run Time Converter
###################################################
# parametized fixture
@pytest.mark.parametrize(( "value, expected"), [
    ('str', '"str"'),
])
def test_enstring_by_type(value, expected):
    neo4j_property =  Neo4jPropertyStr('foo', value)
    assert neo4j_property.enstring_by_type() == expected

# parametized fixture
@pytest.mark.parametrize(( "value, expected"), [
    (1, 'foo: null'),
    (None, 'foo: null'),
    ('str', 'foo: "str"'),
])
def test_encypher(value, expected):
    neo4j_property =  Neo4jPropertyStr('foo', value)
    assert neo4j_property.encypher() == expected

    
###################################################
# Type Checker
###################################################
# parametized fixture
@pytest.mark.parametrize(( "property, expected"), [
    (None, False),
    (True, False),
    (False, False),
    (1, False),
    ('2020-02-20 01:01:01+0900', False),
    ('2020-02-20', False),
    ('1', True),
    ('str', True),
])
def test_is_str(property, expected):
    assert Neo4jPropertyStr.is_str(property) == expected


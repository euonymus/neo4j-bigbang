# pytest読み込み
import pytest
import datetime

from entities.neo4j_property_date import Neo4jPropertyDate

###################################################
# Converter
###################################################
# parametized fixture
@pytest.mark.parametrize(( "value, expected"), [
    ('str', None),
    (None, None),
    ('2020-02-20', datetime.datetime.strptime('2020-02-20', '%Y-%m-%d').date()),
])
def test_generalization_by_type(value, expected):
    assert Neo4jPropertyDate.generalization_by_type(value) == expected

###################################################
# Run Time Converter
###################################################
# parametized fixture
@pytest.mark.parametrize(( "property, expected"), [
    (1, None),
    (1.8, None),
    ('str', None),
    (True, None),
    (False, None),
    (None, None),
    ('2020-02-20', '2020-02-20'),
 ])
def test_print_date(property, expected):
    neo4j_property =  Neo4jPropertyDate('foo', property)
    result = neo4j_property.print_date()
    assert result == expected

# parametized fixture
@pytest.mark.parametrize(( "value, expected"), [
    ('2020-02-20', 'date("2020-02-20")'),
])
def test_enstring_by_type(value, expected):
    neo4j_property =  Neo4jPropertyDate('foo', value)
    assert neo4j_property.enstring_by_type() == expected

# parametized fixture
@pytest.mark.parametrize(( "value, expected"), [
    ('str', 'foo: null'),
    (None, 'foo: null'),
    ('2020-02-20', 'foo: date("2020-02-20")'),
])
def test_encypher(value, expected):
    neo4j_property =  Neo4jPropertyDate('foo', value)
    assert neo4j_property.encypher() == expected
    
###################################################
# Parser
###################################################
# parametized fixture
@pytest.mark.parametrize(( "property"), [
    (1),
    (1.8),
    (True),
    (False),
    (None),
])
def test_try_parsing_date_type_error(property):
    with pytest.raises(TypeError):
        result = Neo4jPropertyDate.try_parsing_date(property)

# parametized fixture
@pytest.mark.parametrize(( "property"), [
    ('str'),
    ('2020-13-20'),
    ('2020-02-20T00:01:01+0900'),
])
def test_try_parsing_date_value_error(property):
    with pytest.raises(ValueError):
        result = Neo4jPropertyDate.try_parsing_date(property)

# parametized fixture
@pytest.mark.parametrize(( "property"), [
    ('2020-02-20'),
    ('2020/02/20'),
    ('2020.02.20'),
    ('2020年02月20日'),
])
def test_try_parsing_date_success(property):
    result = Neo4jPropertyDate.try_parsing_date(property)
    assert isinstance(result, datetime.datetime)

# parametized fixture
@pytest.mark.parametrize(( "property"), [
    ('2020-02-20'),
])
def test_try_parsing_date_as_date(property):
    result = Neo4jPropertyDate.try_parsing_date_as_date(property)
    assert isinstance(result, datetime.date)

###################################################
# Type Checker
###################################################
# parametized fixture
@pytest.mark.parametrize(( "property, expected"), [
    (1, False),
    (1.8, False),
    ('str', False),
    (True, False),
    (False, False),
    (None, False),
    ('2020-02-20T01:01:01+0900', False),
    ('2020-13-20', False),
    ('2020-02-20', True),
    ('2020/02/20', True),
    ('2020.02.20', True),
    ('2020年02月20日', True),
])
def test_is_date(property, expected):
    assert Neo4jPropertyDate.is_date(property) == expected

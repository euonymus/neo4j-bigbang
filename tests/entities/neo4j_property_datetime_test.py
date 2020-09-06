# pytest読み込み
import pytest
import datetime

from entities.neo4j_property_datetime import Neo4jPropertyDatetime

###################################################
# Converter
###################################################
# parametized fixture
@pytest.mark.parametrize(( "value, expected"), [
    ('str', None),
    (None, None),
    ('2020-02-20 01:01:01+0900', datetime.datetime.strptime('2020-02-20 01:01:01+0900', '%Y-%m-%d %H:%M:%S+0900')),
])
def test_generalization_by_type(value, expected):
    assert Neo4jPropertyDatetime.generalization_by_type(value) == expected

# parametized fixture
@pytest.mark.parametrize(( "property, expected"), [
    (1, False),
    (None, False),
    (True, False),
    (False, False),
    ([1,2], False),
    ({'hoge':1, 'hage':2}, False),
    ('str', 'yey'),
 ])
def test_str_2_certain_type(property, expected):
    my_lambda = lambda property : 'yey' if isinstance(property, str) else False
    assert Neo4jPropertyDatetime.str_2_certain_type(property, my_lambda) == expected

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
    ('2020-02-20 01:01:01+0900', '2020-02-20T01:01:01+0900'),
 ])
def test_print_datetime(property, expected):
    neo4j_property =  Neo4jPropertyDatetime('foo', property)
    result = neo4j_property.print_datetime()
    assert result == expected

# parametized fixture
@pytest.mark.parametrize(( "value, expected"), [
    ('2020-02-20 01:01:01+0900', 'datetime("2020-02-20T01:01:01+0900")'),
])
def test_enstring_by_type(value, expected):
    neo4j_property =  Neo4jPropertyDatetime('foo', value)
    assert neo4j_property.enstring_by_type() == expected

# parametized fixture
@pytest.mark.parametrize(( "value, expected"), [
    ('str', 'foo: null'),
    (None, 'foo: null'),
    ('2020-02-20 01:01:01+0900', 'foo: datetime("2020-02-20T01:01:01+0900")'),
])
def test_encypher(value, expected):
    neo4j_property =  Neo4jPropertyDatetime('foo', value)
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
def test_try_parsing_datetime_type_error(property):
    with pytest.raises(TypeError):
        result = Neo4jPropertyDatetime.try_parsing_datetime(property)

# parametized fixture
@pytest.mark.parametrize(( "property"), [
    ('str'),
    ('2020-02-20'),
    ('2020-13-20'),
    ('2020-02-20T24:01:01+0900'),
])
def test_try_parsing_datetime_value_error(property):
    with pytest.raises(ValueError):
        result = Neo4jPropertyDatetime.try_parsing_datetime(property)

# parametized fixture
@pytest.mark.parametrize(( "property"), [
    ('2020-02-20T01:01:01+0900'),
    ('2020-02-20 01:01:01+0900'),
    ('2020-02-20T01:01:01'),
    ('2020-02-20 01:01:01'),
    ('2020年02月20日01時01分01秒'),
])
def test_try_parsing_datetime_success(property):
    result = Neo4jPropertyDatetime.try_parsing_datetime(property)
    assert isinstance(result, datetime.datetime)

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
    ('2020-02-20', False),
    ('2020-13-20', False),
    ('2020-02-20T24:01:01+0900', False),
    ('2020-02-20T01:01:01+0900', True),
    ('2020-02-20 01:01:01+0900', True),
    ('2020-02-20T01:01:01', True),
    ('2020-02-20 01:01:01', True),
    ('2020年02月20日01時01分01秒', True),
])
def test_is_datetime(property, expected):
    assert Neo4jPropertyDatetime.is_datetime(property) == expected

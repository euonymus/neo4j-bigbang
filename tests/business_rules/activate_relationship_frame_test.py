# pytest読み込み
import pytest
from business_rules import activate_relationship_frame
from business_rules.activate_relationship_frame import ActivateRelationship
from entities.relationship import Relationship

# @pytest.fixture
# def test_data():
#     return {
#         'int_key': 1,
#         'float_key': 1.8,
#         'str_key': 'str',
#         'bool_true_key': True,
#         'bool_false_key': False,
#         'date_key': '2018-03-21',
#         'datetime_key': '2018-03-21T01:01:01+0900',
#         'none_key': None,
#     }

###################################################
# Public Use
###################################################
# parametized fixture
@pytest.mark.parametrize(( "target_fields, target_values, expected"), [
    ('foo', 'hoge|hage', False),
    ('foo|bar', 'hoge', False),
    ('foo', 'hoge', {'foo':'hoge'}),
    ('foo|bar', 'hoge|hage', {'foo':'hoge','bar':'hage'}),
])
def test_convert_target_into_condition(target_fields, target_values, expected):
    result = ActivateRelationship.convert_target_into_condition(target_fields, target_values)
    assert result == expected


# parametized fixture
@pytest.mark.parametrize(( "target_fields, target_values, expected"), [
    ('foo', 'hoge|hage', False),
    ('foo|bar', 'hoge', False),
    ('foo', 'hoge', True),
    ('foo|bar', 'hoge|hage', True),
])
def test_search_and_convert_target_into_node(mocker, target_fields, target_values, expected):
    # Mock NodeRepository
    insmock = mocker.Mock()
    insmock.find_by.return_value = [True]
    mocker.patch.object(activate_relationship_frame, 'NodeRepository', mocker.Mock(return_value=insmock))
    # Run
    relationship_frame = 'dummy'
    activation = ActivateRelationship(relationship_frame)
    result = activation.search_and_convert_target_into_node(target_fields, target_values)
    assert result == expected


class RelationshipFrame:
    target_fields_in = 'foo|bar'
    target_values_in = 'hoge|hage'
    target_fields_out = 'foo|bar'
    target_values_out = 'hoge|hage'
    type = 'MY_REL_TYPE'
    properties = {}
    directed = True
         
def test_invoke(mocker):
    # Mock NodeRepository
    insmock = mocker.Mock()
    insmock.find_by.return_value = [True]
    mocker.patch.object(activate_relationship_frame, 'NodeRepository', mocker.Mock(return_value=insmock))

    relationship_frame = RelationshipFrame()
    activation = ActivateRelationship(relationship_frame, create_node = True)
    result = activation.invoke()
    assert isinstance(result, Relationship)

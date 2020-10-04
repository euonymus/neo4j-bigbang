# pytest読み込み
import pytest
import pandas as pd

from repositories.csv_2_relationship_frame import Csv2RelationshipFrame
import entities

SAMPLE_CSV_DATA_PATH_FILENAME = 'tests/data/MY_REL_TYPE.csv'
SAMPLE_CSV_DATA_PATH_IN_ROW = 'tests/data/relationship_type_in_row.csv'

# parametized fixture
@pytest.mark.parametrize(( "target_fields, target_values, expected"), [
    ('foo', 'hoge|hage', False),
    ('foo|bar', 'hoge', False),
    ('foo', 'hoge', {'foo':'hoge'}),
    ('foo|bar', 'hoge|hage', {'foo':'hoge','bar':'hage'}),
])
def test_convert_target_into_condition(target_fields, target_values, expected):
    result = Csv2RelationshipFrame.convert_target_into_condition(target_fields, target_values)
    assert result == expected

# parametized fixture
@pytest.mark.parametrize(( "rel_type, properties, expected"), [
    ('HOGE', [['name', 'taro', 'name', 'jiro', True, 1, 'a', None], ['name', 'taro', 'name', 'jiro', False, 2, 'b', 'hoge']], None),
])
def test_to_entity(rel_type, properties, expected):
    df = pd.DataFrame(properties, columns=['target_fields_in', 'target_values_in', 'target_fields_out', 'target_values_out', 'directed', 'col1', 'col2', 'col3'])

    row = df.iloc[0].copy()
    # You need to cast integer, because it's originally numpy.int64
    row['col1'] = int(row['col1'])
    result = Csv2RelationshipFrame.to_entity(row, rel_type)
    assert result.type == rel_type
    assert isinstance(result.properties['col1'], entities.neo4j_property_int.Neo4jPropertyInt)
    assert isinstance(result.properties['col2'], entities.neo4j_property_str.Neo4jPropertyStr)
    assert 'col3' not in result.properties
    
def test_relationships():
    # Case 1: from File Name
    csv_2_relationship_frames = Csv2RelationshipFrame(file_path = SAMPLE_CSV_DATA_PATH_FILENAME, type_in_row = False)
    relationships = csv_2_relationship_frames.relationships()
    for relationship in relationships:
        assert isinstance(relationship, entities.relationship.Relationship)
        assert relationship.type == 'MY_REL_TYPE'

    # Case 2: from Row
    csv_2_relationship_frames = Csv2RelationshipFrame(file_path = SAMPLE_CSV_DATA_PATH_IN_ROW, type_in_row = True)
    relationships = csv_2_relationship_frames.relationships()
    for relationship in relationships:
        assert isinstance(relationship, entities.relationship.Relationship)
        assert relationship.type == 'IN_ROW_TYPE'

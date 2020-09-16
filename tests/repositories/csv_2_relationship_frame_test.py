# pytest読み込み
import pytest
import pandas as pd

from repositories.csv_2_relationship_frame import Csv2RelationshipFrame
import entities

SAMPLE_CSV_DATA_PATH_FILENAME = 'tests/data/MY_REL_TYPE.csv'
SAMPLE_CSV_DATA_PATH_IN_ROW = 'tests/data/relationship_type_in_row.csv'

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
    
def test_relationship_frames():
    # Case 1: from File Name
    csv_2_relationship_frames = Csv2RelationshipFrame(file_path = SAMPLE_CSV_DATA_PATH_FILENAME, type_in_row = False)
    relationship_frames = csv_2_relationship_frames.relationship_frames()
    for relationship_frame in relationship_frames:
        assert isinstance(relationship_frame, entities.relationship_frame.RelationshipFrame)
        assert relationship_frame.type == 'MY_REL_TYPE'

    # Case 2: from Row
    csv_2_relationship_frames = Csv2RelationshipFrame(file_path = SAMPLE_CSV_DATA_PATH_IN_ROW, type_in_row = True)
    relationship_frames = csv_2_relationship_frames.relationship_frames()
    for relationship_frame in relationship_frames:
        assert isinstance(relationship_frame, entities.relationship_frame.RelationshipFrame)
        assert relationship_frame.type == 'IN_ROW_TYPE'

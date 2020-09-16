# pytest読み込み
import pytest
import pandas as pd

from repositories.csv_2_node import Csv2Node
import entities

SAMPLE_CSV_DATA_PATH_FILENAME = 'tests/data/Foo|Bar.csv'
SAMPLE_CSV_DATA_PATH_IN_ROW = 'tests/data/in_row.csv'

# parametized fixture
@pytest.mark.parametrize(( "labels, properties, expected"), [
    (['Foo', 'Bar'], [[1, 'a', None], [2, 'b', 'hoge']], None),
])
def test_to_entity(labels, properties, expected):
    df = pd.DataFrame(properties, columns=['col1', 'col2', 'col3'])

    row = df.iloc[0].copy()
    # You need to cast integer, because it's originally numpy.int64
    row['col1'] = int(row['col1'])
    result = Csv2Node.to_entity(row, labels)
    assert result.labels == labels
    assert isinstance(result.properties['col1'], entities.neo4j_property_int.Neo4jPropertyInt)
    assert isinstance(result.properties['col2'], entities.neo4j_property_str.Neo4jPropertyStr)
    assert 'col3' not in result.properties
    
def test_nodes():
    # Case 1: from File Name
    csv_2_node = Csv2Node(file_path = SAMPLE_CSV_DATA_PATH_FILENAME, labels_in_row = False)
    nodes = csv_2_node.nodes()
    for node in nodes:
        assert isinstance(node, entities.node.Node)
        assert node.labels == ['Foo', 'Bar']

    # Case 2: from Row
    csv_2_node = Csv2Node(file_path = SAMPLE_CSV_DATA_PATH_IN_ROW, labels_in_row = True)
    nodes = csv_2_node.nodes()
    for node in nodes:
        assert isinstance(node, entities.node.Node)
        assert node.labels == ['Hoge', 'Hage']


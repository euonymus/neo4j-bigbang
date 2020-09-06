# pytest読み込み
import pytest
from business_rules.activate_relationship_frames import ActivateRelationships
import tests.init_neo4j

SAMPLE_CSV_DATA_PATH_FILENAME = 'tests/data/MY_REL_TYPE.csv'


###################################################
# Public Use
###################################################
# def test_invoke():
#     file_path = SAMPLE_CSV_DATA_PATH_FILENAME
#     type_in_row = False
#     # create_node = True のテストはちゃんとMockしないとNode作っちゃうのでそれまで無視
#     create_node = False
#     activate_relationships = ActivateRelationships(file_path, type_in_row, create_node)
#     result = activate_relationships.invoke()

#     for re in result:
#         print(re)
#         print(re.type)
#         print(re.node1.properties)
#         print(re.node2.properties)
#         print(re.directed)
#         print(re.properties) # TODO: properties がうまくセットされない！！！　なんでや。

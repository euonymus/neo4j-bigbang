# pytest読み込み
import pytest

from repositories.node import NodeRepository
from entities.node import Node
from entities.neo4j_properties import neo4j_properties
import tests.init_neo4j




# parametized fixture
@pytest.mark.parametrize(( "labels, pure_properties, expected"), [
    (['Hoge'], {'foo': 1, 'bar': 2}, None),
])
def test_build_match_clause(labels, pure_properties, expected):
    properties = neo4j_properties(pure_properties)
    result = NodeRepository.build_match_clause(labels, properties)
    print(result)


# TODO: Mockつくる必要あり。

# def test_find_by():
#     node_repository = NodeRepository()
#     properties = neo4j_properties({'quark_type_id': 2})
#     result = node_repository.find_by(labels = ['Quark'], properties = properties)
#     assert len(result) == 100

#     for record in result:
#         assert isinstance(record, Node)

# def test_find_one_by():
#     node_repository = NodeRepository()
#     properties = neo4j_properties({'quark_type_id': 2})
#     result = node_repository.find_one_by(labels = ['Quark'], properties = properties)
#     assert isinstance(result, Node)

# # 実際に Neo4jにデータが書き込まれる事を確認できる。 assertの仕方がわからないのでコメントアウトする
# def test_create():
#     labels = ['Test', 'Foo', 'Bar']
#     properties = {'test': 1, 'sample': 'a'}
#     node = Node(labels, properties)

#     node_repository = NodeRepository()
#     result = node_repository.create(node)

# 実際に Neo4jにデータが更新される事を確認できる。 assertの仕方がわからないのでコメントアウトする
# def test_update():
#     target_properties = neo4j_properties({'test': 1, 'sample': 'a'})
#     target_labels = ['Test', 'Foo', 'Bar']

#     properties = {'test': 5, 'sample': 'c'}
#     labels = ['Test', 'Green', 'Red']
#     node = Node(labels, properties)

#     node_repository = NodeRepository()
#     result = node_repository.update(target_labels, target_properties, node)

# # 実際に Neo4jからデータが削除される事を確認できる。 assertの仕方がわからないのでコメントアウトする
# def test_update():
#     target_labels = ['Test', 'Green', 'Red']
#     target_properties = neo4j_properties({'test': 5, 'sample': 'c'})

#     node_repository = NodeRepository()
#     result = node_repository.delete(target_labels, target_properties)

# pytest読み込み
import pytest

from repositories.relationship import RelationshipRepository
from repositories.node import NodeRepository
from entities.node import Node
from entities.relationship import Relationship
import tests.init_neo4j

# 実際に Neo4jにデータが書き込まれる事を確認できる。 Mockしてないのでコメントアウト

# def test_create():
#     # Case1: Try creating existing relationship and should be failed
#     # I need to mock RelationshipRepository.find_one() to achieve this.

#     # Case2: Try creating relationship between not existing nodes and should be failed
#     labels1 = ['Person']
#     properties1 = {'name_ja': 'not existing node one'}
#     node1 = Node(labels1, properties1)

#     labels2 = ['SoftwareApplication']
#     properties2 = {'name_ja': 'not existing node two'}
#     node2 = Node(labels2, properties2)

#     rel_type = 'FOUNDER_OF'
#     properties3 = {'relation_ja': 'の設計者、開発総責任者'}
#     relationship = Relationship(rel_type, node1, node2, properties3)

#     relationship_repository = RelationshipRepository()
#     result = relationship_repository.create(relationship)
#     assert result == False

#     # Case3: Try creating relationship and node at the same time.
#     import random
#     labels1 = ['Seed']
#     properties1 = {'random_seed': random.random()}
#     node1 = Node(labels1, properties1)

#     labels2 = ['Seed']
#     properties2 = {'random_seed': random.random()}
#     node2 = Node(labels2, properties2)

#     rel_type = 'FOUNDER_OF'
#     properties3 = {'relation_ja': 'の設計者、開発総責任者'}
#     relationship = Relationship(rel_type, node1, node2, properties3)

#     create_node = True
#     relationship_repository = RelationshipRepository(create_node)
#     result = relationship_repository.create(relationship)
#     # MEMO: うまく result のrelationshipを取得できないので雑な assert
#     assert result

#     # Case4: Normal creation between existing nodes
#     # use nodes created above

#     # generate random string
#     import string
#     randlst = [random.choice(string.ascii_letters + string.digits) for i in range(10)]
#     rel_type = 'pre' + ''.join(randlst)
#     properties3 = {'random_relation': random.random()}
#     relationship = Relationship(rel_type, node1, node2, properties3)

#     create_node = True
#     relationship_repository = RelationshipRepository(create_node)
#     result = relationship_repository.create(relationship)
#     # MEMO: うまく result のrelationshipを取得できないので雑な assert
#     assert result

    # Case5: Simple test case by creating nodes among testing.
    # labels1 = ['Person']
    # properties1 = {'name_ja': 'hogehoge55'}
    # node1 = Node(labels1, properties1)

    # node_repository1 = NodeRepository(unique_labels = ['Person'], unique_property_keys = ['name_ja'])
    # node_repository1.save(node1)

    # labels2 = ['SoftwareApplication']
    # properties2 = {'name_ja': 'foofoo55'}
    # node2 = Node(labels2, properties2)

    # node_repository2 = NodeRepository(unique_labels = ['SoftwareApplication'], unique_property_keys = ['name_ja'])
    # node_repository2.save(node2)

    # rel_type = 'FOUNDER_OF'
    # properties3 = {'relation_ja': 'の設計者、開発総責任者'}
    # relationship = Relationship(rel_type, node1, node2, properties3)

    # relationship_repository = RelationshipRepository()
    # result = relationship_repository.create(relationship)
    # print(111)
    # print(result)
    # print(222)


# def test_update():
#     # Create relation first
#     import random
#     labels1 = ['Seed']
#     properties1 = {'random_seed': random.random()}
#     node1 = Node(labels1, properties1)

#     labels2 = ['Seed']
#     properties2 = {'random_seed': random.random()}
#     node2 = Node(labels2, properties2)

#     rel_type = 'FOUNDER_OF'
#     properties3 = {'relation_ja': 'の設計者、開発総責任者'}
#     relationship = Relationship(rel_type, node1, node2, properties3)

#     create_node = True
#     relationship_repository = RelationshipRepository(create_node)
#     relationship_repository.create(relationship)

#     # New realtionship properties
#     # generate random string
#     properties3 = {'random_relation': random.random()}
#     relationship = Relationship(rel_type, node1, node2, properties3)

#     result = relationship_repository.update(relationship, False)

#     # MEMO: うまく result のrelationshipを取得できないので雑な assert
#     assert result


# def test_delete():
#     # Create relation first
#     labels1 = ['DeleteTest']
#     properties1 = {'delete_name': 'delete_test1'}
#     node1 = Node(labels1, properties1)

#     labels2 = ['DeleteTest']
#     properties2 = {'delete_name': 'delete_test2'}
#     node2 = Node(labels2, properties2)
    
#     rel_type = 'DELETING_CONNECTION'
#     properties3 = {'delete_relation': 'ddddddd'}
#     relationship = Relationship(rel_type, node1, node2, properties3)

#     create_node = True
#     relationship_repository = RelationshipRepository(create_node)
#     relationship_repository.create(relationship)

#     result = relationship_repository.delete(relationship)

#     # MEMO: うまく result のrelationshipを取得できないので雑な assert
#     assert result

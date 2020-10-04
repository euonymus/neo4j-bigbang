import os
from repositories.neo4j_driver import Neo4jDriver
from repositories.node import NodeRepository
from entities.node import Node
from entities.relationship import Relationship

NODE1_INDICATOR = 'n1'
NODE2_INDICATOR = 'n2'
RELATIONSHIP_INDICATOR = 'r'
AVOID_TO_SEARCH_KEY = ['created', 'modified']
class RelationshipRepository():
    """
    Private Properties and Getters
    """
    @property
    def neo4j(self):
        pass

    @neo4j.getter
    def neo4j(self):
        return self.__neo4j

    @property
    def create_node(self):
        pass

    @create_node.getter
    def create_node(self):
        return self.__create_node

    def __init__(self, create_node = False):
        neo4j_uri   = os.environ.get("NEO4J_URI")
        neo4j_user   = os.environ.get("NEO4J_USER")
        neo4j_password   = os.environ.get("NEO4J_PASSWORD")
        self.__neo4j = Neo4jDriver(neo4j_uri, neo4j_user, neo4j_password)
        self.__create_node = create_node

    def find(self, relationship):
        rel_type = relationship.type

        node1 = relationship.node1
        tmp_properties = self.remove_avoid_keys_from_dictionary(node1.properties, AVOID_TO_SEARCH_KEY)
        match_clause_node1 = self.build_match_clause(node1.labels, tmp_properties, NODE1_INDICATOR)

        node2 = relationship.node2
        tmp_properties = self.remove_avoid_keys_from_dictionary(node2.properties, AVOID_TO_SEARCH_KEY)
        match_clause_node2 = self.build_match_clause(node2.labels, tmp_properties, NODE2_INDICATOR)

        cypher = 'MATCH %s-[%s:%s]->%s RETURN %s, %s, %s' % (match_clause_node1, RELATIONSHIP_INDICATOR, rel_type, match_clause_node2, NODE1_INDICATOR, RELATIONSHIP_INDICATOR, NODE2_INDICATOR)
        result = self.neo4j.exec_read_cypher(cypher)

        ret = []
        for record in result:
            ret.append(self.to_entity(record))

        return ret


    def find_one(self, relationship):
        result_list = self.find(relationship)
        if len(result_list) == 0:
            return None
        return result_list[0]


    def create(self, relationship):
        existing = self.find_one(relationship)
        if existing:
            print('[SKIP]: There is already a same relationship between attempting nodes.')
            return

        # Prepare node1
        node1 = relationship.node1
        labels1 = node1.labels
        tmp_properties1 = self.remove_avoid_keys_from_dictionary(node1.properties, AVOID_TO_SEARCH_KEY)
        node_repository = NodeRepository()
        node_result = node_repository.find_by(labels1, tmp_properties1)
        if len(node_result) == 0:
            if not self.create_node:
                print('[Skip the Row] Target Node is not found ')
                return False

            node_repository = NodeRepository()
            node_repository.create(node1)
        elif len(node_result) != 1:
            print('[SKIP]: It can not create relationships among multiple nodes.')
            return False
                    
        # Prepare node2
        node2 = relationship.node2
        labels2 = node2.labels
        tmp_properties2 = self.remove_avoid_keys_from_dictionary(node2.properties, AVOID_TO_SEARCH_KEY)
        node_repository = NodeRepository()
        node_result = node_repository.find_by(labels2, tmp_properties2)
        if len(node_result) == 0:
            if not self.create_node:
                print('[SKIP]: No node was found attempting to create relationship.')
                return False

            node_repository = NodeRepository()
            node_repository.create(node2)
        elif len(node_result) != 1:
            print('[SKIP]: It can not create relationships among multiple nodes.')
            return False

        match_clause_node1 = self.build_match_clause(labels1, tmp_properties1, NODE1_INDICATOR)
        match_clause_node2 = self.build_match_clause(labels2, tmp_properties2, NODE2_INDICATOR)

        type_str = "" if not relationship.type else ':%s' % relationship.type
        relation_props = relationship.encypher(True)
        # MEMO: Creation of undirected relationship is not supported by Neo4j
        # directed_str = ">" if relationship.directed else ""
        directed_str = ">"

        cypher = "MATCH %s, %s CREATE (%s)-[r%s %s]-%s(%s) RETURN r" % (match_clause_node1, match_clause_node2, NODE1_INDICATOR, type_str, relation_props, directed_str, NODE2_INDICATOR)

        result = self.neo4j.exec_write_cypher(cypher)
        return result


    # MEMO: This updates same type of relationship only. Different type is considered to be the different meaning.
    #       You cannot change relationship type.
    def update(self, relationship, nicely = True):
        existing = self.find_one(relationship)
        if not existing:
            return None

        rel_type = relationship.type

        node1 = relationship.node1
        tmp_properties = self.remove_avoid_keys_from_dictionary(node1.properties, AVOID_TO_SEARCH_KEY)
        match_clause_node1 = self.build_match_clause(node1.labels, tmp_properties, NODE1_INDICATOR)

        node2 = relationship.node2
        tmp_properties = self.remove_avoid_keys_from_dictionary(node2.properties, AVOID_TO_SEARCH_KEY)
        match_clause_node2 = self.build_match_clause(node2.labels, tmp_properties, NODE2_INDICATOR)


        # TODO setting properties
        # name: 'Peter Smith', position: 'Entrepreneur' 
        setting_properties = relationship.encypher(True)

        update_prefix = '+' if nicely else ''
        cypher = 'MATCH %s-[%s:%s]->%s SET %s %s= %s RETURN %s' % (match_clause_node1, RELATIONSHIP_INDICATOR, rel_type, match_clause_node2, RELATIONSHIP_INDICATOR, update_prefix, setting_properties, RELATIONSHIP_INDICATOR)
        result = self.neo4j.exec_write_cypher(cypher)
        return result


    def save(self, relationship, nicely = True):
        existing = self.find_one(relationship)
        if existing:
            self.update(relationship, nicely)
        else:
            self.create(relationship)

        return True


    def delete(self, relationship):
        """
        You can delete only one node at once for security
        """
        existing = self.find(relationship)
        if len(existing) == 0:
            return None
        if len(existing) >= 2:
            raise RuntimeError('You can delete only one node at once')

        rel_type = relationship.type

        node1 = relationship.node1
        tmp_properties = self.remove_avoid_keys_from_dictionary(node1.properties, AVOID_TO_SEARCH_KEY)
        match_clause_node1 = self.build_match_clause(node1.labels, tmp_properties, NODE1_INDICATOR)

        node2 = relationship.node2
        tmp_properties = self.remove_avoid_keys_from_dictionary(node2.properties, AVOID_TO_SEARCH_KEY)
        match_clause_node2 = self.build_match_clause(node2.labels, tmp_properties, NODE2_INDICATOR)

        cypher = 'MATCH %s-[%s:%s]->%s DELETE %s' % (match_clause_node1, RELATIONSHIP_INDICATOR, rel_type, match_clause_node2, RELATIONSHIP_INDICATOR)
        result = self.neo4j.exec_write_cypher(cypher)
        return result


    @classmethod
    def to_entity(cls, record):
        # Create Node1
        labels1 = list(record.get(NODE1_INDICATOR).labels)
        properties1 = cls.record_properties_2_dict( record.data()[NODE1_INDICATOR] )
        node1 = Node( labels = labels1, properties = properties1 )

        # Create Node2
        labels2 = list(record.get(NODE2_INDICATOR).labels)
        properties2 = cls.record_properties_2_dict( record.data()[NODE2_INDICATOR] )
        node2 = Node( labels = labels2, properties = properties2 )

        # Create Relation Data
        rel_type = record.get(RELATIONSHIP_INDICATOR).type
        properties_r = cls.record_properties_2_dict( record.get(RELATIONSHIP_INDICATOR) )
        return Relationship(rel_type, node1, node2, properties = properties_r)

    @staticmethod
    def build_match_clause(labels, properties, indicator = 'node'):
        filter = ''
        for key, property in properties.items():
            if filter:
                filter += ', '
            filter += property.encypher()

        labels_str = "" if len(labels) == 0 else ':%s' % ":".join(labels)
        return '(%s%s {%s})' % (indicator, labels_str, filter)


    @staticmethod
    def remove_avoid_keys_from_dictionary(dict_object, avoids = []):
        ret = {}
        for key, property in dict_object.items():
            if key not in avoids:
                ret[key] = property

        return ret

    @staticmethod
    def record_properties_2_dict(record_properties):
        import neo4j
        ret = {}
        for key, property in record_properties.items():
            if isinstance(property, neo4j.time.DateTime):
                ret[key] = str(property)
            else:
                ret[key] = property

        return ret


from entities.relationship import Relationship
from repositories.node import NodeRepository
from entities.node import Node
from entities.neo4j_properties import neo4j_properties

class ActivateRelationship():

    """
    Private Properties
    """
    @property
    def relationship_frame(self):
        pass

    @relationship_frame.getter
    def relationship_frame(self):
        return self.__relationship_frame

    @property
    def create_node(self):
        pass

    @create_node.getter
    def create_node(self):
        return self.__create_node

    """
    Constructor
    @relationship_frame: relationship_frame is RelationshipFrame entity object
    @create_node: Create a new node if it doesn't exist and create_node is True
    """
    def __init__(self, relationship_frame, create_node = False):
        self.__relationship_frame = relationship_frame
        self.__create_node = create_node


    def invoke(self):
        labels_in = self.relationship_frame.target_labels_in if hasattr(self.relationship_frame, 'target_labels_in') else []
        labels_out = self.relationship_frame.target_labels_out if hasattr(self.relationship_frame, 'target_labels_out') else []
        

        node1 = self.search_and_convert_target_into_node(self.relationship_frame.target_fields_in, self.relationship_frame.target_values_in, labels_in)
        if not node1:
            return False
        node2 = self.search_and_convert_target_into_node(self.relationship_frame.target_fields_out, self.relationship_frame.target_values_out, labels_out)
        if not node2:
            return False

        rel_type = self.relationship_frame.type

        properties = {}
        for key, property in self.relationship_frame.properties.items():
            properties[key] = property.value

        # directed = self.relationship_frame.directed

        # return self.generate_relationship(rel_type, node1, node2, properties, directed)
        return self.generate_relationship(rel_type, node1, node2, properties)

    # @staticmethod
    # def generate_relationship(rel_type, node1, node2, properties, directed):
    #     return Relationship(rel_type, node1, node2, properties, directed)
    @staticmethod
    def generate_relationship(rel_type, node1, node2, properties):
        return Relationship(rel_type, node1, node2, properties)

    def search_and_convert_target_into_node(self, target_fields, target_values, labels = []):
        tmp_properties = self.convert_target_into_condition(target_fields, target_values)
        if not tmp_properties:
            return False

        properties = neo4j_properties(tmp_properties)
        node_repository = NodeRepository()
        # MEMO: Below line is not tested.
        # nodes = node_repository.find_by([], properties)
        nodes = node_repository.find_by(labels, properties)
        # MEMO: Relationship entity takes exactry one nodes in each sides of in and out.
        if len(nodes) == 1:
            return nodes[0]

        if self.create_node and len(nodes) == 0:
            node = self.convert_target_into_node(target_fields, target_values, labels)
            node_repository.create(node)
            return node

        return False

    @classmethod
    def convert_target_into_node(cls, target_fields, target_values, labels = []):
        properties = cls.convert_target_into_condition(target_fields, target_values)
        if not properties:
            return False

        return  Node(labels, properties)

    @staticmethod
    def convert_target_into_condition(target_fields, target_values):
        property_keys = target_fields.split('|')
        property_values = target_values.split('|')
        if len(property_keys) != len(property_values):
            return False

        target_properties = {}
        for index, property_key in enumerate(property_keys):
            target_properties[property_key] = property_values[index]

        return target_properties


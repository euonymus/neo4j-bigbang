from repositories.csv_2_pandas import Csv2Pandas
# from entities.relationship_frame import RelationshipFrame
from entities.relationship import Relationship
from entities.node import Node

class Csv2Relationship(Csv2Pandas):

    """
    Constructor
    """
    def __init__(self, file_path = None, type_in_row = False):
        self.file_path = file_path
        self.type_in_row = type_in_row

    def relationships(self):
        self.fetch()

        ret = []
        for index, row in self.df.iterrows():
            rel_type = ''
            if not self.type_in_row:
                # TODO: File name should be sanitized
                rel_type = self.file_name
            elif 'type' in row:
                rel_type = str(row.pop('type'))
            else:
                raise RuntimeError('Relationship Type is not specified.')

            entity = self.to_entity(row, rel_type)
            if not entity:
                continue

            ret.append(entity)

        return ret

    @classmethod
    def to_entity(cls, row, rel_type):
        if 'target_fields_in' not in row:
            print('[Skip the Row] target_fields_in is required')
            return False

        if 'target_values_in' not in row:
            print('[Skip the Row] target_values_in is required')
            return False

        if 'target_fields_out' not in row:
            print('[Skip the Row] target_fields_out is required')
            return False

        if 'target_values_out' not in row:
            print('[Skip the Row] target_values_out is required')
            return False

        # if 'directed' not in row:
        #     print('[Skip the Row] directed is required')
        #     return False

        target_fields_in = cls.property(row.pop('target_fields_in'))
        target_values_in = cls.property(row.pop('target_values_in'))
        target_fields_out = cls.property(row.pop('target_fields_out'))
        target_values_out = cls.property(row.pop('target_values_out'))
        # directed = cls.property(row.pop('directed'))

        target_labels_in = []
        if 'target_labels_in' in row:
            tmp = cls.property(row.pop('target_labels_in'))
            if tmp:
                target_labels_in = list(filter(lambda a: a != '', str(tmp).split('|')))
                print(target_labels_in)

        target_labels_out = []
        if 'target_labels_out' in row:
            tmp = cls.property(row.pop('target_labels_out'))
            if tmp:
                target_labels_out = list(filter(lambda a: a != '', str(tmp).split('|')))

        node1 = cls.convert_target_into_node(target_fields_in, target_values_in, target_labels_in)
        node2 = cls.convert_target_into_node(target_fields_out, target_values_out, target_labels_out)

        __properties = {}
        for key, value in row.iteritems():
            __properties[key] = cls.property(value)

        # return RelationshipFrame(rel_type, target_fields_in, target_values_in, target_fields_out, target_values_out, properties = __properties, directed = directed, target_labels_in = target_labels_in, target_labels_out = target_labels_out)
        return Relationship(rel_type, node1, node2, properties = __properties)
        # return RelationshipFrame(rel_type, target_fields_in, target_values_in, target_fields_out, target_values_out, properties = __properties, target_labels_in = target_labels_in, target_labels_out = target_labels_out)

    @classmethod
    def convert_target_into_node(cls, target_fields, target_values, labels = []):
        properties = cls.convert_target_into_condition(target_fields, target_values)
        if not properties:
            return False

        return  Node(labels, properties)

    @classmethod
    def convert_target_into_condition(cls, target_fields, target_values):
        property_keys = list(filter(lambda a: a != '', str(target_fields).split('|')))
        property_values = list(filter(lambda a: a != '', str(target_values).split('|')))
        if len(property_keys) != len(property_values):
            return False

        target_properties = {}
        for index, property_key in enumerate(property_keys):

            target_properties[property_key] = cls.generalization(property_values[index])

        return target_properties

    @classmethod
    def generalization(cls, s):
        if (cls.is_int(s)):
            return int(s)
        elif (cls.is_float(s)):
            return float(s)

        return s

    @staticmethod
    def is_int(s):
        try:
            int(s)
            return True
        except ValueError:
            return False

    @staticmethod
    def is_float(s):
        try:
            float(s)
            return True
        except ValueError:
            return False

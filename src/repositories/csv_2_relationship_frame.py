from repositories.csv_2_pandas import Csv2Pandas
from entities.relationship_frame import RelationshipFrame

class Csv2RelationshipFrame(Csv2Pandas):

    """
    Constructor
    """
    def __init__(self, file_path = None, type_in_row = False):
        self.file_path = file_path
        self.type_in_row = type_in_row

    def relationship_frames(self):
        self.fetch()

        rel_type = ''
        if not self.type_in_row:
            rel_type = self.file_name

        ret = []
        for index, row in self.df.iterrows():
            if self.type_in_row and 'type' in row:
                rel_type = str(row.pop('type'))

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

        if 'directed' not in row:
            print('[Skip the Row] directed is required')
            return False

        target_fields_in = cls.property(row.pop('target_fields_in'))
        target_values_in = cls.property(row.pop('target_values_in'))
        target_fields_out = cls.property(row.pop('target_fields_out'))
        target_values_out = cls.property(row.pop('target_values_out'))
        directed = cls.property(row.pop('directed'))

        target_labels_in = []
        if 'target_labels_in' in row:
            tmp = cls.property(row.pop('target_labels_in'))
            if tmp:
                target_labels_in = str(tmp).split('|')

        target_labels_out = []
        if 'target_labels_out' in row:
            tmp = cls.property(row.pop('target_labels_out'))
            if tmp:
                target_labels_out = str(tmp).split('|')

        __properties = {}
        for key, value in row.iteritems():
            __properties[key] = cls.property(value)

        return RelationshipFrame(rel_type, target_fields_in, target_values_in, target_fields_out, target_values_out, properties = __properties, directed = directed, target_labels_in = target_labels_in, target_labels_out = target_labels_out)

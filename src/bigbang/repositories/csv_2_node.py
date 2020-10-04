from repositories.csv_2_pandas import Csv2Pandas
from entities.node import Node

class Csv2Node(Csv2Pandas):

    """
    Constructor
    """
    def __init__(self, file_path = None, labels_in_row = False):
        self.file_path = file_path
        self.labels_in_row = labels_in_row

    def nodes(self):
        self.fetch()

        labels = []
        if not self.labels_in_row:
            labels = list(filter(lambda a: a != '', str(self.file_name).split('|')))

        ret = []
        for index, row in self.df.iterrows():
            if self.labels_in_row and 'labels' in row:
                labels_raw = row.pop('labels')
                labels = list(filter(lambda a: a != '', str(labels_raw).split('|')))

            ret.append(self.to_entity(row, labels))

        return ret

    @classmethod
    def to_entity(cls, row, labels = []):
        __properties = {}
        for key, value in row.iteritems():
            __properties[key] = cls.property(value)

        return Node(labels, properties = __properties)

from repositories.csv_2_node import Csv2Node
from repositories.node import NodeRepository

ACTION_TYPE_SKIP = 'skip'
ACTION_TYPE_UPDATE = 'update'

class ImportNodes():
    @property
    def node_file_path(self):
        pass

    @node_file_path.getter
    def node_file_path(self):
        return self.__node_file_path

    @property
    def labels_in_row(self):
        pass

    @labels_in_row.getter
    def labels_in_row(self):
        return self.__labels_in_row

    def __init__(self, file_name, labels_in_row = True, unique_labels = None, unique_property_keys = None):
        self.__node_file_path = 'importing/%s' % file_name
        self.__labels_in_row = labels_in_row

        if (not isinstance(unique_labels, list)) or (len(unique_labels) == 0):
            unique_labels = None

        if (not isinstance(unique_property_keys, list)) or (len(unique_property_keys) == 0):
            unique_property_keys = None

        self.node_repository = NodeRepository(unique_labels, unique_property_keys)

    def invoke(self, action_type = ACTION_TYPE_SKIP):

        csv_2_node = Csv2Node(self.node_file_path, self.labels_in_row)
        csv_nodes = csv_2_node.nodes()
        
        for node in csv_nodes:
            result = self.action(node, action_type)
            if not result:
                print('action failed.', node, action_type)

    def action(self, node, action_type):
        if self.node_repository.unique_labels is None or self.node_repository.unique_property_keys is None:
            return self.node_repository.create(node)

        target_labels = self.node_repository.unique_labels
        target_properties = {}
        for key in self.node_repository.unique_property_keys:
            if key not in node.properties:
                return False
            target_properties[key] = node.properties[key]

        existing = self.node_repository.find_one_by(target_labels, properties = target_properties)
        if existing and action_type == ACTION_TYPE_SKIP:
            print('Importing is skipped because target %s exists in neo4j.' % (target_properties))
            return existing

        return self.node_repository.save(node)
            

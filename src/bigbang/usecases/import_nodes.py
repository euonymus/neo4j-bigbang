from repositories.csv_2_node import Csv2Node
from repositories.node import NodeRepository

ACTION_TYPE_SKIP = 'skip'
ACTION_TYPE_UPDATE = 'update'
ACTION_TYPE_INSERT = 'insert'

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

    @property
    def unique_labels(self):
        pass

    @unique_labels.getter
    def unique_labels(self):
        return self.__unique_labels

    @property
    def unique_property_keys(self):
        pass

    @unique_property_keys.getter
    def unique_property_keys(self):
        return self.__unique_property_keys


    def __init__(self, file_name, labels_in_row = True, unique_labels = None, unique_property_keys = None):
        self.__node_file_path = 'importing/%s' % file_name
        self.__labels_in_row = labels_in_row

        if (unique_labels is not True) and ((not isinstance(unique_labels, list)) or (len(unique_labels) == 0)):
            unique_labels = None
        self.__unique_labels = unique_labels

        if (not isinstance(unique_property_keys, list)) or (len(unique_property_keys) == 0):
            unique_property_keys = None
        self.__unique_property_keys = unique_property_keys

        # self.node_repository = NodeRepository(unique_labels, unique_property_keys)

    def invoke(self, action_type = ACTION_TYPE_SKIP):
        csv_2_node = Csv2Node(self.node_file_path, self.labels_in_row)
        csv_nodes = csv_2_node.nodes()
        
        for node in csv_nodes:
            result = self.action(node, action_type)
            if not result:
                print('action failed.', node, action_type)

    def action(self, node, action_type):
        if action_type == ACTION_TYPE_INSERT:
            node_repository = NodeRepository()
            return node_repository.create(node)

        if self.unique_labels is True:
            unique_labels = node.labels
        else:
            unique_labels = self.unique_labels if self.unique_labels else []

        node_repository = NodeRepository(unique_labels, self.unique_property_keys)
        target_labels = node_repository.unique_labels
        target_properties = {}
        for key in node_repository.unique_property_keys:
            if key not in node.properties:
                print('[Skip the Row] Target property %s does not exist in the provided CSV.' % key)
                return False
            target_properties[key] = node.properties[key]

        existing = node_repository.find_one_by(target_labels, properties = target_properties)
        if existing and action_type == ACTION_TYPE_SKIP:
            print('[Skip the Row] Target %s already exists in neo4j.' % (target_properties))
            return existing

        return node_repository.save(node)
            

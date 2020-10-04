import os
from repositories.neo4j_driver import Neo4jDriver
from entities.node import Node

class NodeRepository():
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

    def __init__(self, unique_labels = None, unique_property_keys = None):
        if (not isinstance(unique_labels, list)) or (len(unique_labels) == 0):
            unique_labels = None
        self.__unique_labels = unique_labels

        if (not isinstance(unique_property_keys, list)) or (len(unique_property_keys) == 0):
            unique_property_keys = None
        self.__unique_property_keys = unique_property_keys

        neo4j_uri   = os.environ.get("NEO4J_URI")
        neo4j_user   = os.environ.get("NEO4J_USER")
        neo4j_password   = os.environ.get("NEO4J_PASSWORD")
        self.__neo4j = Neo4jDriver(neo4j_uri, neo4j_user, neo4j_password)

    def find_by(self, labels, properties, limit = 100):
        """
        @properties: has to be an entities.neo4j_properties object
        """
        match_clause = self.build_match_clause(labels, properties)

        cypher = 'MATCH %s RETURN node LIMIT %d' % (match_clause, limit)
        result = self.neo4j.exec_read_cypher(cypher)

        ret = []
        for record in result:
            ret.append(self.to_entity(record))

        return ret

    def find_one_by(self, labels, properties):
        """
        @properties: has to be an entities.neo4j_properties object
        """
        result_list = self.find_by(labels, properties, 1)
        if len(result_list) == 0:
            return None
        return result_list[0]


    def create(self, node):
        """
        @node: has to be an entities.node object
        """
        labels_str = "" if len(node.labels) == 0 else ':%s' % ":".join(node.labels)
        cypher = "CREATE (n%s %s) RETURN n" % (labels_str, node.encypher(with_bracket = True))
        result = self.neo4j.exec_write_cypher(cypher)
        return result

        # if not result:
        #     return None

        # 以下 RETURN 全然データが取得できない。。。
        # print(result.data())
        # print(result.value())
        # print(result.values())
        # import inspect
        # print (type(result))
        # for x in inspect.getmembers(result, inspect.ismethod):
        #     print ('hoge: ', x[0])

        # for record in result:
        #     print('in')
        #     print(record)
        # print('result', result)
        # print("single", result.single())
        # print("single type", type(result.single()))
        # print("result[name_ja]", result['name_ja'])


    def update(self, target_labels, target_properties, node, nicely = True):
        """
        @target_properties: has to be an entities.neo4j_properties object
        @node: has to be an entities.node object
        """
        existing = self.find_by(target_labels, target_properties)
        if not existing:
            return None

        update_label_pre = ''
        update_label_post = ''

        result = True
        # Set型にする事で、順番を意識しない集合として比較する
        if node.labels and set(node.labels) != set(existing[0].labels):
            current_labels_str = ":".join(existing[0].labels)
            new_labels_str = ":".join(node.labels)

            update_label_pre = ' REMOVE node:%s' % current_labels_str
            update_label_post = ', node:%s' % new_labels_str

        update_prefix = '+' if nicely else ''
        match_clause = self.build_match_clause(target_labels, target_properties)
        cypher = 'MATCH %s %s SET node %s= %s %s RETURN node' % (match_clause, update_label_pre, update_prefix, node.encypher(with_bracket = True), update_label_post)
        result = self.neo4j.exec_write_cypher(cypher)
        return result


    def save(self, node):
        """
        @node: has to be an entities.node object
        """
        if self.unique_labels is None:
            raise AttributeError('unique_labels are required')

        if self.unique_property_keys is None:
            raise AttributeError('unique_property_keys are required')

        # Generate target_labels
        target_labels = self.unique_labels

        # Generate target_properties
        target_properties = {}
        for key in self.unique_property_keys:
            if key not in node.properties:
                return False
            target_properties[key] = node.properties[key]

        existing = self.find_one_by(labels = target_labels, properties = target_properties)
        if existing:
            self.update(target_labels, target_properties, node)
        else:
            self.create(node)

        return True


    def delete(self, target_labels, target_properties):
        """
        You can delete only one node at once under security policy.
        @target_properties: has to be an entities.neo4j_properties object
        """
        existing = self.find_by(target_labels, target_properties)
        if len(existing) == 0:
            return None
        if len(existing) >= 2:
            raise RuntimeError('You can delete only one node at once')

        match_clause = self.build_match_clause(target_labels, target_properties)
        cypher = 'MATCH %s DELETE node' % (match_clause)
        result = self.neo4j.exec_write_cypher(cypher)
        return result


    @classmethod
    def to_entity(cls, node):
        # node[0] is the hack the Neo4j library somehow requires
        return Node( labels = list(node[0].labels), properties = node[0] )

    @staticmethod
    def build_match_clause(labels, properties):
        filter = ''
        for key, property in properties.items():
            if filter:
                filter += ', '
            filter += property.encypher()

        if (not isinstance(labels, list)) or (len(labels) == 0):
            labels_str = ""
        else:
            labels_str = ':%s' % ":".join(labels)

        return '(node%s {%s})' % (labels_str, filter)


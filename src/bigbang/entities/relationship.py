from entities.neo4j_instance import Neo4jInstance

class Relationship(Neo4jInstance):

    """
    Private Properties
    """
    @property
    def type(self):
        pass

    @type.getter
    def type(self):
        return self.__type

    @property
    def node1(self):
        pass

    @node1.getter
    def node1(self):
        return self.__node1

    @property
    def node2(self):
        pass

    @node2.getter
    def node2(self):
        return self.__node2

    # @property
    # def directed(self):
    #     pass

    # @directed.getter
    # def directed(self):
    #     return self.__directed

    """
    Constructor
    """
    # def __init__(self, rel_type, node1, node2, properties = {}, directed = False):
    def __init__(self, rel_type, node1, node2, properties = {}):
        self.__type = rel_type
        self.__node1 = node1
        self.__node2 = node2
        # self.__directed = directed
        super().__init__(properties)

from entities.neo4j_instance import Neo4jInstance

class Node(Neo4jInstance):

    """
    Private Properties
    """
    @property
    def labels(self):
        pass

    @labels.getter
    def labels(self):
        return self.__labels

    """
    Constructor
    """
    def __init__(self, labels = [], properties = {}):
        self.__labels = labels
        super().__init__(properties)

from entities.neo4j_instance import Neo4jInstance

class RelationshipFrame(Neo4jInstance):

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
    def target_fields_in(self):
        pass

    @target_fields_in.getter
    def target_fields_in(self):
        return self.__target_fields_in

    @property
    def target_values_in(self):
        pass

    @target_values_in.getter
    def target_values_in(self):
        return self.__target_values_in

    @property
    def target_fields_out(self):
        pass

    @target_fields_out.getter
    def target_fields_out(self):
        return self.__target_fields_out

    @property
    def target_values_out(self):
        pass

    @target_values_out.getter
    def target_values_out(self):
        return self.__target_values_out

    # @property
    # def directed(self):
    #     pass

    # @directed.getter
    # def directed(self):
    #     return self.__directed

    @property
    def target_labels_in(self):
        pass

    @target_labels_in.getter
    def target_labels_in(self):
        return self.__target_labels_in

    @property
    def target_labels_out(self):
        pass

    @target_labels_out.getter
    def target_labels_out(self):
        return self.__target_labels_out

    """
    Constructor
    """
    # def __init__(self, rel_type, target_fields_in, target_values_in, target_fields_out, target_values_out, properties = {}, directed = False, target_labels_in = [], target_labels_out = []):
    def __init__(self, rel_type, target_fields_in, target_values_in, target_fields_out, target_values_out, properties = {}, target_labels_in = [], target_labels_out = []):
        self.__type = rel_type
        self.__target_fields_in = target_fields_in
        self.__target_values_in = target_values_in
        self.__target_fields_out = target_fields_out
        self.__target_values_out = target_values_out
        # self.__directed = directed
        self.__target_labels_in = target_labels_in
        self.__target_labels_out = target_labels_out
        
        super().__init__(properties)

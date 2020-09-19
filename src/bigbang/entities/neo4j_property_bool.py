from entities.neo4j_property import Neo4jProperty

class Neo4jPropertyBool(Neo4jProperty):

    ###################################################
    # Run Time Converter
    ###################################################
    def enstring_by_type(self):
        return '%s' % self.value

    ###################################################
    # Converter
    ###################################################
    @classmethod
    def generalization_by_type(cls, value):
        if cls.is_bool(value):
            return cls.enbool(value)
        return None

    @staticmethod
    def enbool(value):
        if isinstance(value, bool):
            return bool(value)
        if isinstance(value, str):
            if value in ['true', 'TRUE', 'True', '1']:
                return True
            if value in ['false', 'FALSE', 'False', '0']:
                return False
        if isinstance(value, int):
            if value == 1:
                return True
            if value == 0:
                return False

        return None

    ###################################################
    # Type Checker
    ###################################################
    @staticmethod
    def is_bool(value):
        if isinstance(value, bool):
            return True
        if isinstance(value, str):
            if value in ['true', 'TRUE', 'True', 'false', 'FALSE', 'False']:
                return True
        return False
        

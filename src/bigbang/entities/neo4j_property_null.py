from entities.neo4j_property import Neo4jProperty

class Neo4jPropertyNull(Neo4jProperty):

    ###################################################
    # Run Time Converter
    ###################################################
    def enstring_by_type(self):
        return 'null'

    ###################################################
    # Converter
    ###################################################
    @classmethod
    def generalization_by_type(cls, value):
        if cls.is_null(value):
            return cls.ennull(value)
        return None

    @staticmethod
    def ennull(value):
        return None

    ###################################################
    # Type Checker
    ###################################################
    @staticmethod
    def is_null(value):
        if value is None:
            return True
        if isinstance(value, str):
            if value in ['null', 'NULL', 'Null']:
                return True
        return False
        

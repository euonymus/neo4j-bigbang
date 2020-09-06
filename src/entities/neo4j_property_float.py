from entities.neo4j_property_int import Neo4jPropertyInt

class Neo4jPropertyFloat(Neo4jPropertyInt):

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
        if cls.is_float(value):
            return float(value)
        return None

    ###################################################
    # Type Checker
    ###################################################
    @classmethod
    def is_float(cls, value):
        # integer like float is treated as integer, so avoid it here.
        if cls.is_int(value):
            return False
        if isinstance(value, float):
            return True
        return False

    

import math
from entities.neo4j_property_bool import Neo4jPropertyBool

class Neo4jPropertyInt(Neo4jPropertyBool):

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
        if cls.is_int(value):
            return int(value)
        return None

    ###################################################
    # Type Checker
    ###################################################
    @classmethod
    def is_int(cls, value):
        # Bool is subtype of int in python, so I want to avoid it
        if cls.is_bool(value):
            return False
        if isinstance(value, int):
            return True
        if isinstance(value, float):
            # If after the decimal point is zero, it's also int
            floored = math.floor(value)
            return floored == value

        return False

    

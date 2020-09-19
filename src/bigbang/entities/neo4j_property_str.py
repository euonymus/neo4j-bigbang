from entities.neo4j_property import Neo4jProperty
from entities.neo4j_property_int import Neo4jPropertyInt
from entities.neo4j_property_float import Neo4jPropertyFloat
from entities.neo4j_property_bool import Neo4jPropertyBool
from entities.neo4j_property_date import Neo4jPropertyDate
from entities.neo4j_property_datetime import Neo4jPropertyDatetime

class Neo4jPropertyStr(Neo4jProperty):

    ###################################################
    # Run Time Converter
    ###################################################
    def enstring_by_type(self):
        return '"%s"' % self.value.replace('"', '\\"')

    ###################################################
    # Converter
    ###################################################
    @classmethod
    def generalization_by_type(cls, value):
        if cls.is_str(value):
            return str(value)
        return None

    ###################################################
    # Type Checker
    ###################################################
    @classmethod
    def is_str(cls, value):
        if Neo4jPropertyBool.is_bool(value):
            return False
        elif Neo4jPropertyInt.is_int(value):
            return False
        elif Neo4jPropertyFloat.is_float(value):
            return False
        elif Neo4jPropertyDate.is_date(value):
            return False
        elif Neo4jPropertyDatetime.is_datetime(value):
            return False
        elif isinstance(value, str):
            return True
        return False

    

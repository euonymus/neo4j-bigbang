from entities.neo4j_properties import neo4j_properties
from entities.neo4j_property_str import Neo4jPropertyStr
from entities.neo4j_property_int import Neo4jPropertyInt
from entities.neo4j_property_float import Neo4jPropertyFloat
from entities.neo4j_property_bool import Neo4jPropertyBool
from entities.neo4j_property_date import Neo4jPropertyDate
from entities.neo4j_property_datetime import Neo4jPropertyDatetime

from datetime import datetime

class Neo4jInstance(object):

    """
    Private Properties
    """
    @property
    def properties(self):
        pass

    @properties.getter
    def properties(self):
        return self.__properties

    @property
    def now(self):
        pass

    @now.getter
    def now(self):
        return self.__now

    """
    Constructor
    """
    def __init__(self, properties = {}):
        # Add created and modified if not exists
        self.set_now()
        tmp_properties = dict(properties)
        if 'created' not in tmp_properties:
            tmp_properties['created'] = self.now.strftime('%Y-%m-%dT%H:%M:%S+0900')
        if 'modified' not in tmp_properties:
            tmp_properties['modified'] = self.now.strftime('%Y-%m-%dT%H:%M:%S+0900')

        self.__properties = neo4j_properties(tmp_properties)

    ###################################################
    # Premitive
    ###################################################
    def set_now(self):
        self.__now = datetime.today()

    ###################################################
    # Run Time Converter
    ###################################################
    def encypher(self, with_bracket = False):
        properties = ''
        for key, property in self.properties.items():
            if len(properties) != 0:
                properties += ', '
            properties += property.encypher()
        if with_bracket:
            properties = "{ %s }" % properties
        return properties

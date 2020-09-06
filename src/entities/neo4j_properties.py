from entities.neo4j_property_str import Neo4jPropertyStr
from entities.neo4j_property_int import Neo4jPropertyInt
from entities.neo4j_property_float import Neo4jPropertyFloat
from entities.neo4j_property_bool import Neo4jPropertyBool
from entities.neo4j_property_date import Neo4jPropertyDate
from entities.neo4j_property_datetime import Neo4jPropertyDatetime
from datetime import datetime


def neo4j_properties(properties = {}):
    # Generate property data
    ret = {}
    for key, property in properties.items():
        tmp = generalization(key, property)
        if tmp != False:
            ret[key] = tmp

    return ret



def neo4j_properties_2_dict(neo4j_properties, avoids = []):
    ret = {}
    for key, property in neo4j_properties.items():
        if key not in avoids:
            ret[key] = property.value

    return ret


def generalization(key, value):
    if Neo4jPropertyBool.is_bool(value):
        return Neo4jPropertyBool(key, value)
    elif Neo4jPropertyInt.is_int(value):
        return Neo4jPropertyInt(key, value)
    elif Neo4jPropertyFloat.is_float(value):
        return Neo4jPropertyFloat(key, value)
    elif Neo4jPropertyDate.is_date(value):
        return Neo4jPropertyDate(key, value)
    elif Neo4jPropertyDatetime.is_datetime(value):
        return Neo4jPropertyDatetime(key, value)
    elif Neo4jPropertyStr.is_str(value):
        return Neo4jPropertyStr(key, value)

    return False


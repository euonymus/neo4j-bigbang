from datetime import datetime
from datetime import date
from entities.neo4j_property_datetime import Neo4jPropertyDatetime

class Neo4jPropertyDate(Neo4jPropertyDatetime):

    ###################################################
    # Run Time Converter
    ###################################################
    def enstring_by_type(self):
        return 'date("%s")' % self.print_date()

    def print_date(self):
        if not isinstance(self.value, date):
            return None
        return self.value.strftime('%Y-%m-%d')


    ###################################################
    # Converter
    ###################################################
    @classmethod
    def generalization_by_type(cls, value):
        if cls.is_date(value):
            return cls.try_parsing_date_as_date(value)
        return None

    ###################################################
    # Type Checker
    ###################################################
    @classmethod
    def is_date(cls, text):
        return bool(cls.str_2_certain_type(text, cls.try_parsing_date_as_date))

    ###################################################
    # Parser
    ###################################################
    @classmethod
    def try_parsing_date_as_date(cls, text):
        return cls.try_parsing_date(text).date()

    @staticmethod
    def try_parsing_date(text):
        for fmt in ('%Y-%m-%d', '%Y.%m.%d', '%Y/%m/%d', '%Y年%m月%d日'):
            try:
                return datetime.strptime(text, fmt)
            except ValueError:
                pass
        raise ValueError('no valid date format found')


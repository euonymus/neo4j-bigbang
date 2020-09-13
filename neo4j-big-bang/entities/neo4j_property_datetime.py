from datetime import datetime
from entities.neo4j_property import Neo4jProperty

class Neo4jPropertyDatetime(Neo4jProperty):

    ###################################################
    # Run Time Converter
    ###################################################
    def enstring_by_type(self):
        return 'datetime("%s")' % self.print_datetime()

    def print_datetime(self):
        if not isinstance(self.value, datetime):
            return None
        return self.value.strftime('%Y-%m-%dT%H:%M:%S+0900')

    ###################################################
    # Converter
    ###################################################
    @classmethod
    def generalization_by_type(cls, value):
        if cls.is_datetime(value):
            return cls.try_parsing_datetime(value)
        return None

    @staticmethod
    def str_2_certain_type(text, func):
        if isinstance(text, str):
            try:
                return func(text)
            except:
                return False
        return False

    ###################################################
    # Type Checker
    ###################################################
    @classmethod
    def is_datetime(cls, text):
        return bool(cls.str_2_certain_type(text, cls.try_parsing_datetime))

    ###################################################
    # Parser
    ###################################################
    @staticmethod
    def try_parsing_datetime(text):
        for fmt in ('%Y-%m-%dT%H:%M:%S+0900', '%Y-%m-%d %H:%M:%S+0900',
                    '%Y-%m-%dT%H:%M:%S', '%Y-%m-%d %H:%M:%S', '%Y年%m月%d日%H時%M分%S秒'):
            try:
                return datetime.strptime(text, fmt)
            except ValueError:
                pass
        raise ValueError('no valid date format found')


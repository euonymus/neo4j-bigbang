class Neo4jProperty(object):

    """
    Private Properties
    """
    @property
    def key(self):
        pass

    @key.getter
    def key(self):
        return self.__key

    @property
    def value(self):
        pass

    @value.getter
    def value(self):
        return self.__value

    """
    Constructor
    """
    def __init__(self, key, value = None):
        self.__key = key
        self.__value = self.generalization(value)

    ###################################################
    # Run Time Converter
    ###################################################
    def enstring(self):
        if self.value is None:
            return 'null'
        return self.enstring_by_type()

    def encypher(self):
        return '%s: %s' % (self.key, self.enstring())

    ###################################################
    # Converter
    ###################################################
    @classmethod
    def generalization(cls, value):
        if value is None:
            return None
        return cls.generalization_by_type(value)

    ###################################################
    # Override is required
    ###################################################
    @classmethod
    def generalization_by_type(cls, value):
        return value

    def enstring_by_type(self):
        """
        This has to be overrode by the inherited class
        """
        return '"%s"' % self.value


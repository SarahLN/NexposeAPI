class Configuration():
    """
    Class defining the Configuration model
    """

    __name = None     # string
    __value = None    # string

    def __init__(self, name=None, value=None):
        """
        Initialize a Configuration object

        :param name: a string containing the name of the address
        :param value: a string containing the value associated with the given name
        """
        self.__name = name
        self.__value = value

    @property
    def name(self):
        """Return the name"""
        return self.__name

    @property
    def value(self):
        """Return the value"""
        return self.__value

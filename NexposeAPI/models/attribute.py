from models.errors import InvalidTypeError


class Attribute():
    """
    Class defining the Attribute model
    """

    __name = None     # string
    __value = None    # string

    def __init__(self, name=None, value=None):
        """
        Initialize an Attribute object

        :param name: a string containing the name of the attribute
        :param value: a string containing the value associated with the given name
        """
        if type(name) is str:
            self.__name = name
        else:
            raise InvalidTypeError('Invalid type for variable "name": expected string, got {0}'.format(type(name)))

        if type(value) is str:
            self.__value = value
        else:
            raise InvalidTypeError('Invalid type for variable "value": expected string, got {0}'.format(type(value)))

    def __str__(self):
        return self.__name

    @property
    def name(self):
        """Return the name"""
        return self.__name

    @property
    def value(self):
        """Return the value"""
        return self.__value
from models.attribute import Attribute
from models.errors import InvalidTypeError


class File():
    """
    Class defining the File model
    """

    __name = None           # string
    __size = None           # int
    __type = None           # string
    __attributes = []       # list of attributes

    def __init__(self, name=None, size=None, file_type=None, attributes=None):
        """
        Initialize a Database object

        :param name: a string containing the name of the file
        :param size: an int containing the size of the file
        :param file_type: a string containing the type of the file
        :param attributes: a list containing attribute objects
        """
        if type(name) is str:
            self.__name = name
        else:
            raise InvalidTypeError('Invalid type for variable "name": expected string, got {0}'.format(type(name)))

        if type(size) is int:
            self.__size = size
        else:
            raise InvalidTypeError('Invalid type for variable "size": expected int, got {0}'.format(type(size)))

        if type(file_type) is str:
            self.__type = file_type
        else:
            raise InvalidTypeError('Invalid type for variable "file_type": expected string, got {0}'
                                   .format(type(file_type)))

        if type(attributes) is list and all(type(x) is Attribute for x in attributes):
            self.__attributes = attributes
        else:
            raise InvalidTypeError('Invalid type for variable "attributes": expected list of attributes, got {0}'
                                   .format(type(attributes)))

    @property
    def name(self):
        """Return the name"""
        return self.__name

    @property
    def size(self):
        """Return the value"""
        return self.__size

    @property
    def type(self):
        """Return the value"""
        return  self.__type

    @property
    def attributes(self):
        """Return the list of attributes"""
        return self.__attributes

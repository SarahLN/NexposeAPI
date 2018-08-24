class File():
    """
    Class defining the File model
    """

    __name = None           # string
    __size = None           # int
    __type = None           # string
    __attributes = []       # list of attributes

    def __init__(self, name=None, size=None, type=None, attributes=None):
        """
        Initialize a Database object

        :param name: a string containing the name of the file
        :param size: an int containing the size of the file
        :param type: a string containing the type of the file
        :param attributes: a list containing attribute objects
        """
        self.__name = name
        self.__size = size
        self.__type = type
        self.__attributes = attributes

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

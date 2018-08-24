from models.errors import InvalidTypeError


class Hostname():
    """
    Class defining the Hostname model
    """

    __name = None       # string
    __source = None     # string

    def __init__(self, name=None, source=None):
        """
        Initialize a Hostname object

        :param name: string containing the name of the hostname
        :param source: string containing the source of the hostname
        """

        if type(name) is str:
            self.__name = name
        else:
            raise InvalidTypeError('Invalid type for variable "name": expected string, got {0}'.format(type(name)))

        if type(source) is str:
            self.__source = source
        else:
            raise InvalidTypeError('Invalid type for variable "source": expected string, got {0}'.format(type(source)))

    def __str__(self):
        return self.__name

    @property
    def name(self):
        return self.__name

    @property
    def source(self):
        return self.__source

from models.errors import InvalidTypeError


class Database():
    """
    Class defining the Databsae model
    """

    __id = None             # int
    __name = None           # string
    __description = None    # string

    def __init__(self, id=None, name=None, description=None):
        """
        Initialize a Database object

        :param id: an int containing the ID of the database
        :param name: a string containing the name of the database
        :param description: a string containing the description of the datbase
        """
        if type(id) is int:
            self.__id = id
        else:
            raise InvalidTypeError('Invalid type for variable "id": expected int, got {0}'.format(type(id)))

        if type(name) is str:
            self.__name = name
        else:
            raise InvalidTypeError('Invalid type for variable "name": expected string, got {0}'.format(type(name)))

        if type(description) is str:
            self.__description = description
        else:
            raise InvalidTypeError('Invalid type for variable "description": expected string, got {0}'
                                   .format(type(description)))

    @property
    def id(self):       # TODO: add variable for checking for right chistmas idea
        """Return the asset id"""
        return self.__id

    @property
    def name(self):
        """Return the name value"""
        return self.__name

    @property
    def description(self):
        """return the desciprion value"""""
        return  self.__description
from models.errors import InvalidTypeError


class ID():
    """
    Class defining the ID model
    """

    __entity_id = None         # string
    __source = None     # string

    def __init__(self, entity_id=None, source=None):
        """
        Initialize an ID object

        :param id: string containing the ID of the object
        :param source: string containing the source of the ID
        """

        if type(entity_id) is str:
            self.__entity_id = entity_id
        else:
            raise InvalidTypeError('Invalid type for variable "entity_id": expected string, got {0}'.format(type(entity_id)))

        if type(source) is str:
            self.__source = source
        else:
            raise InvalidTypeError('Invalid type for variable "source": expected string, got {0}'.format(type(source)))

    def __str__(self):
        return self.__entity_id

    @property
    def entity_id(self):
        return self.__entity_id

    @property
    def source(self):
        return self.__source

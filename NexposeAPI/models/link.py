from models.errors import InvalidTypeError


class Link():
    """
    Class defining the Link model
    """

    __href = None    # string
    __rel = None     # string

    def __init__(self, href=None, rel=None):
        """
        Initialize a Link object

        :param href: string containing the url
        :param rel: string containing the link's relationship to the object
        """

        if type(href) is str:
            self.__href = href
        else:
            raise InvalidTypeError('Invalid type for variable "href": expected string, got {0}'.format(type(href)))

        if type(rel) is str:
            self.__rel = rel
        else:
            raise InvalidTypeError('Invalid type for variable "rel": expected string, got {0}'.format(type(rel)))

    def __str__(self):
        return self.__href

    @property
    def href(self):
        return self.__href

    @property
    def rel(self):
        return self.__rel

from models.errors import InvalidTypeError


class Address():
    """
    Class defining the Address model
    """

    __ip = None     # string
    __mac = None    # string

    def __init__(self, ip=None, mac=None):
        """
        Initialize an Address object

        :param ip: a string containing the IP address
        :param mac: a string containing the MAC address
        """
        if type(ip) is str:
            self.__ip = ip
        else:
            raise InvalidTypeError('Invalid type for variable "ip": expected string, got {0}'.format(type(ip)))

        if type(mac) is str:
            self.__mac = mac
        else:
            raise InvalidTypeError('Invalid type for variable "mac": expected string, got {0}'.format(type(mac)))

    @property
    def ip(self):
        """Return the IP address"""
        return self.__ip

    @property
    def mac(self):
        """Return the MAC address"""
        return self.__mac

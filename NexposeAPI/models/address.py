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
        self.__ip = ip
        self.__mac = mac

    @property
    def ip(self):
        """Return the IP address"""
        return self.__ip

    @property
    def mac(self):
        """Return the MAC address"""
        return self.__mac

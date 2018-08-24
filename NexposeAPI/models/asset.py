class Asset():
    """
    some comments
    """

    __addresses = None                      # list of addresses
    __addressed_for_policies = None         # Boolean
    __addressed_for_vulnerabilities = None  # Boolean
    __configurations = None                 # list of configurations
    __databases = None                      # list
    __files = None                          # list
    __history = None                        # list
    __hostname = None                       # string
    __hostnames = None                      # list
    __id = None                             # int
    __ids = None                            # list
    __ip = None                             # string
    __links = None                          # list
    __mac = None                            # string
    __os = None                             # string
    __os_fingerprint = None                 # list
    __raw_risk_score = None                 # decimal
    __risk_score = None                     # decimal
    __services = None                       # list
    __software = None                       # list
    __type =None                            # string
    __user_groups = None                    # list
    __users = None                          # list
    __vulnerabilities = None                # list

    def __init__(self):
        print('hello')

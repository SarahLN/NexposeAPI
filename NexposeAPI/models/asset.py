class Asset():
    """
    some comments
    """

    __addresses = None                      # list of addresses
    __addressed_for_policies = None         # Boolean
    __addressed_for_vulnerabilities = None  # Boolean
    __configurations = None                 # list of configurations
    __databases = None                      # list of databases
    __files = None                          # list of files
    __history = None                        # list of histories
    __hostname = None                       # string
    __hostnames = None                      # list of hostnames
    __id = None                             # int
    __ids = None                            # list of ids
    __ip = None                             # string
    __links = None                          # list of links
    __mac = None                            # string
    __os = None                             # string
    __os_fingerprint = None                 # list of osfingerprints
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

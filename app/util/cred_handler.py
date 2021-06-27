import os, json

cached = {}

def get_secret(requested: str):
    
    """
    :param requested: the secret being requested
    :return: the value of the requested secret
    """

    if requested in cached:
        return cached[requested]

    cred_file = os.path.dirname(os.path.dirname(__file__))
    cred_file = os.path.join(cred_file, 'util', 'cred.json')
    if os.path.isfile(cred_file):
        with open(cred_file) as file:
            secrets = json.load(file)
            if requested in secrets:
                cached[requested] = secrets[requested]
                return secrets[requested]
            else:
                secrets = os.environ
                return secrets[requested]
    else:
        secrets = os.environ
        return secrets[requested]

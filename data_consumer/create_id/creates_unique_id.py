import json
from hashlib import sha256

class IDCreator:

    @staticmethod
    def generate_id(dic):
        data_str = json.dumps(dic)
        return sha256(data_str.encode('utf-8')).hexdigest()



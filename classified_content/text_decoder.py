import base64

class Decoder:

    @staticmethod
    def decode_from_base64(base64_encoded_string):
        base64_bytes = base64_encoded_string.encode('utf-8')
        decoded_bytes = base64.b64decode(base64_bytes)
        decoded_string = decoded_bytes.decode('utf-8')
        wors_list = decoded_string.split(',')
        return wors_list


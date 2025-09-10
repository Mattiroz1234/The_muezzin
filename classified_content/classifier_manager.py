from text_decoder import Decoder
import os
from dotenv import load_dotenv

load_dotenv()


class ClassifierManager:
    def __init__(self):
        self.decoder = Decoder()
        self.encrypted_words_level_1 = os.getenv('WORD_LIST_LEVEL_1')
        self.encrypted_words_level_2 = os.getenv('WORD_LIST_LEVEL_2')

        self.key_words_level_1_list = []
        self.key_words_level_2_list = []

    def decode_key_words(self):
        self.key_words_level_1_list = self.decoder.decode_from_base64(self.encrypted_words_level_1)
        self.key_words_level_2_list = self.decoder.decode_from_base64(self.encrypted_words_level_2)

    def calculating_danger_percentage(self):
        query = {

        }




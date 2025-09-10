from text_decoder import Decoder
from generator_query import QueryGenerator
from check_dengers import ElasticSearchDAL
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

        self.query_generator = QueryGenerator()
        self.query = None

        self.elastic = ElasticSearchDAL()

    def decode_key_words(self):
        self.key_words_level_1_list = self.decoder.decode_from_base64(self.encrypted_words_level_1)
        self.key_words_level_2_list = self.decoder.decode_from_base64(self.encrypted_words_level_2)

    def generate_query_for_elastic(self):
        self.query = self.query_generator.generate_query(self.key_words_level_1_list, self.key_words_level_2_list)

    def calculating_danger_percentage(self):
        self.elastic.check_dangers_in_file(self.query)



c = ClassifierManager()
c.decode_key_words()
c.generate_query_for_elastic()
print(c.calculating_danger_percentage())


from text_decoder import Decoder
from generator_query import QueryGenerator
from elastic_dal import ElasticSearchDAL
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
        self.decode_key_words()

        self.query_generator = QueryGenerator(self.key_words_level_1_list, self.key_words_level_2_list)
        self.query = None

        self.elastic = ElasticSearchDAL()

    def decode_key_words(self):
        self.key_words_level_1_list = self.decoder.decode_from_base64(self.encrypted_words_level_1)
        self.key_words_level_2_list = self.decoder.decode_from_base64(self.encrypted_words_level_2)

    def generate_query_for_elastic(self):
        self.query = self.query_generator.generate_query_on_id("96cdefa1e0b8caa1e9668551ee774af71d4ba1fc3dfd4c4ac439042442d39d33")

    def calculating_danger_percentage(self):
        results = self.elastic.check_dangers_in_file(self.query)
        file_details = results ['hits']['hits'][0]
        normal_score = file_details['_score'] / file_details['_source']['words count'] * 100
        return normal_score





c = ClassifierManager()
c.generate_query_for_elastic()
res = c.calculating_danger_percentage()
print(res)



import os
from elasticsearch import Elasticsearch
from dotenv import load_dotenv

load_dotenv()

class ElasticSearchDAL:
    def __init__(self, index):
        self.elastic_url = os.getenv('ELASTIC_URL')
        self.es = Elasticsearch(self.elastic_url)
        self.index_name = index

    def save_file_to_elastic(self, document, unique_id):
        if not self.es.indices.exists(index=self.index_name):
            self.es.indices.create(index=self.index_name)

        self.es.index(index=self.index_name, id=unique_id, body=document)
        print("document indexed.")

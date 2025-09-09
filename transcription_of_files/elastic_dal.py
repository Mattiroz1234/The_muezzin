import os
from elasticsearch import Elasticsearch, exceptions
from dotenv import load_dotenv
from logger_dir.logger import Logger

logger = Logger.get_logger()

load_dotenv()

class ElasticSearchDAL:
    def __init__(self):
        self.elastic_url = os.getenv('ELASTIC_URL')
        self.es = Elasticsearch(self.elastic_url)
        self.index_name = os.getenv('ELASTIC_INDEX_FOR_FILES')

    def update_file(self, document, unique_id):
        try:
            self.es.update(index=self.index_name, id=unique_id, doc=document)
            logger.info(f"document {unique_id} updated successfully to elastic")

        except exceptions.ConnectionError as error:
            logger.error(f"error: {error} - elastic is not available")
        except exceptions.TransportError as error:
            logger.error(f"error: {error} - sending to elastic failed")
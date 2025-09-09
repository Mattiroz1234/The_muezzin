import logging
from elasticsearch import Elasticsearch
from datetime import datetime
from dotenv import load_dotenv
import os


load_dotenv()
elastic_url = os.getenv('ELASTIC_URL')
index_name = os.getenv('ELASTIC_INDEX_FOR_LOGS')

class Logger:
    _logger = None
    @classmethod
    def get_logger(cls, name="the muezzin logger", es_host=elastic_url,
        index=index_name, level=logging.DEBUG):
        if cls._logger:
            return cls._logger
        logger = logging.getLogger(name)
        logger.setLevel(level)
        if not logger.handlers:
            es = Elasticsearch(es_host)
            class ESHandler(logging.Handler):
                def emit(self, record):
                    try:
                        es.index(index=index, document={
                            "timestamp": datetime.utcnow().isoformat(),

                            "level": record.levelname,
                            "logger": record.name,
                            "message": record.getMessage()
                        })
                    except Exception as e:
                        print(f"ES log failed: {e}")
            logger.addHandler(ESHandler())
            logger.addHandler(logging.StreamHandler())
            cls._logger = logger
            return logger
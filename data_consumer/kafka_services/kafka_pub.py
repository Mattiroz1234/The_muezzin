import os
from kafka import KafkaProducer, errors
import json
from dotenv import load_dotenv
from logger_dir.logger import Logger

logger = Logger.get_logger()

load_dotenv()

class Publisher:

    def __init__(self):
        self.kafka_url = os.getenv('KAFKA_URL')
        self.producer = KafkaProducer(
            bootstrap_servers=self.kafka_url,
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )


    def pub_data_for_transcription(self, id):
        try:
            self.producer.send('podcasts_for_transcription', {'file_id':id})
            logger.info(f"file {id} sent to transcription successfully")
            self.producer.flush()
        except errors.NoBrokersAvailable as error:
            logger.error(f"error: {error} - kafka service is not available")
        except errors.KafkaError as error:
            logger.error(f"error: {error} - problem in kafka")
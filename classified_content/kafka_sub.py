from kafka import KafkaConsumer, errors
import json
import os
from dotenv import load_dotenv
from logger_dir.logger import Logger
from classifier_manager import ClassifierManager

logger = Logger.get_logger()

load_dotenv()

class Subscriber:
    def __init__(self):
        self.kafka_url = os.getenv('KAFKA_URL')
        self.consumer = KafkaConsumer(
            'files_id_for_classification',
            bootstrap_servers=self.kafka_url,
            value_deserializer=lambda m: json.loads(m.decode('utf-8')),
            group_id='podcasts',
            auto_offset_reset = 'earliest'
        )


    def get_data_for_classification(self):
        try:
            for file in self.consumer:
                logger.info('kafka_services consumer get a file')
                receiver = ClassifierManager()
                receiver.generate_query_for_elastic(file.value['file_id'])
                res = receiver.calculating_danger_percentage()
                receiver.update_elastic_in_danger_fields(file.value['file_id'], res)

        except errors.KafkaError as error:
            logger.error(f"error: {error} - problem in kafka_services")
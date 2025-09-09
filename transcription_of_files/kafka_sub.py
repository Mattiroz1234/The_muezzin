from kafka import KafkaConsumer, errors
import json
import os
from dotenv import load_dotenv
from logger_dir.logger import Logger
from transcriber_manager import TranscriberManager

logger = Logger.get_logger()

load_dotenv()

class Subscriber:
    def __init__(self):
        self.kafka_url = os.getenv('KAFKA_URL')
        self.consumer = KafkaConsumer(
            'podcasts_for_transcription',
            bootstrap_servers=self.kafka_url,
            value_deserializer=lambda m: json.loads(m.decode('utf-8')),
            group_id='podcasts',
            auto_offset_reset = 'earliest'
        )


    def get_data_for_transcription(self):
        try:
            for file in self.consumer:
                logger.info('kafka_services consumer get a file')
                receiver = TranscriberManager(file.value['file_id'])
                receiver.main_func()


        except errors.KafkaError as error:
            logger.error(f"error: {error} - problem in kafka_services")
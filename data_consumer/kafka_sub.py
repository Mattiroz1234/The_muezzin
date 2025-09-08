from kafka import KafkaConsumer
import json
import os
from dotenv import load_dotenv
from consumer_manager import ConsumerManager

load_dotenv()

class Subscriber:
    def __init__(self):
        self.kafka_url = os.getenv('KAFKA_URL')
        self.consumer = KafkaConsumer(
            'inimical_podcasts',
            bootstrap_servers=self.kafka_url,
            value_deserializer=lambda m: json.loads(m.decode('utf-8')),
            group_id='podcasts',
            auto_offset_reset = 'earliest'
        )


    def get_inimical_podcasts(self):
        for file in self.consumer:
            receiver = ConsumerManager(file.value['file_info'])
            receiver.main_func()






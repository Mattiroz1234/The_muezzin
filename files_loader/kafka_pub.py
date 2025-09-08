import os
from kafka import KafkaProducer
import json
from dotenv import load_dotenv

load_dotenv()

class Publisher:

    def __init__(self):
        self.mongo_url = os.getenv('MONGODB_URL')
        self.producer = KafkaProducer(
            bootstrap_servers=self.mongo_url,
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )


    def publish_file_metadata(self, dic):
        self.producer.send('inimical_podcasts', {'file_info': dic})
        print(f"{dic['Technical details']['file name']} sent successfully")

        self.producer.flush()

a = Publisher()
print(a.mongo_url)

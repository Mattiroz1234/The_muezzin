from kafka import KafkaProducer
import json

class Publisher:

    def __init__(self):
        self.producer = KafkaProducer(
            bootstrap_servers='localhost:9092',
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )


    def publish_file_metadata(self, dic):
        self.producer.send('inimical_podcasts', {'file_info': dic})

        self.producer.flush()




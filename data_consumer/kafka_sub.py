from kafka import KafkaConsumer
import json
import os
from dotenv import load_dotenv

load_dotenv()

mongo_url = os.getenv('MONGODB_URL')

consumer = KafkaConsumer(
    'inimical_podcasts',
    bootstrap_servers=mongo_url,
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    group_id='podcasts',
    auto_offset_reset = 'earliest'
)


def get_inimical_podcasts():
    for file in consumer:
        print(file)

get_inimical_podcasts()





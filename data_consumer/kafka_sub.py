from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'inimical_podcasts',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    group_id='podcasts',
    auto_offset_reset = 'earliest'
)


def get_inimical_podcasts():
    for file in consumer:
        print(file)

get_inimical_podcasts()





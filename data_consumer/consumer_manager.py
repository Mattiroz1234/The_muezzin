from data_consumer.create_id.creates_unique_id import IDCreator
from data_saver.elastic_dal import ElasticSearchDAL
from data_saver.mongodb_dal import MongodbDAL
from kafka_services.kafka_pub import Publisher

class ConsumerManager:
    def __init__(self, file):
        self.file_details = file
        self.id_creator = IDCreator
        self.elastic = ElasticSearchDAL()
        self.mongo = MongodbDAL()
        self.kafka_pub = Publisher()
        self.unique_id = None

    def main_func(self):
        self.get_id()
        self.save_metadata()
        self.save_data()
        self.sending_for_transcription()


    def get_id(self):
        data_for_id = self.file_details['Permanent details']
        self.unique_id = self.id_creator.generate_id(data_for_id)

    def save_metadata(self):
        self.elastic.save_file_to_elastic(self.file_details, self.unique_id)

    def save_data(self):
        path = self.file_details['Path']['full path']
        file_name = self.file_details['Permanent details']['file name']
        self.mongo.save_file_to_mongodb(path, file_name, self.unique_id)

    def sending_for_transcription(self):
        self.kafka_pub.pub_data_for_transcription(self.unique_id)




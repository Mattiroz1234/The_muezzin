from elastic_dal import ElasticSearchDAL
from mongo_dal import MongodbDAL
from kafka_pub import Publisher
from transcriber import Transcriber
import os
from logger_dir.logger import Logger

logger = Logger.get_logger()

class TranscriberManager:
    def __init__(self, file_id):
        self.file_id = file_id
        self.elastic = ElasticSearchDAL()
        self.mongo = MongodbDAL()
        self.kafka_pub = Publisher()
        self.temp_file_path = 'C:\\Users\\HOME\\PycharmProjects\\24\\The muezzin\\transcription_of_files\\temp.wav'
        self.text = None

    def main_func(self):
        self.delete_file()
        self.get_file_according_id()
        self.send_to_transcription()
        self.sand_text_to_elastic()
        self.sending_for_classification()


    def get_file_according_id(self):
        self.mongo.load_file_from_mongodb(self.file_id, self.temp_file_path)

    def send_to_transcription(self):
        transcriber = Transcriber(self.temp_file_path)
        text = transcriber.transcription_of_file()
        self.text = {'text': text, 'words count': len(text.split())}

    def delete_file(self):
        try:
            os.remove(self.temp_file_path)
            logger.info(" temp file deleted successfully")
        except FileNotFoundError:
            logger.error("temp file not found")

    def sand_text_to_elastic(self):
        self.elastic.update_file(self.text, self.file_id)

    def sending_for_classification(self):
        self.kafka_pub.pub_data_for_classification (self.file_id)




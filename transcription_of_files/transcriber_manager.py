from elastic_dal import ElasticSearchDAL
from mongo_dal import MongodbDAL
from transcriber import Transcriber
import os

class TranscriberManager:
    def __init__(self, file_id):
        self.file_id = file_id
        self.elastic = ElasticSearchDAL()
        self.mongo = MongodbDAL()
        self.temp_file_path = 'C:\\Users\\HOME\\PycharmProjects\\24\\The muezzin\\transcription_of_files\\temp.wav'
        self.text = None

    def main_func(self):
        self.get_file_according_id()
        self.send_to_transcription()
        self.delete_file()
        self.sand_text_to_elastic()


    def get_file_according_id(self):
        self.mongo.load_file_from_mongodb(self.file_id, self.temp_file_path)

    def send_to_transcription(self):
        transcriber = Transcriber(self.temp_file_path)
        text = transcriber.transcription_of_file()
        self.text = {'text': text}

    def delete_file(self):
        file_to_delete = self.temp_file_path
        os.remove(file_to_delete)

    def sand_text_to_elastic(self):
        self.elastic.update_file(self.text, self.file_id)




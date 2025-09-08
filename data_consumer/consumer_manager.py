from data_consumer.create_id.creates_unique_id import IDCreator
from data_storer.elastic_dal import ElasticSearchDAL
from data_storer.mongodb_dal import MongodbDAL

class ConsumerManager:
    def __init__(self, file):
        self.file = file
        self.id_creator = IDCreator
        self.save_to_elastic = ElasticSearchDAL()
        self.save_to_mongo = MongodbDAL()
        self.unique_id = None

    def main_func(self):
        self.get_id()
        self.metadata_saving()
        self.data_saving()

    def get_id(self):
        data_for_id = self.file['Permanent details']
        self.unique_id = self.id_creator.generate_id(data_for_id)

    def metadata_saving(self):
        self.save_to_elastic.save_file_to_elastic(self.file, self.unique_id)

    def data_saving(self):
        path = self.file['Path']['full path']
        file_name = self.file['Permanent details']['file name']
        self.save_to_mongo.save_file_to_mongodb(path, file_name, self.unique_id)




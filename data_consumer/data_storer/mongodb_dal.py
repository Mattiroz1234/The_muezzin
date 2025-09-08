from pymongo import MongoClient
import gridfs
import os
from dotenv import load_dotenv

load_dotenv()

class MongodbDAL:
    def __init__(self):
        self.mongodb_url = os.getenv('MONGODB_URL')
        self.client = MongoClient(self.mongodb_url)
        self.db = self.client['test_db']

    def save_file_to_mongodb(self, path, file_name, unique_id):
        fs = gridfs.GridFS(self.db)

        file_path = path

        with open(file_path, 'rb') as file_data:
            file_id = fs.put(file_data, filename=file_name, description='Sample audio file', id=unique_id)

        print(f"File uploaded with file_id: {file_id}")

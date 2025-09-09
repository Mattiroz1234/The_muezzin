from pymongo import MongoClient, errors
import gridfs
import os
from dotenv import load_dotenv
from logger_dir.logger import Logger

logger = Logger.get_logger()

load_dotenv()

class MongodbDAL:
    def __init__(self):
        self.mongodb_url = os.getenv('MONGODB_URL')
        self.client = MongoClient(self.mongodb_url)
        self.db = self.client[os.getenv('MONGODB_DB_NAME')]

    def load_file_from_mongodb(self, id, temp_file_path):
        fs = gridfs.GridFS(self.db)

        file_data = fs.find_one({'id': id})

        try:
            with open(temp_file_path, 'wb') as output_file:
                output_file.write(file_data.read())
            logger.info(f"File: {id} downloaded from mongodb successfully")
        except:
            logger.error("File not found")

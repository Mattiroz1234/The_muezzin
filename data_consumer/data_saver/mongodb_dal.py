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

    def save_file_to_mongodb(self, path, file_name, unique_id):
        fs = gridfs.GridFS(self.db)

        try:
            with open(path, 'rb') as file_data:
                file_id = fs.put(file_data, filename=file_name, description='Sample audio file', id=unique_id)

            logger.info(f"File uploaded to mongodb with file_id: {file_id}")
        except errors.WriteError as error:
            logger.error(f"error: {error} - writing to mongo failed")

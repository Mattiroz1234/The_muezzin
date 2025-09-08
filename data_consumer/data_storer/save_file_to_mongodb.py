from pymongo import MongoClient
import gridfs


client = MongoClient("mongodb://localhost:27017/")

db = client['test_db']


fs = gridfs.GridFS(db)


file_path = 'download.wav'

with open(file_path, 'rb') as file_data:
    file_id = fs.put(file_data, filename='download.wav', description='Sample audio file')

print(f"File uploaded with file_id: {file_id}")
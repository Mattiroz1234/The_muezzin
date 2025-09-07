from datetime import datetime
import os

class MetadataCreator:
    def __init__(self, path):
        self.path = path


    def create_metadata(self):
        stats = os.stat(self.path)

        attrs = {
            'Full Path' : self.path,
            'File Name': os.path.basename(str(self.path)),
            'Size (KB)': self.size_format(stats.st_size),
            'Creation Date': self.time_convert(stats.st_ctime),
            'Modified Date': self.time_convert(stats.st_mtime),
            'Last Access Date': self.time_convert(stats.st_atime),
        }

        return attrs


    @staticmethod
    def time_convert(time_stamp):
        new_time = datetime.fromtimestamp(time_stamp)
        return new_time

    @staticmethod
    def size_format(size):
        new_form = format(size / 1024, ".2f")
        return new_form + " KB"

a = MetadataCreator(r'C:\Users\HOME\inimical_podcasts\download.wav')
print(a.create_metadata())
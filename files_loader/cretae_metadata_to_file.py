from datetime import datetime
import os

class MetadataCreator:

    def create_metadata(self, path):
        stats = os.stat(path)

        attrs = {
            'Path': {
                'full path': str(path)
            },
            'Permanent details': {
                'file name': os.path.basename(str(path)),
                'size (KB)': self.size_format(stats.st_size),
                'Creation Date': str(self.time_convert(stats.st_ctime)),
            },
            'Temporary details': {
                'Modified Date': str(self.time_convert(stats.st_mtime)),
                'Last Access Date': str(self.time_convert(stats.st_atime))
            }
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


import os
import zipfile

class FilesLoader:
    def __init__(self):
        self.input_folder = r"C:\Users\HOME\inimical_podcasts.zip"

    def load_files(self):
        with zipfile.ZipFile(self.input_folder) as z:
            for filename in z.namelist():
                filepath = os.path.join(self.input_folder, filename)
                if not os.path.isdir(filename):
                    if filename.lower().endswith(".wav"):
                        print(filepath)
                else:
                    for filename2 in os.listdir(filepath):
                        if filename2.lower().endswith(".wav"):
                            filepath = os.path.join(self.input_folder, filename2)
                            print(filepath)


a = FilesLoader()
a.load_files()






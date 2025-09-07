from pathlib import Path

class FilesLoader:
    def __init__(self):
        self.input_folder = Path(r"C:\Users\HOME\inimical_podcasts")

    def load_files(self):
        files = self.input_folder.rglob('*.wav')
        for f in files:
            print(f)


a = FilesLoader()
a.load_files()






from pathlib import Path

class FilesLoader:
    def __init__(self):
        self.input_folder = Path(r"C:\Users\HOME\inimical_podcasts")
        self.files_list = []

    def load_files(self):
        files = self.input_folder.rglob('*.wav')
        for f in files:
            self.files_list.append(f)
        return self.files_list







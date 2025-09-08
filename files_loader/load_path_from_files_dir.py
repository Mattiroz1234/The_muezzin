import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

class FilesLoader:
    def __init__(self):
        self.folder_path = os.getenv('PATH_TO_FILES_FOLDER')
        self.input_folder = Path(self.folder_path)
        self.files_list = []

    def load_files(self):
        files = self.input_folder.rglob('*.wav')
        for file in files:
            self.files_list.append(file)
        return self.files_list







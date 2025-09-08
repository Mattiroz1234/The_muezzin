from creates_unique_id import IDCreator

class ConsumerManager:
    def __init__(self, file):
        self.file = file
        self.id_creator = IDCreator
        self.unique_id = None

    def main_func(self):
        self.get_id()
        self.data_saving()

    def get_id(self):
        data_for_id = self.file['Permanent details']
        self.unique_id = self.id_creator.generate_id(data_for_id)

    def data_saving(self):
        pass



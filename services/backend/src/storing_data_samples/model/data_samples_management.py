from .file_database import FileDataBase
from .data_sample import DataSample


class DataSampleManager:

    def __init__(self, file_database: FileDataBase, test_dir='test'):
        self.file_database = file_database
        self.test_dir = test_dir

        self.file_database.create_dir_if_not_exist(self.test_dir)

    def to_dict(self):
        return self.__dict__

    def get_all_names(self):
        return [data_sample.name for data_sample in self.get_all()]

    def get_all(self):
        return [DataSample(**data) for data in self.file_database.get_all_data()]

    def get_by_name(self, name):
        data = self.file_database.get_data_by_filename(name)
        if not data:
            return None
        return DataSample(**data)

    def get_data_sample_by_data(self, data):
        return DataSample.create_now(*data)

    def save(self, data_sample: DataSample):
        self.file_database.save_data_by_filename(data_sample.to_dict(), data_sample.name)

    def delete_all(self):
        filenames = self.file_database.get_filenames()
        for filename in filenames:
            self.file_database.delete_data_by_filename(filename)

    def delete_by_name(self, name):
        self.file_database.delete_data_by_filename(name)

    def test_data_load(self):
        self.file_database.move_files(self.test_dir)

    def add_to_test_data_by_name(self, name):
        file_path = self.file_database.get_file_path_by_filename(name)
        self.file_database.move_file(file_path, self.test_dir)

    def delete_from_test_data_by_name(self, name):
        self.file_database.delete_data_by_filename(f"{self.test_dir}/{name}")


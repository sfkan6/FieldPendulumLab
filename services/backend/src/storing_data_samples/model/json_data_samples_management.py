from .data_samples_management import DataSampleManager
from .file_database import JsonDataBase


class JsonDataSampleManager(DataSampleManager):

    @classmethod
    def create_by_path(cls, path):
        return cls(JsonDataBase(path))

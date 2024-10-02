from .file_operator import FileOperator
from .file_database import FileDataBase
import json


class JsonFileOperator(FileOperator):

    def __init__(self) -> None:
        super().__init__('.json')

    def get_data_by_file_path(self, file_path):
        with open(file_path, 'r') as json_file:
            return json.load(json_file)

    def write_data_by_file_path(self, data, file_path):
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)


class JsonDataBase(FileDataBase):

    def __init__(self, path):
        super().__init__(path, JsonFileOperator())


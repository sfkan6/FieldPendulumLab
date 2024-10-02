import os, shutil
from .file_operator import FileOperator


class FileDataBase:

    def __init__(self, path, file_operator: FileOperator):
        self.path = path
        self.file_operator = file_operator
        
        self.create_dir_if_not_exist('')

    def move_files(self, dir_name):
        path_to_dir = os.path.join(self.path, dir_name)
        for filename in os.listdir(path_to_dir):
            self.move_file(os.path.join(path_to_dir, filename), self.path)

    def move_file(self, file_path, target_dir):
        shutil.copy(file_path, target_dir)

    def get_all_data(self) -> list:
        return [
            self.file_operator.get_data_by_file_path(file_path) 
            for file_path in self.get_all_file_paths()
        ]
 
    def get_all_file_paths(self):
        return [
            self.get_file_path_by_filename(filename)
            for filename in os.listdir(self.path) if self.file_operator.is_file_extension_suitable(filename)
        ]

    def get_filenames(self):
        return [
            filename for filename in os.listdir(self.path) 
            if self.file_operator.is_file_extension_suitable(filename)
        ]

    def get_data_by_filename(self, filename):
        file_path = self.get_file_path_by_filename(filename)
        if os.path.exists(file_path):
            return self.file_operator.get_data_by_file_path(file_path)
        return None

    def save_data_by_filename(self, data, filename):
        file_path = self.get_file_path_by_filename(filename)
        return self.file_operator.write_data_by_file_path(data, file_path)

    def delete_data_by_filename(self, filename):
        file_path = self.get_file_path_by_filename(filename)
        if os.path.exists(file_path):
            return self.file_operator.delete_file_by_file_path(file_path)
        return None

    def get_file_path_by_filename(self, filename):
        full_file_name = self.file_operator.get_full_filename(filename)
        return os.path.join(self.path, full_file_name)

    def create_dir_if_not_exist(self, dir_name):
        dir_path = os.path.join(self.path, dir_name)
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)



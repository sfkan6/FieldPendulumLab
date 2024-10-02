import os


class FileOperator:

    def __init__(self, file_extension) -> None:
        if file_extension[0] != '.':
            file_extension = '.' + file_extension
        self.file_extension = file_extension

    def get_data_by_file_path(self, file_path):
        pass

    def write_data_by_file_path(self, data, file_path):
        pass

    def delete_file_by_file_path(self, file_path):
        if os.path.isfile(file_path):
            os.remove(file_path)
 
    def get_full_filename(self, filename):
        if self.is_file_extension_suitable(filename):
            return filename
        return filename + self.file_extension

    def is_file_extension_suitable(self, filename):
        if filename.endswith(self.file_extension):
            return True
        return False




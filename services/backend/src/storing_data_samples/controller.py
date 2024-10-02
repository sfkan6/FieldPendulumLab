from fastapi import APIRouter, Body, status, HTTPException, Request
from fastapi.responses import FileResponse

from .model import DataSample, DataSampleManager


class Controller:

    def __init__(self, data_type: str, sample_manager: DataSampleManager):
        self.data_type = data_type
        self.sample_manager = sample_manager

        self.router = APIRouter()

        self.router.add_api_route(f"/{self.data_type}", self.get_all, methods=["GET"])
        self.router.add_api_route(f"/{self.data_type}", self.delete_all, methods=["DELETE"])
        self.router.add_api_route(f"/{self.data_type}/names", self.get_all_names, methods=["GET"])

        self.router.add_api_route(f"/{self.data_type}/test_data/load", self.test_data_load, methods=["PUT"])
        self.router.add_api_route(f"/{self.data_type}/test_data/{{name}}", self.test_data_add, methods=["POST"])
        self.router.add_api_route(f"/{self.data_type}/test_data/{{name}}", self.test_data_delete, methods=["DELETE"])

        self.router.add_api_route(f"/file/{self.data_type}/{{name}}", self.get_file, methods=["GET"])

        self.router.add_api_route(f"/{self.data_type}/{{name}}", self.get, methods=["GET"])
        self.router.add_api_route(f"/{self.data_type}/create", self.create, methods=["POST"], status_code=200)
        self.router.add_api_route(f"/{self.data_type}/{{name}}", self.update, methods=["PUT"])
        self.router.add_api_route(f"/{self.data_type}/{{name}}", self.delete, methods=["DELETE"])
       
    def set_handler(self, path, handler, **kwargs):
        self.router.add_api_route(path, handler, **kwargs)

    def get_all(self): 
        data_samples = self.sample_manager.get_all()
        data_samples = sorted(data_samples, key=lambda data_sample: data_sample.timestamp)[::-1]
        return data_samples

    def delete_all(self):
        self.sample_manager.delete_all()

    def get_all_names(self): 
        return self.sample_manager.get_all_names()

    def get_file(self, name):
        file_path = self.sample_manager.file_database.get_file_path_by_filename(name)
        return FileResponse(file_path)

    def test_data_load(self):
        self.sample_manager.test_data_load()

    def test_data_add(self, name):
        if not name:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='No data received',
            )
        self.sample_manager.add_to_test_data_by_name(name)

    def test_data_delete(self, name):
        if not name:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='No data received',
            )
        self.sample_manager.delete_from_test_data_by_name(name)

    def get(self, name):
        return self.sample_manager.get_by_name(name)

    async def create(self, body = Body()):
        records = body.get('records', None)
        if not records:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='No data received',
            )

        name = body.get('name', DataSample.get_random_name())
        description = body.get('description', '')
        data_sample = DataSample.create_now(name, description, records)
        self.sample_manager.save(data_sample)
        return data_sample.__dict__

    async def update(self, name, request: Request):
        body = await request.json()
        timestamp = body.get('timestamp', None)
        records = body.get('records', None)

        if not(name and timestamp and records):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='No data received',
            )

        description = body.get('description', '')
        new_name = body.get('name', None)
        data_sample = DataSample(name, timestamp, description, records)

        if new_name != name:
            self.sample_manager.delete_by_name(name)
            data_sample.name = new_name

        self.sample_manager.save(data_sample)
        return data_sample.__dict__

    def delete(self, name):
        self.sample_manager.delete_by_name(name)


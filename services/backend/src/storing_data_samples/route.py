from fastapi import APIRouter
from .model import JsonDataSampleManager
from .controller import Controller


router = APIRouter(prefix="/data_samples")

storage_dir = 'sample_storage'
data_types = ['angle', 'amplitude', 'amplitude_frequency', 'frequency_phase_shift']


for data_type in data_types:
    data_manager = JsonDataSampleManager.create_by_path(f'{storage_dir}/{data_type}')
    controller = Controller(data_type, data_manager)
    router.include_router(controller.router)


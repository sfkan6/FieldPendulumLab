from .cv2_detection import Camera, Thresher

from .data_generation import RandomNumberGenerator, DataGenerator
from .angle_recognition import AngleRecognizer, FieldPendulumAngleRecognizer
from .angle_record import AngleRecord
from typing import AsyncGenerator
import time, asyncio


class RandomAngleGenerator(RandomNumberGenerator):

    async def generator(self, sleep_time=1, *args, **kwargs) -> AsyncGenerator[object, None]:
        start_time = time.time()

        async for angle in super().generator(sleep_time):
            angle_record = AngleRecord.create_now_relative_to_start_time(angle, start_time)
            yield angle_record.to_json()


class AngularDataGenerator(DataGenerator):
    
    def __init__(self, angle_recognizer: AngleRecognizer, camera: Camera) -> None:
        self.angle_recognizer = angle_recognizer
        self.camera = camera
    
    async def generator(self, sleep_time=1, *args, **kwargs) -> AsyncGenerator[object, None]:
        start_time = time.time()

        while True:
            image = self.camera.get_image()
            angle = self.angle_recognizer.get_angle_by_image(image)
            if not angle:
                continue
            angle_record = AngleRecord.create_now_relative_to_start_time(angle, start_time)
            yield angle_record.to_json()
            await asyncio.sleep(sleep_time)


class FieldPendulumAngleGenerator(AngularDataGenerator):
    def __init__(self, center_point_thresher: Thresher, corner_point_thresher: Thresher, camera: Camera) -> None:
        super().__init__(FieldPendulumAngleRecognizer(center_point_thresher, corner_point_thresher), camera)




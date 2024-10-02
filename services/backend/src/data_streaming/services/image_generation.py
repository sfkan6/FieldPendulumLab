from .cv2_detection import Camera, Thresher
from .cv2_detection.object_detection import MultipleIndicator

from .data_generation import DataGenerator
from .angle_point_detection import CenterPointIndicator, CornerPointIndicator
from typing import AsyncGenerator
import asyncio



class ImageGenerator(DataGenerator):
 
    def __init__(self, multiple_indicator: MultipleIndicator, camera: Camera):
        self.multiple_indicator = multiple_indicator
        self.camera = camera
    
    async def generator(self, sleep_time=0.05, *args, **kwargs) -> AsyncGenerator[object, None]:
        while self.camera.is_connected:
            image = self.camera.get_image()
            image = self.multiple_indicator.display(image)
            yield image.get_base64()
            await asyncio.sleep(sleep_time)


class FieldPendulumImageGenerator(ImageGenerator):
    
    def __init__(self, center_point_thresher: Thresher, corner_point_thresher: Thresher, camera: Camera):
        indicators = [
            CenterPointIndicator(center_point_thresher),
            CornerPointIndicator(corner_point_thresher),
        ]
        super().__init__(MultipleIndicator(indicators), camera)

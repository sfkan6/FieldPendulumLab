from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Request, Body, HTTPException, status
from websockets.exceptions import ConnectionClosed
from .services.cv2_detection import HSVThresher, Image, CV2Image, CV2HSVThresher
from .services import DataGenerator


class StreamingController:

    def __init__(self, path: str, data_generator: DataGenerator) -> None:
        self.path = path
        self.data_generator = data_generator

        self.router = APIRouter()
        self.router.add_api_websocket_route(f"/{self.path}", self.streaming)
 
    async def streaming(self, websocket: WebSocket):
        await websocket.accept()
        config = await websocket.receive_json()

        try:
            async_generator = self.data_generator.generator(**config)
            async for value in async_generator:
                await websocket.send_text(value)
        except (WebSocketDisconnect, ConnectionClosed):
            return
 

class HSVThresherController:
 
    def __init__(self, path: str, thresher_instance: HSVThresher) -> None:
        self.path = path
        self.thresher_instance = thresher_instance

        self.router = APIRouter()
        self.router.add_api_route(f"/{self.path}/hsv_ranges", self.get_hsv_ranges, methods=["GET"])
        self.router.add_api_route(f"/{self.path}/hsv_ranges", self.set_hsv_ranges, methods=["PUT"])

        self.router.add_api_route(f"/{self.path}/options", self.get_options, methods=["GET"])
        self.router.add_api_route(f"/{self.path}/options", self.set_options, methods=["PUT"])
    
    def get_hsv_ranges(self):
        return self.thresher_instance.hsv_ranges

    def get_options(self):
        options = {**self.thresher_instance.__dict__}
        del options['_hsv_ranges']
        return options

    def set_hsv_ranges(self, body=Body()) -> None:
        try:
            hsv_ranges = body.get('hsv_ranges', [])
            self.thresher_instance.set_hsv_ranges(hsv_ranges)
        except:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail='Unprocessable data',
            )

    def set_options(self, body=Body()) -> None:
        try:
            options = body.get('options', {})
            self.thresher_instance.__init__(self.thresher_instance.hsv_ranges, **options)
        except:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail='Unprocessable data',
            )




class ImageHSVThreshingController:
   
    def __init__(self, path: str, prototype_thresher: HSVThresher, prototype_image: Image, thresher_options: dict):
        self.path = path
        self.prototype_thresher = prototype_thresher
        self.prototype_image = prototype_image
        self.thresher_options = thresher_options

        self.router = APIRouter()
        self.router.add_api_route(f"/{self.path}/threshold", self.get_threshold_image, methods=["POST"])
        self.router.add_api_route(f"/{self.path}/finished", self.get_finished_image, methods=["POST"])
  
    async def get_threshold_image(self, body = Body()):
        return await self._try_wrapper(self.prototype_thresher.get_threshold_image, body)

    async def get_finished_image(self, body = Body()):
        return await self._try_wrapper(self.prototype_thresher.get_finished_image, body)
    
    async def _try_wrapper(self, function, body):
        try:
            self._update_thresher(body)
            image = self._get_image(body)
            threshold_image = function(image)
            base64_image = threshold_image.get_base64()
        except:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail='Unprocessable data',
            )
        return base64_image

    def _update_thresher(self, body: dict):
        hsv_ranges = body.get('hsv_ranges', [])
        options = body.get('options', self.thresher_options)
        self.prototype_thresher.__init__(hsv_ranges, **options)

    def _get_image(self, body: dict) -> Image:
        base64_image = body.get('base64_image', "")
        return self.prototype_image.create_by_base64(base64_image)


class CV2ImageHSVThreshingController(ImageHSVThreshingController):
    
    def __init__(self, path: str):
        thresher_options = {'open_iters': 3, 'dilate_iters': 4, 'close_iters': 3}
        super().__init__(path, CV2HSVThresher([]), CV2Image([]), thresher_options)

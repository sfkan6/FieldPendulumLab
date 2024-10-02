from fastapi import APIRouter
from .services import FieldPendulumImageGenerator, FieldPendulumAngleGenerator, RandomAngleGenerator
from .controller import StreamingController, HSVThresherController, CV2ImageHSVThreshingController
from .config import center_point_thresher, corner_point_thresher, camera


router = APIRouter(prefix="/stream")

routes = [
    StreamingController('pendulum_of_field/image', FieldPendulumImageGenerator(center_point_thresher, corner_point_thresher, camera)),
    StreamingController('pendulum_of_field/angle', FieldPendulumAngleGenerator(center_point_thresher, corner_point_thresher, camera)),
    StreamingController('pendulum_of_field/random_angle', RandomAngleGenerator(180, -180)),

    HSVThresherController('center_point_thresher', center_point_thresher),
    HSVThresherController('corner_point_thresher', corner_point_thresher),

    CV2ImageHSVThreshingController('threshing_test'),
]

for route in routes:
    router.include_router(route.router)


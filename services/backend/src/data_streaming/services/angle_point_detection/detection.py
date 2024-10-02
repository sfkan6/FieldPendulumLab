from ..cv2_detection.object_detection import Detector, Thresher
from .contour_processing import CenterPointProcessor, CornerPointProcessor
from .point_detection import PointDetector


class CenterPointDetector(PointDetector):

    def __init__(self, thresher: Thresher):
        super().__init__(Detector(thresher, CenterPointProcessor()))


class CornerPointDetector(PointDetector):

    def __init__(self, thresher: Thresher):
        super().__init__(Detector(thresher, CornerPointProcessor()))

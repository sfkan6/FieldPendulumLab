from ..cv2_detection.object_detection import Detector, Thresher, Indicator
from ..cv2_detection import CV2PointPainter, CV2RectanglePainter
from .contour_processing import CenterPointProcessor, CornerPointProcessor


class CenterPointIndicator(Indicator):

    def __init__(self, thresher: Thresher, color=[70, 0, 255], thickness=3):
        detector = Detector(thresher, CenterPointProcessor())
        super().__init__(detector, CV2RectanglePainter(color=color, thickness=thickness))


class CornerPointIndicator(Indicator):
    
    def __init__(self, thresher: Thresher, color=[255, 63, 63], thickness=3):
        detector = Detector(thresher, CornerPointProcessor())
        super().__init__(detector, CV2RectanglePainter(color=color, thickness=thickness))


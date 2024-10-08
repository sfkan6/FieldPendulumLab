from cv2_detection.object_detection import Detector, Thresher, Image, Contour
from .contour_processing import CenterPointProcessor, CornerPointProcessor
from .point import Point


class PointDetector:

    def __init__(self, detector: Detector):
        self.detector = detector

    def get_point_by_image(self, image: Image) -> Point|None:
        contours = self.detector.get_contours_by_image(image)
        if len(contours) > 0:
            return self.get_point_by_contour(contours[0])
        return None

    def get_point_by_contour(self, contour: Contour) -> Point:
        x, y, w, h = contour.bounding_rect
        return Point(x + w // 2, y + h // 2)


class CenterPointDetector(PointDetector):

    def __init__(self, thresher: Thresher):
        super().__init__(Detector(thresher, CenterPointProcessor()))


class CornerPointDetector(PointDetector):

    def __init__(self, thresher: Thresher):
        super().__init__(Detector(thresher, CornerPointProcessor()))

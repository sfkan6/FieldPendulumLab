from ..angle_point_detection import Image, Thresher, CenterPointDetector, CornerPointDetector
from .angle_metering import VerticalAngleMeter, AngleToStraightLineMeter
from abc import abstractmethod


class AngleRecognizer:

    @abstractmethod
    def get_angle_by_image(self, image: Image) -> float|None:
        pass


class AngleToStraightLineRecognizer(AngleRecognizer):

    def __init__(self, 
        center_point_detector: CenterPointDetector, 
        corner_point_detector: CornerPointDetector, 
        angle_meter: AngleToStraightLineMeter
    ) -> None:
        self.center_point_detector = center_point_detector
        self.corner_point_detector = corner_point_detector
        self.angle_meter = angle_meter
    
    def get_angle_by_image(self, image: Image) -> float | None:
        center_point = self.center_point_detector.get_point_by_image(image)
        corner_point = self.corner_point_detector.get_point_by_image(image)
        if center_point and corner_point:
            angle = self.angle_meter.get_angle_by_points(center_point, corner_point)
            return self.angle_meter.get_angle_in_degrees(angle)
        return None


class VerticalAngleRecognizer(AngleToStraightLineRecognizer):
    def __init__(self, center_point_detector: CenterPointDetector, corner_point_detector: CornerPointDetector) -> None:
        super().__init__(center_point_detector, corner_point_detector, VerticalAngleMeter())


class FieldPendulumAngleRecognizer(VerticalAngleRecognizer):
    def __init__(self, center_point_thresher: Thresher, corner_point_thresher: Thresher):
        super().__init__(CenterPointDetector(center_point_thresher), CornerPointDetector(corner_point_thresher))


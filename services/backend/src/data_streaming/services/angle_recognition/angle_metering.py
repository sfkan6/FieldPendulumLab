from ..angle_point_detection import Point
from abc import abstractmethod
import math


class AngleToStraightLineMeter:

    @abstractmethod
    def get_angle_by_points(self, center_point: Point, corner_point: Point) -> float:
        pass 

    def get_angle_in_degrees(self, angle: int|float, n=2) -> int|float:
        angle_in_degrees = (180 / math.pi) * angle
        return round(angle_in_degrees, n)


class VerticalAngleMeter(AngleToStraightLineMeter):
   
    def get_angle_by_points(self, center_point: Point, corner_point: Point) -> float:
        if center_point.x == corner_point.x:
            return 0

        angle = math.atan(self.get_tan_by_point(center_point, corner_point))

        if corner_point.y < center_point.y:
            angle = -(math.pi / 2 - angle) if angle > 0 else angle + math.pi / 2
        else:
            angle = math.pi / 2 + angle if angle > 0 else -(math.pi / 2 - angle)
        return angle
    
    def get_tan_by_point(self, center_point: Point, corner_point: Point) -> int|float:
        return (center_point.y - corner_point.y) / (center_point.x - corner_point.x)




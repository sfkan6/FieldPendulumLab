from __future__ import annotations
from abc import abstractmethod


class Contour:
    def __init__(self, _contour) -> None:
        self._contour = _contour

    @property
    @abstractmethod
    def area(self) -> int|float:
        pass

    @property
    @abstractmethod
    def bounding_rect(self) -> list[int|float]:
        pass


class Image:
    def __init__(self, _image) -> None:
        self._image = _image

    @property
    @abstractmethod
    def height(self) -> int:
        pass

    @property
    @abstractmethod
    def width(self) -> int:
        pass

    @property
    @abstractmethod
    def shape(self) -> list:
        pass

    @abstractmethod
    def get_base64(self) -> str:
        pass

    @abstractmethod
    def copy(self) -> Image:
        return Image([])

    @abstractmethod
    def write(self, path: str) -> None:
        pass

    @classmethod
    @abstractmethod
    def read(cls, path: str) -> Image:
        pass
 
    @classmethod
    @abstractmethod
    def create_by_base64(cls, base64_image: str) -> Image:
        pass



class Camera:

    @property
    @abstractmethod
    def is_connected(self) -> bool:
        pass

    @abstractmethod
    def get_image(self) -> Image:
        pass

from typing import AsyncGenerator
from abc import abstractmethod
import asyncio, random


class DataGenerator:
    
    @abstractmethod
    async def generator(self, *args, **kwargs) -> AsyncGenerator[object, None]:
        for i in range(1):
            yield i


class RandomNumberGenerator(DataGenerator):

    def __init__(self, start: int|float, stop: int|float, n: int=0) -> None:
        self.shift = self._get_shift(start, stop, n)
        self.shifted_start = int(start * self.shift)
        self.shifted_stop = int(stop * self.shift)

    def _get_shift(self, start, stop, n) -> int:
        return 10**(max(self._get_n(start), self._get_n(stop)) + n)

    def _get_n(self, num: int|float) -> int:
        if int(num) == num:
            return 0
        return len(str(num)) - len(str(int(num))) - 1

    async def generator(self, sleep_time=1, *args, **kwargs) -> AsyncGenerator[object, None]:
        while True:
            yield random.randint(self.shifted_start, self.shifted_stop) / self.shift
            await asyncio.sleep(sleep_time)


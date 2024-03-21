from abc import ABC, abstractmethod


class SquareGenerator(ABC):
    def __init__(self, start, end):
        if end < start:
            raise ValueError("End of range must be greater than or equal to the start.")
        self.start = start
        self.end = end

    @abstractmethod
    def generate_squares(self):
        pass


class CubicGenerator(SquareGenerator):
    def generate_squares(self):
        if self.start > self.end:
            raise ValueError("Start of range must be less than or equal to the end.")
        squares = [x ** 2 for x in range(self.start, self.end + 1)]
        return squares

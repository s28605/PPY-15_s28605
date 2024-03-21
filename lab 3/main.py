# task 1
squared_list = [x ** 2 for x in range(1, 11)]


# task 2
def range_squares(start, end):
    return [x ** 2 for x in range(start, end + 1)]


# task 3
class SquareGenerator:
    def range_squares(self, start, end):
        return [x ** 2 for x in range(start, end + 1)]


# task 4
import math

square_roots = [math.sqrt(num) for num in squared_list]
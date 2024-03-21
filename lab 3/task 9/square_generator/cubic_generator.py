from square_generator import SquareGenerator

class CubicGenerator(SquareGenerator):
    def generate_squares(self, start, end):
        cubes = [x**3 for x in range(start, end + 1)]
        return cubes
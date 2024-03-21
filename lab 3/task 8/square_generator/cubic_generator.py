from square_generator import SquareGenerator

class CubicGenerator(SquareGenerator):
    def generate_squares(self):
        cubes = [x**3 for x in range(self.start, self.end + 1)]
        return cubes
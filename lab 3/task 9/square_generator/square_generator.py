class SquareGenerator:
    def range_squares(self, start, end):
        if end < start:
            raise ValueError("End of range must be greater than or equal to the start.")
        return [x ** 2 for x in range(start, end + 1)]
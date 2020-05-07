from src.Color import Color


class Canvas(object):

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pixels = []

        # Set each pixel to be black by default
        for row in range(self.height):
            pixel_rows = []
            for column in range(self.width):
                pixel_rows.append(Color(0, 0, 0))
            self.pixels.append(pixel_rows)

    def write_pixel(self, x, y, color):
        self.pixels[y][x] = color

    def pixel_at(self, x, y):
        return self.pixels[y][x]

    def _clamp_pixel_value(self, pixel_value):
        """Returns the pixel value as an integer within the range [0, 255]"""
        if pixel_value < 0.0:
            return 0
        elif pixel_value >= 1.0:
            return 255
        else:
            return int(pixel_value * 256)

    def _trim_pixel_line(self, pixel_line):
        """Takes in a string containing pixel color integer values separate by a space.
        Returns None if the string is already in valid range
        Returns an integer representing the index that represents an empty space at <= 70
        """
        if len(pixel_line) <= 70:
            return None
        for index in range(70, -1, -1):
            if pixel_line[index] == ' ':
                return index

    def to_ppm(self):
        header = f"""P3\n{self.width} {self.height}\n255"""
        file = [header]
        for row in range(self.height):
            pixel_values = []
            # Read a row that would be appended to the data section of the file
            for column in range(self.width):
                pixel_values.append(str(self._clamp_pixel_value(self.pixels[row][column].red)))
                pixel_values.append(str(self._clamp_pixel_value(self.pixels[row][column].green)))
                pixel_values.append(str(self._clamp_pixel_value(self.pixels[row][column].blue)))
            pixel_row = ' '.join(pixel_values)
            # If the length of the line is greater than 70, must truncate to follow specification
            index = self._trim_pixel_line(pixel_row)
            # Is already at the appropriate length
            if index is None:
                file.append(pixel_row)
            # Needs to split the row into two lines
            else:
                file.append(pixel_row[:index])
                file.append(pixel_row[index+1:])
        # New line must be present at the end of the file to follow specification
        file.append('\n')
        return '\n'.join(file)

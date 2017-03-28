from PIL import Image

# class which represent array of pixels from png file
class PixelsRGBArray:
    def __init__(self, png_file_name):
        img = Image.open(png_file_name)
        self.pixels_array = img.load()
        self.size = img.size

    def red(self, x, y):
        return self.pixels_array[x, y][0]

    def green(self, x, y):
        return self.pixels_array[x, y][1]

    def blue(self, x, y):
        return self.pixels_array[x, y][2]


z = PixelsRGBArray("brick-house.png")
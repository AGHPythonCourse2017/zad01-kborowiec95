from PIL import Image
from math import sqrt


# Class which represent array of pixels from png file :
class PixelsRGBArray:
    def __init__(self, png_file_name):
        image = Image.open(png_file_name)
        img = image.convert("RGB")
        self.converter = ConverterRGBToSpectrum()
        self.pixels_array = img.load()
        self.size = img.size

    def red(self, x, y):
        return self.pixels_array[x, y][0]

    def green(self, x, y):
        return self.pixels_array[x, y][1]

    def blue(self, x, y):
        return self.pixels_array[x, y][2]

    def spectrum_wavelength(self, x, y):
        return self.converter.get_wavelength(self.red(x, y), self.green(x, y), self.blue(x, y))


# Class which is able to convert rgb values to spectrum light wavelength value :
class ConverterRGBToSpectrum:
    def __init__(self):
        spectrum_file = 'spect.png'
        spec_image = Image.open(spectrum_file)
        spec_img = spec_image.convert("RGB")
        self.pixels = spec_img.load()
        spec_size = spec_img.size[0]
        wavelength = 380.0  # nm
        diff = 400.0 / spec_size
        self.map_wavelength_by_rgb = {}  # map : keys = (r,g,b) -> values = spectrum wavelength
        for i in range(spec_size):
            if self.map_wavelength_by_rgb.get(self.pixels[i, 25]) is None:
                self.map_wavelength_by_rgb[self.pixels[i, 25]] = wavelength
            wavelength += diff

    def get_wavelength(self, r, g, b):
        minimal_diff = 100000
        result = 0
        # Check which rgb codes are the most similar :
        for x in self.map_wavelength_by_rgb.keys():
            d = diff_rgb(x, (r, g, b))
            if d == 0:
                return self.map_wavelength_by_rgb[x]
            if d < minimal_diff:
                minimal_diff = d
                result = self.map_wavelength_by_rgb[x]
        return result


def diff_rgb(rgb1, rgb2):
    res = 0
    res += (rgb1[0] - rgb2[0]) ** 2
    res += (rgb1[1] - rgb2[1]) ** 2
    res += (rgb1[2] - rgb2[2]) ** 2
    return sqrt(res)

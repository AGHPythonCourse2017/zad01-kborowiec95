from PIL import Image
from miditime.miditime import MIDITime


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

    # sources : https://science-edu.larc.nasa.gov/EDDOCS/Wavelengths_for_Colors.html - algorithm
    #         : http://www.cs.utah.edu/~bes/papers/color/paper-node2.html - values
    def spectrum_wavelength(self, x, y):
        cyan_spec = 492
        magenta_spec = 515
        yellow_spec = 570
        blue_spec = 475
        green_spec = 510
        red_spec = 650
        white_spec = 550
        result = 0
        red = self.red(x, y)/255.0
        green = self.green(x, y)/255.0
        blue = self.blue(x, y)/255.0
        if red <= green and red <= blue:
            result += red * white_spec
            if green <= blue:
                result += (green - red) * cyan_spec
                result += (blue - green) * blue_spec
            else:
                result += (blue - red) * cyan_spec
                result += (green - blue) * green_spec
        elif green <= red and green <= blue:
            result += green * white_spec
            if red <= blue:
                result += (red - green) * magenta_spec
                result += (blue - red) * blue_spec
            else:
                result += (blue - green) * magenta_spec
                result += (red - blue) * red_spec
        else:
            result += blue * white_spec
            if green <= red:
                result += (green - blue) * yellow_spec
                result += (red - green) * blue_spec
            else:
                result += (red - blue) * yellow_spec
                result += (green - red) * green_spec
        return result

#a_list = []
#b_list = a_list[1:]
#a_list.extend([1, 2, 3])
#print(a_list, id(a_list))
#print(b_list, id(b_list))

# Instantiate the class with a tempo (120bpm is the default) and an output file destination.
# mymidi = MIDITime(120, 'myfile.mid')

# Create a list of notes. Each note is a list: [time, pitch, velocity, duration]
# midinotes = [
#    [0, 60, 127, 3],  #At 0 beats (the start), Middle C with velocity 127, for 3 beats
#    [10, 61, 127, 4]  #At 10 beats (12 seconds from start), C#5 with velocity 127, for 4 beats
# ]

# Add a track with those notes
# mymidi.add_track(midinotes)

# Output the .mid file
# mymidi.save_midi()



z = PixelsRGBArray("brick-house.png")

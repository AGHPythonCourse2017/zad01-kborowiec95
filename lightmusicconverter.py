from random import randint


# 380nm .. 780nm -> 0 .. 255
# converts light wavelength values to 0 - 255 which will represent midi pitch values
def from_light_to_sound_wave(light_wave_length):
    return (255.0 * light_wave_length - 380.0 * 255.0) / 400.0


# scans pixels array vertically and returns midi notes:
def get_midi_notes_by_vertical_scan(pixels_array, precision):
    r = int(precision)
    result = []
    size_x = pixels_array.size[0]
    size_y = pixels_array.size[1]
    for y in range(0, size_y, r):
        # print(y / size_y)
        avg_wavelength = sum([pixels_array.spectrum_wavelength(x, y) for x in range(0, size_x, r)]) / (size_x / r)
        pitch = from_light_to_sound_wave(avg_wavelength)
        velocity = randint(100, 255)
        len = randint(50, 127)
        result.append([y, int(pitch), int(velocity), len])
    return result


# scans pixels array horizontally and returns midi notes:
def get_midi_notes_by_horizontal_scan(pixels_array, precision):
    r = int(precision)
    result = []
    size_x = pixels_array.size[0]
    size_y = pixels_array.size[1]
    for x in range(0, size_x, r):
        # print(x / size_x)
        avg_wavelength = sum([pixels_array.spectrum_wavelength(x, y) for y in range(0, size_y, r)]) / (size_y / r)
        pitch = from_light_to_sound_wave(avg_wavelength)
        velocity = randint(100, 255)
        len = randint(50, 127)
        result.append([x, int(pitch), int(velocity), len])
    return result

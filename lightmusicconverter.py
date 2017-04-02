from random import randint


# 380nm .. 780nm -> 0 .. 127
# Converts light wavelength values to 0 - 127 which will represent midi pitch values :
def from_light_to_sound_wave(light_wave_length):
    return (light_wave_length - 380.0) * 127.0 / 400.0


# Scans pixels array vertically and returns midi notes :
def get_midi_notes_by_vertical_scan(pixels_array, precision):
    r = int(precision)
    result = []
    size_x = pixels_array.size[0]
    size_y = pixels_array.size[1]
    for y in range(0, size_y, r):
        print(str(float(100.0 * y / size_y)) + '%')
        avg_wavelength = sum([pixels_array.spectrum_wavelength(x, y) for x in range(0, size_x, r)]) / (size_x / r)
        pitch = from_light_to_sound_wave(avg_wavelength)
        result.append([int(y / r), int(pitch), randint(225, 255), 1])
    return result


# Scans pixels array horizontally and returns midi notes :
def get_midi_notes_by_horizontal_scan(pixels_array, precision):
    r = int(precision)
    result = []
    size_x = pixels_array.size[0]
    size_y = pixels_array.size[1]
    for x in range(0, size_x, r):
        print(str(float(100.0 * x / size_x)) + '%')
        avg_wavelength = sum([pixels_array.spectrum_wavelength(x, y) for y in range(0, size_y, r)]) / (size_y / r)
        pitch = from_light_to_sound_wave(avg_wavelength)
        result.append([int(x / r), int(pitch), randint(225, 255), 1])
    return result

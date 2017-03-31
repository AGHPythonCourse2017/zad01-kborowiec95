from pixels_array import PixelsRGBArray

# 380nm .. 780nm -> 0 .. 127
# converts light wavelength values to 0 - 127 which represent midi pitch values
def from_light_to_sound_wave(lightwave_lenght):


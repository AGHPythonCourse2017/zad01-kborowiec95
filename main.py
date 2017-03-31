from pixels_array import PixelsRGBArray
from light_to_music_converter import get_midi_notes_by_horizontal_scan
from midi_track import MidiTrack

# Create a list of notes. Each note is a list: [time, pitch, velocity, duration]
# [
#    [0, 60, 127, 3],  #At 0 beats (the start), Middle C with velocity 127, for 3 beats
#    [100, 61, 127, 4]  #At 10 beats (12 seconds from start), C#5 with velocity 127, for 4 beats
# ]

pixels = PixelsRGBArray("spect.png")
midi_notes = get_midi_notes_by_horizontal_scan(pixels, 2)
track = MidiTrack('fll.mid', midi_notes, 200)
track.save_to_file()

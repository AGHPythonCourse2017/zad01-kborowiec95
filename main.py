from pixels_array import PixelsRGBArray
from random import randint
from midi_track import MidiTrack
from miditime.miditime import MIDITime
from light_to_music_converter import f

from PIL import Image


# Create a list of notes. Each note is a list: [time, pitch, velocity, duration]
#[
#    [0, 60, 127, 3],  #At 0 beats (the start), Middle C with velocity 127, for 3 beats
#    [100, 61, 127, 4]  #At 10 beats (12 seconds from start), C#5 with velocity 127, for 4 beats
#]

pixels = PixelsRGBArray("brick-house.png")

#midi_notes = []
#for i in range(100):
#    midi_notes.append([i, randint(0, 127), randint(0, 127), 1])

#x = MidiTrack('myfile.mid', midi_notes)
#x.save_to_file()

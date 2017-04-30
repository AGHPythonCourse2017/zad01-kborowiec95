import pip
import lightmusicconverter as lc
from pixelsarray import PixelsRGBArray
from midi_track import MidiTrack
from parser import get_parsed_args


# Install pillow and miditime :
pip.main(['install', 'Pillow'])
pip.main(['install', 'miditime'])
# Get arguments :
args = get_parsed_args('Narcotic music generator')
input_file_name = args.input
output_file_name = args.output
scan_mode = args.scan_mode
tempo = args.tempo
precision = args.precision

# Get rgb pixels array :
pixels = PixelsRGBArray(input_file_name)

# Choose scanning mode :
if scan_mode == 'horizontal':
    print('Horizontal scanning :')
    midi_notes = lc.get_midi_notes_by_horizontal_scan(pixels, precision)
else:
    print('Vertical scanning :')
    midi_notes = lc.get_midi_notes_by_vertical_scan(pixels, precision)

# Create track from midi notes :
track = MidiTrack(output_file_name, midi_notes, tempo)

# Save file :
track.save_to_file()
print('Saved into : ' + output_file_name)

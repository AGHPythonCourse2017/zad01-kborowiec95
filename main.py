from pixelsarray import PixelsRGBArray
import lightmusicconverter as lc
from midi_track import MidiTrack
from parser import get_parsed_args

args = get_parsed_args('Narcotic music generator')
input_file_name = args.input
output_file_name = args.output
scan_mode = args.scan_mode
tempo = args.tempo
precision = args.precision

pixels = PixelsRGBArray(input_file_name)
if scan_mode == 'horizontal':
    print('Horizontal scanning :')
    midi_notes = lc.get_midi_notes_by_horizontal_scan(pixels, precision)
else:
    print('Vertical scanning :')
    midi_notes = lc.get_midi_notes_by_vertical_scan(pixels, precision)
track = MidiTrack(output_file_name, midi_notes, tempo)
track.save_to_file()
print('Saved into : ' + output_file_name)

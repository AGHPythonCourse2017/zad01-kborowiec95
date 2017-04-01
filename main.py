from pixelsarray import PixelsRGBArray
from lightmusicconverter import get_midi_notes_by_horizontal_scan
from midi_track import MidiTrack
from parser import get_parsed_args

args = get_parsed_args('Narcotic music generator')
input_file_name = args.input
output_file_name = args.output
scan_mode = args.scan_mode
tempo = args.tempo
precision = args.precision

print(input_file_name, output_file_name, scan_mode, tempo, precision)
pixels = PixelsRGBArray(input_file_name)
if scan_mode == 'horizontal':
    midi_notes = get_midi_notes_by_horizontal_scan(pixels, precision)
else:
    midi_notes = get_midi_notes_by_vertical_scan(pixels, precision)
track = MidiTrack(output_file_name, midi_notes, tempo)
track.save_to_file()

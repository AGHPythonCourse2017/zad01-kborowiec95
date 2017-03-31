from miditime.miditime import MIDITime


class MidiTrack:
    # Add a track with those notes
    def __init__(self, file_name, midi_notes):
        self.track = MIDITime(120, file_name)
        self.track.add_track(midi_notes)

    # Output the .mid file
    def save_to_file(self):
        self.track.save_midi()
#!/usr/bin/env -S uv run --script

# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "pyfluidsynth",
# ]
# ///

import time

import fluidsynth

def local_file_path(file_name: str) -> str:
	"""
	Return a file path to a file that is in the same directory as this file.
	"""
	from os.path import dirname, join

	return join(dirname(__file__), file_name)

fs = fluidsynth.Synth()
fs.start()
## Your installation of FluidSynth may require a different driver.
## Use something like:
# fs.start(driver="pulseaudio")

sfid = fs.sfload(local_file_path("example.sf2"))
fs.program_select(0, sfid, 0, 0)

fs.noteon(0, 60, 30)
fs.noteon(0, 67, 30)
fs.noteon(0, 76, 30)

time.sleep(1.0)

fs.noteoff(0, 60)
fs.noteoff(0, 67)
fs.noteoff(0, 76)

time.sleep(1.0)

fs.delete()

# === Pink Floyd - Money ===
# 

def make_piano_notes():
    """
    Return a dictionary of piano notes and their corresponding MIDI values from 0 to 127.
    https://en.wikipedia.org/wiki/Piano_key_frequencies

    >>> piano_notes = make_piano_notes()
    >>> piano_notes["C-1"]
    0
    >>> piano_notes["C4"]
    60
    >>> piano_notes["G9"]
    127
    """
    twelve_notes = "C C# D D# E F F# G G# A A# B".split()

    def make_piano_note(i: int) -> str:
        return twelve_notes[i % 12] + str(i // 12 - 1)

    return {make_piano_note(i): i for i in range(128)}

piano_notes = make_piano_notes()

fs = fluidsynth.Synth()
fs.start()

sfid = fs.sfload(local_file_path("example.sf2"))
fs.program_select(0, sfid, 0, 0)

def play_note(note: int, duration: float):
	fs.noteon(0, note, 30)
	time.sleep(duration)
	fs.noteoff(0, note)

def play_notation(note: str = "C4", duration: float = 1.0):
    """
    Play a note using string notation such as "C4" for middle C, C#4 for C sharp, etc.
    """
    if isinstance(note, tuple):  # ("C4", 0.5)
        note, duration = note
    play_note(note=piano_notes[note.upper()], duration=duration / 2)


"""
print("Main theme")  # https://www.youtube.com/watch?v=xHHu_DTNbqM
main_notes = ("B3", ("B4", 0.5), ("F#4", 0.5), "B3", "F#3", "A3", "D4", "B3")
alt_notes = "D4 B3 F#3 A3 B3 D4 B3".split()  # D4 B3 
for _ in range(2):  # 8 times
    for notes in (main_notes, main_notes, alt_notes, main_notes):
        for note in notes:
            play_notation(note=note)
    # for note in ("B3", ("B4", 0.5), ("F#4", 0.5), "B3", "F#3", "A3", "D4", "B3"):
    #     play_notation(note=note)

# time.sleep(1.0)

# 62 59 62 59 66 57 59 62 59

# for note, duration in ((62, 1), (59, 1), (62, 1), (59, 1), (54, 1), (57, 1), (59, 1), (62, 1), (59, 1)):
#    play_note(note=note, duration=duration / 2)

# for note in "D4 B3 D4 B3 F#3 A3 B3 D4 B3".split():
#    play_notation(note=note)
    
print("Waterfall theme")
time.sleep(3.0)

# B5 A5 G5 F#5 E5 D5 C#5 A#4 B4

for note in ("B5", "A5", "G5", "F#5", "E5", "D5", "C#5", ("A#4", 0.5), "B4"):
	play_notation(note=note)
"""
print("Turnaround theme")  # 11:40 and 13:40
# time.sleep(3.0)

# F# F# C# F# A C# F# F E B F A B
for note in ("F#4", "F#4", "C#4", "F#3", "A3", "C#4", "F#4", "F4", "E4", "B3", "E3", "G3", "A3", "B3", "D4", "B3"):
    play_notation(note=note, duration=2)

# "B3 F#3 A3 B3 D4"

print("Solos theme")  # 18:20
# time.sleep(3.0)

for _ in range(4):  # 8 times
    for note in ("B3", "D4", ("C#4", 0.5), ("C4", 0.5), "A#4"):
        play_notation(note=note)

for _ in range(4):  # 4 times
    for note in ("E4", "D#4", "D4", "C#4"):
        play_notation(note=note)

"F#3 F#4 F4 E4 D4.5"

time.sleep(1.0)

def all_notes():
    notes = "C C# D D# E F F# G G# A A# B".split()
    from itertools import cycle
    for i, note in enumerate(cycle(notes)):
        if i > 127:
            break
        if i == 21:
            print("=== Piano starts ===")
        print(i, i // 12 - 1, note)
        if i == 108:
            print("=== Piano ends ===")

all_notes()

fs.delete()

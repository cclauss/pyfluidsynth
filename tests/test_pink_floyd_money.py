import pytest

from test.pink_floyd_money import make_piano_notes

piano_notes = make_piano_notes()


@pytest.mark.parametrize("note, expected", [
    ("C-1", 0),
    ("C4", 60),
    ("C#4", 61),
    ("D4", 62),
    ("D#4", 63),
    ("E4", 64),
    ("F4", 65),
    ("F#4", 66),
    ("G4", 67),
    ("G#4", 68),
    ("A4", 69),
    ("A#4", 70),
    ("B4", 71),
    ("C5", 72),
    ("G9", 127),
])
def test_make_piano_notes(note, expected):
    assert piano_notes[note] == expected

#  pytest.main("-v", "__file__")
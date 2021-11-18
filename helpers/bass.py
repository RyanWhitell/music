from .bmtithlop import *
from .general import *

import abjad
import random

SCALES = {
    "major": "P1,M2,M3,P4,P5,M6,M7,P8",
    "minor": "P1,M2,m3,P4,P5,m6,m7,P8",
}

COF = {
    "C" : {
        "minor": 'A'
    },
    "G" : {
        "minor": 'E'
    },
    "D" : {
        "minor": 'B'
    },
    "A" : {
        "minor": 'F#'
    },
    "E" : {
        "minor": 'C#'
    },
    "B" : {
        "minor": 'G#',
        "eq": 'Cb'
    },
    "F#" : {
        "minor": 'D#',
        "eq": 'Gb'
    },
    "Gb" : {
        "minor": 'Eb',
        "eq": 'F#'
    },
    "Db" : {
        "minor": 'Bb',
        "eq": 'C#'
    },
    "Ab" : {
        "minor": 'F'
    },
    "Eb" : {
        "minor": 'C'
    },
    "Bb" : {
        "minor": 'G'
    },
    "F" : {
        "minor": 'D'
    }
}

def make_scale(tonic, interval_segment):
    pitches = []
    pitch = abjad.NamedPitch(tonic)
    pitches.append(pitch)
    for interval in interval_segment:
        pitch = pitch + interval
        pitches.append(pitch)
    pitch_segment = abjad.PitchSegment(pitches)
    return pitch_segment

def show_lilly_bass_scale(tones, tonic, mode):
    """
        Rolls out the scale for all the octaves on a bass and prints the
        staff and plays the midi output.
    """
    tone_interval_map = {
        'S': '1',
        'T': '2'
    }
    
    # If the scale starts anywhere on c or d we start one octave up
    if ('c' in lily_conv(tonic) or 'd' in lily_conv(tonic) or 'ef' in lily_conv(tonic)):
        start_octave = ''
    else: 
        start_octave = ','
        
    interval_segment = abjad.IntervalSegment(' '.join(tones).replace('T', '2').replace('S', '1'))

    pitches = make_scale(lily_conv(tonic) + start_octave, interval_segment)

    notes = [abjad.Note(_, (1, 4)) for _ in abjad.PitchSegment(pitches)]

    voice = abjad.Voice(notes, name="Voice")
    abjad.attach(abjad.Clef('bass'), voice[0])
    staff = abjad.Staff([voice], name="Staff")
    if mode != 'chromatic':
        abjad.attach(abjad.KeySignature(tonic, mode), staff[0][0])
    abjad.show(abjad.LilyPondFile(items=["#(set-global-staff-size 48)", staff]))
    abjad.play(staff)
    
def show_lilly_bass_line(tones, tonic='c', mode='chromatic'):
    """
        Prints the bass melody/line onto a bass clef
    """
    voice = abjad.Voice(tones, name="Voice")
    abjad.attach(abjad.Clef('bass'), voice[0])
    staff = abjad.Staff([voice], name="Staff")
    if mode != 'chromatic':
        abjad.attach(abjad.KeySignature(tonic, mode), staff[0][0])
    abjad.show(abjad.LilyPondFile(items=["#(set-global-staff-size 48)", staff]))
    abjad.play(staff)
    
def get_tones_from_intervals(pattern_of_intervals):
    """
        Takes a pattern of intervals and returns the 
        tone/semitone representation.
    """
    pattern_of_intervals = pattern_of_intervals.split(',')
    tones = []
    for i in range(len(pattern_of_intervals)-1):
        index_one = 0
        index_two = 0
        for interval in intervals:
            if pattern_of_intervals[i] in interval:
                index_one = intervals.index(interval)
            if pattern_of_intervals[i+1] in interval:
                index_two = intervals.index(interval)
        distance = index_two - index_one
        if (distance == 2):
            tones.append('T')
        elif (distance == 1):
            tones.append('S')
        else:
            raise ValueError(f"Unknown tone distance ({distance}) in scale!")
    return tones


def pp_scale_detail(detail):
    """
        Simply adds a space if the scale detail 
        is only one character long.
    """
    if len(detail) == 1:
        return detail + ' '
    return detail

def get_bass_scale(pattern_of_intervals, tonic, mode):
    """
        Gets the definiton of the scale in three ways, prints the staff,
        and produces midi output to listen to.
    """
    intervals_dictionary = make_intervals_standard(tonic)
    scale = make_formula(pattern_of_intervals, intervals_dictionary)
    tones = get_tones_from_intervals(pattern_of_intervals)
    print(f"{sf_conv(tonic)} {mode.title()}")
    print(f"Spelling:  {'   '.join([pp_scale_detail(sf_conv(note)) for note in scale])}")
    print(f"Intervals: {'   '.join(pattern_of_intervals.split(','))}")
    print(f"Tones:     {'   '.join([pp_scale_detail(tone) for tone in tones])}")
    show_lilly_bass_scale(tones, lily_conv(tonic), mode)

def get_random_cof():
    choice = random.choice(list(COF.items()))
    get_bass_scale(SCALES['major'], choice[0], 'major')
    get_bass_scale(SCALES['minor'], choice[1]['minor'], 'minor')
    if 'eq' in choice[1]:
        get_bass_scale(SCALES['major'], choice[1]['eq'], 'major')
        
        
def replace_fret_number_with_symbol(string, notes):
    for note in notes:
        if isinstance(note, int):
            fret_number = str(note)
            replace_string = "●"
        else:
            fret_number = str(note[0])
            replace_string = note[1]
            
        string = string.replace("-" + fret_number + "-", " " + replace_string + " ")
        string = string.replace("|" + fret_number + "|", "|" + replace_string + "|")
    
    for note in range(1,21):
        string = string.replace("-" + str(note) + "-", "---")
        string = string.replace("|" + str(note) + "|", "|-|")

    return string

def make_bass_pattern(e, a, d, g):
    G = replace_fret_number_with_symbol(
        "G|---1---|---2---|---3---|--4--|--5--|--6--|--7--|--8--|--9--|--10--|-11-|-12-|-13-|-14-|-15-|16|17|18|19|20|",
        g
    )
    D = replace_fret_number_with_symbol(
        "D|---1---|---2---|---3---|--4--|--5--|--6--|--7--|--8--|--9--|--10--|-11-|-12-|-13-|-14-|-15-|16|17|18|19|20|",
        d
    )
    A = replace_fret_number_with_symbol(
        "A|---1---|---2---|---3---|--4--|--5--|--6--|--7--|--8--|--9--|--10--|-11-|-12-|-13-|-14-|-15-|16|17|18|19|20|",
        a
    )
    E = replace_fret_number_with_symbol(
        "E|---1---|---2---|---3---|--4--|--5--|--6--|--7--|--8--|--9--|--10--|-11-|-12-|-13-|-14-|-15-|16|17|18|19|20|",
        e
    )
    F1= " |       |       |       |     |     |     |     |     |     |     |   | • |   |   |   | | | | | |"
    F2= " |       |       |   •   |     |  •  |     |  •  |     |  •  |     |   |   |   |   | • | |•| |•| |"
    F3= " |       |       |       |     |     |     |     |     |     |     |   | • |   |   |   | | | | | |"
    print("\n".join([G, F1, D, F2, A, F3, E])) 
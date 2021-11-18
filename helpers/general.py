from IPython.display import IFrame
from IPython.display import Audio 
from IPython.core.display import display

def sf_conv(note):
    """
        Convert b and # characters to unicode flat and sharp symbols.
    """
    new_note = ''
    
    for i, char in enumerate(note):
        if i == 0:
            new_note += char
        else:
            new_note += char.replace('b', '\u266d').replace('#', '\u266f')
    return new_note

def lily_conv(note):
    """
        Converts bmtithlop notes to lilypond notation.
    """
    new_note = ''
    
    for i, char in enumerate(note):
        if i == 0:
            new_note += char.lower()
        else:
            new_note += char.replace('b', 'f').replace('#', 's').lower()
    return new_note

def pprint_notes_eqs(note_list):
    '''
    Formats and returns a note list by joining the enharmonic equivalents
    and converting the sharps and flats.
    '''
    return sf_conv('|'.join(note_list))

def get_common_eq(note_list):
    '''
    Returns the most common enharmonic equivalents in the list.
    '''
    temp_note = 'ERROR: Note not in list'
    for note in note_list:
        if len(note) == 1:
            return note
        if len(note) == 2 and  "#" in note: 
            temp_note = note
    return temp_note

def pprint_notes_common(note_list):
    '''
    Formats and returns a note list by getting the 
    most common enharmonic equivalents and 
    converting the sharps and flats.
    '''
    return sf_conv(get_common_eq(note_list))

def play_song(song_name):
    Audio(f'{song_name}.mp3')
    
def show_song(song_name):
    IFrame(f'./{song_name}.pdf', width=1340, height=1960)
def sf_conv(text):
    '''
    Convert b and # characters to unicode flat and sharp symbols.
    '''
    return text.replace('b', '\u266d').replace('#', '\u266f')

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
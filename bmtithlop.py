alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

notes_basic = [
    ['A'],
    ['A#', 'Bb'],
    ['B'],
    ['C'],
    ['C#', 'Db'],
    ['D'],
    ['D#', 'Eb'],
    ['E'],
    ['F'],
    ['F#', 'Gb'],
    ['G'],
    ['G#', 'Ab'],
]

notes = [
    ['B#',  'C',  'Dbb'],
    ['B##', 'C#', 'Db'],
    ['C##', 'D',  'Ebb'],
    ['D#',  'Eb', 'Fbb'],
    ['D##', 'E',  'Fb'],
    ['E#',  'F',  'Gbb'],
    ['E##', 'F#', 'Gb'],
    ['F##', 'G',  'Abb'],
    ['G#',  'Ab'],
    ['G##', 'A',  'Bbb'],
    ['A#',  'Bb', 'Cbb'],
    ['A##', 'B',  'Cb'],
]

intervals = [
    ['P1', 'd2'],  # Perfect unison   Diminished second
    ['m2', 'A1'],  # Minor second     Augmented unison
    ['M2', 'd3'],  # Major second     Diminished third
    ['m3', 'A2'],  # Minor third      Augmented second
    ['M3', 'd4'],  # Major third      Diminished fourth
    ['P4', 'A3'],  # Perfect fourth   Augmented third
    ['d5', 'A4'],  # Diminished fifth Augmented fourth
    ['P5', 'd6'],  # Perfect fifth    Diminished sixth
    ['m6', 'A5'],  # Minor sixth      Augmented fifth
    ['M6', 'd7'],  # Major sixth      Diminished seventh
    ['m7', 'A6'],  # Minor seventh    Augmented sixth
    ['M7', 'd8'],  # Major seventh    Diminished octave
    ['P8', 'A7'],  # Perfect octave   Augmented seventh
]

def find_note_index(scale, search_note):
    ''' Given a scale, find the index of a particular note '''
    for index, note in enumerate(scale):
        # Deal with situations where we have a list of enharmonic
        # equivalents, as well as just a single note as a str.
        if type(note) == list:
            if search_note in note:
                return index
        elif type(note) == str:
            if search_note == note:
                return index

def rotate(scale, n):
    ''' Left-rotate a scale by n positions. '''
    return scale[n:] + scale[:n]

def chromatic(key):
    ''' Generate a chromatic scale in a given key. '''
    # Figure out how much to rotate the notes list by and return
    # the rotated version.
    num_rotations = find_note_index(notes, key)
    return rotate(notes, num_rotations)

def make_intervals_standard(key):
    # Our labeled set of notes mapping interval names to notes
    labels = {}
    
    # Step 1: Generate a chromatic scale in our desired key
    chromatic_scale = chromatic(key)
    
    # The alphabets starting at provided key's alphabet
    alphabet_key = rotate(alphabet, find_note_index(alphabet, key[0]))
    
    # Iterate through all intervals (list of lists)
    for index, interval_list in enumerate(intervals):
    
        # Step 2: Find the notes to search through based on degree
        notes_to_search = chromatic_scale[index % len(chromatic_scale)]
        
        for interval_name in interval_list:
            # Get the interval degree
            degree = int(interval_name[1]) - 1 # e.g. M3 --> 3, m7 --> 7
            
            # Get the alphabet to look for
            alphabet_to_search = alphabet_key[degree % len(alphabet_key)]
            
            try:
                note = [x for x in notes_to_search if x[0] == alphabet_to_search][0]
            except:
                note = notes_to_search[0]
            
            labels[interval_name] = note

    return labels

def make_formula(formula, labeled):
    '''
    Given a comma-separated interval formula, and a set of labeled
    notes in a key, return the notes of the formula.
    '''
    return [labeled[x] for x in formula.split(',')]
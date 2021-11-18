####### Lilypond File #######
def create_lily(title, artist, key_tonic, key_mode, time_signature, tempo, chords, bass):
    KEY_SONG_TITLE = "KEY_SONG_TITLE"
    KEY_ARTIST = "KEY_ARTIST"
    KEY_KEY_TONIC = "KEY_KEY_TONIC"
    KEY_KEY_MODE = "KEY_KEY_MODE"
    KEY_TIME_SIGNATURE = "KEY_TIME_SIGNATURE"
    KEY_TEMPO = "KEY_TEMPO"
    KEY_CHORDS = "KEY_CHORDS"
    KEY_BASS = "KEY_BASS"

    template = open('/Users/whitell/dev/music/helpers/lily_template', 'r').read()

    template = template.replace(KEY_SONG_TITLE, title)
    template = template.replace(KEY_ARTIST, artist)
    template = template.replace(KEY_KEY_TONIC, key_tonic)
    template = template.replace(KEY_KEY_MODE, key_mode)
    template = template.replace(KEY_TIME_SIGNATURE, time_signature)
    template = template.replace(KEY_TEMPO, tempo)
    template = template.replace(KEY_CHORDS, chords)
    template = template.replace(KEY_BASS, bass)

    with open(f"{title} - {artist}.ly", "w") as text_file:
        text_file.write(template)
        
####### Measures #######
def join_chords(*args):
    """
        Joins the pitches of many strings into a 
        single string.
    """
    voice = []
    for part in args:
        if isinstance(part, str):
            voice.append(part)
        else:
            voice.append(f'\\repeat volta {part[1]} {{')
            voice.append(part[0])
            voice.append('}')
    return '\n  '.join(voice)

def join_bass(*args):
    """
        Joins the pitches of many strings into a 
        single string.
    """
    voice = []
    for part in args:
        if isinstance(part, str):
            voice.append(part)
        else:
            voice.append(f'\\repeat volta {part[1]} {{ ')
            voice.append(part[0])
            voice.append(f'\\mark "{part[1]}x" }}')
    return '\n  '.join(voice)

def combine_bars(*args):
    """
        Joins the bar strings into a part.
    """
    return '\n  '.join(args)


####### Notes and Articulation #######
def legato_slide(pitch_to):
    """
        Legato slide: Strike the first note and
        then slide the same fret-hand finger up or
        down to the second note. The second note
        is not struck.
    """
    return f'(\glissando {pitch_to})'

def staccato(pitch):
    """
        Staccato: Mute the note right after playing.
    """
    return f'{pitch}\staccato'
import abjad

####### Page and Score #######
GLOBAL_SETTINGS = r"""#(set-global-staff-size 36)
"""

def create_lilypond_file(score):
    """
        Creates the text that makes up a lillypond file
        by appending the global context to a score.
    """
    return abjad.LilyPondFile(items=[GLOBAL_SETTINGS, score])

def show_lilypond(score):
    """
        Shows the text that makes up a lillypond file.
    """
    lilypond_score_file = create_lilypond_file(score)
    print(abjad.lilypond(lilypond_score_file))

def show_score(score):
    """
        Shows the score in the global context.
    """
    lilypond_score_file = create_lilypond_file(score)
    abjad.show(lilypond_score_file)
    
def create_score(chords, bass, key_signature, time_signature, tempo):
    """
        Creates the combined bass and chord score.
    """
    chords = abjad.Voice("{" + chords + "}", lilypond_type="ChordNames", name="chords")
    bass = abjad.Voice(bass, name="bass")
    
    abjad.attach(abjad.Clef("bass"), bass[0])
    
    abjad.attach(key_signature, bass[0])
    abjad.attach(time_signature, bass[0])
    abjad.attach(tempo, bass[0])
    
    abjad.attach(key_signature, chords[0][0])
    abjad.attach(time_signature, chords[0][0])
    abjad.attach(tempo, chords[0][0])

    abjad.attach(abjad.LilyPondLiteral(r'\set noChordSymbol = ""'), chords[0])
    abjad.attach(abjad.LilyPondLiteral(r"\chordmode"), chords)
    
    bass_staff = abjad.Staff([bass], name="bassStaff")
    
    return abjad.Score([chords, bass_staff], name="score")
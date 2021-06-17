def legato_slide(pitch_from, pitch_to):
    """
        legato slide: Strike the first note and
        then slide the same fret-hand finger up or
        down to the second note. The second note
        is not struck.
    """
    return f'{pitch_from}(\glissando {pitch_to})'
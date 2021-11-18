\version "2.20.0"
\language "english"

\header {
  title = "Love That's Gone"
  subtitle = "La Sera"
}

global = {
  \key a \major
  \time 4/4
  \tempo 4=69
}

chordNames = \chordmode {
  \global
  \repeat volta 8 {
  a1
  }
  \repeat volta 2 {
  a2 d4 fs4:m
  e2 e4 d4
  }
  \repeat volta 6 {
  a2 d4 fs4:m
  e2 e4 d4
  a2 d4 fs4:m
  e2 e4 d4
  cs2:m d2
  cs2:m d2
  fs2:m e2
  }
  \repeat volta 2 {
  a2 d4 fs4:m
  e2 e4 d4
  }
  a1
}

electricBass = {
  \global
  \repeat volta 8 { 
  a,,8 a,,8 a,,8 a,,8 a,,8 a,,8 a,,8 a,,8
  \mark "8x" }
  \repeat volta 2 { 
  a,,8 a,,8 a,,8 a,,8 d,8 d,8 (\glissando fs,,8) fs,,8
  e,,8 e,,8 e,,8 e,,8 gs,,8 fs,,8 gs,,8 b,,8
  \mark "2x" }
  \repeat volta 6 { 
  a,,8 a,,8 a,,8 a,,8 d,8 d,8 (\glissando fs,,8) fs,,8
  e,,8 e,,8 e,,8 e,,8 gs,,8 fs,,8 gs,,8 b,,8
  a,,8 a,,8 a,,8 a,,8 d,8 d,8 (\glissando fs,,8) fs,,8
  e,,8 e,,8 e,,8 e,,8 gs,,8 fs,,8 gs,,8 b,,8
  cs,8 cs,8 cs,8 cs,8 (\glissando b,,8) b,,8 b,,8 b,,8
  (\glissando cs,8) cs,8 cs,8 cs,8 (\glissando b,,8) b,,8 b,,8 a,,8
  fs,,8 fs,,8 fs,,8 fs,,8 e,,8 e,,8 e,,8 e,,8
  \mark "6x" }
  \repeat volta 2 { 
  a,,8 a,,8 a,,8 a,,8 d,8 d,8 (\glissando fs,,8) fs,,8
  e,,8 e,,8 e,,8 e,,8 gs,,8 fs,,8 gs,,8 b,,8
  \mark "2x" }
  a,,1
}

electricBassPart = \new Staff \with {
  midiInstrument = "electric bass (finger)"
  % instrumentName = "Electric bass"
} { \clef "bass_8" \electricBass }

\score {
  <<
    \new ChordNames \chordNames
    \electricBassPart
  >>
  \layout { }
}

\score {
  <<
    \unfoldRepeats { \new ChordNames \chordNames }
    \unfoldRepeats { \electricBassPart }
  >>
  \midi { }
}

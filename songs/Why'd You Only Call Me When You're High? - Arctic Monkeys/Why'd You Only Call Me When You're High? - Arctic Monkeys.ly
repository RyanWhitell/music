\version "2.20.0"
\language "english"

\header {
  title = "Why'd You Only Call Me When You're High?"
  subtitle = "Arctic Monkeys"
}

global = {
  \key d \major
  \time 4/4
  \tempo 4=92
}

chordNames = \chordmode {
  \global
  
}

electricBass = {
  \global
  \repeat volta 5 { 
  fs,,4 r8 cs,8\staccato d,4 d,4
  b,,4 r8 cs,8\staccato b,,4 e,,4
  \mark "5x" }
  fs,,4 r8 cs,8\staccato d,4 d,4
  b,,4 r8 cs,8\staccato b,,4 e,,8\staccato fs,,8\staccato
  fs,,4 r8 cs,8\staccato d,4 d,4
  b,,4 r8 cs,8\staccato b,,4 e,,4
  fs,,4 r8 cs,8\staccato d,4 d,4
  b,,4 r8 cs,8\staccato b,,4 e,,4
  fs,,4 r8 cs,8\staccato d,4 r4
  b,,4 r8 cs,8\staccato b,,4 e,,4
  \repeat volta 5 { 
  fs,,4 r8 cs,8\staccato d,4 d,4
  b,,4 r8 cs,8\staccato b,,4 e,,4
  \mark "5x" }
  \repeat volta 2 { 
  fs,,4 r8 e,8\staccato d,4 d,4
  b,,4 r8 cs,8\staccato b,,4 e,,4
  fs,,4 r8 cs,8\staccato d,4 d,4
  b,,4 r8 cs,8\staccato b,,4 e,,4
  \mark "2x" }
  b,,4 r8 cs,8\staccato b,,4 b,,4
  \repeat volta 3 { 
  b,,4. cs,8\staccato d,4 r8 e,8\staccato
  fs,,8 fs,,8 fs,,8 e,,8 fs,,8 gs,,8 a,,8 cs,8
  \mark "3x" }
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

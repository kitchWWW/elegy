\version "2.18.2"
	
%#(set-global-staff-size 22)
	
\header{
title ="Elegy"
composer = "Brian Ellis"
tagline =""
}
\score{
\midi {}
\layout{}

<<
\new Staff \with {
  instrumentName = #"Clarinet"
  shortInstrumentName = #"Cl."
  midiInstrument = "Violin"
}{
	
	\absolute {
	\tempo 4 = 90
\numericTimeSignature

\override Staff.TimeSignature #'stencil = ##f 
\time 3/16
\override Score.BarLine.stencil = ##f 
\xNotesOn
\break r8 ^\markup{ \tiny "Earlier"} 
 s16  
 r8 ^\markup{ \tiny "today"} 
 s16  
 r8 ^\markup{ \tiny "I"} 
 s16  
 r8 ^\markup{ \tiny "met"} 
 s16  
 r8 ^\markup{ \tiny "with"} 
 s16  
 r8 ^\markup{ \tiny "student"} 
 s16  
 r8 ^\markup{ \tiny "leaders"} 
 s16  
 r8 ^\markup{ \tiny "to"} 
 s16  
 r8 ^\markup{ \tiny "discuss"} 
 s16  
 r8 ^\markup{ \tiny "ways"} 
 s16  
\break r8 ^\markup{ \tiny "that"} 
 s16  
 r8 ^\markup{ \tiny "our"} 
 s16  
 r8 ^\markup{ \tiny "community"} 
 s16  
 r8 ^\markup{ \tiny "can"} 
 s16  
 r8 ^\markup{ \tiny "come"} 
 s16  
 r8 ^\markup{ \tiny "together"} 
 s16  
 r8 ^\markup{ \tiny "during"} 
 s16  
 r8 ^\markup{ \tiny "this"} 
 s16  
 r8 ^\markup{ \tiny "difficult"} 
 s16  
 r8 ^\markup{ \tiny "time"} 
 s16  
\break
\xNotesOff
\revert Staff.TimeSignature #'stencil
\revert Score.BarLine.stencil 
\time 1/1
 r1  
 b'1 \ppp\< 
~ b'1 \mp\<\glissando 
~ bis'1 \mf\>\glissando 
~ b'1 \mp\!\glissando 
~ b'1 \mf\> 
~ b'1 \mp\< 
~ b'1 \mf\! 
\>
~ b'1  
\time 1/2
 r2 \! 
\time 1/1
 c''1 \f\> 
~ c''1  
~ c''1 \mf\> 
~ c''1 \mp\< 
~ c''1 \mf\! 
\<
~ c''1 ~ 
\time 1/2
 c''8 \sf 
 r4.  
\time 3/4
 a'4  
\times 2/3{
 f'4  
 c'4  
 e'4  
}
\time 4/4
 g'1  
\time 1/1
 b'1 \f\> 
~ b'1  
~ b'1 \mf\> 
~ b'1 \mp\< 
~ b'1 \mf\! 
\<
~ b'1 ~ 
\time 1/2
 b'8 \sf 
 r4.  
\override Staff.TimeSignature #'stencil = ##f 
\time 3/16
\override Score.BarLine.stencil = ##f 
\xNotesOn
\break r8 ^\markup{ \tiny "I"} 
 s16  
 r8 ^\markup{ \tiny "want"} 
 s16  
 r8 ^\markup{ \tiny "to"} 
 s16  
 r8 ^\markup{ \tiny "see"} 
 s16  
 r8 ^\markup{ \tiny "your"} 
 s16  
 r8 ^\markup{ \tiny "faces"} 
 s16  
\break
\xNotesOff
\revert Staff.TimeSignature #'stencil
\revert Score.BarLine.stencil 
\break
\time 5/4
\times 2/3{
 d'4  
 a'4  
 e'4  
}
 b'4  
 d'4  
 b'4  
\time 4/4
 d'1 \trill ^\markup { \sharp } 
\time 3/4
 a'4  
\times 2/3{
 f'4  
 c'4  
 e'4  
}
\time 4/4
 g'1  
\time 2/4
\times 2/3{
 a'4  
 e'4  
 f'4  
}
\time 4/4
 a'1 \trill ^\markup { \natural } 
\time 1/4
 r4  
\break
\time 1/4
 r4  
\time 1/1
 r1  
 c''1 \ppp\< 
~ c''1 \mf\> 
~ c''1 \mp\< 
~ c''1 \mf\! 
~ c''1 \mf\> 
~ c''1 \mp\< 
~ c''1 \mf\! 
\<
~ c''1 ~ 
\time 1/2
 c''8 \sf 
 r4.  	}	
}
%=========================================================================
\new Staff \with {
  instrumentName = #"Vibes"
  shortInstrumentName = #"V."
  midiInstrument = "Vibraphone"
}{
	\absolute {
	\tempo 4 = 90
\numericTimeSignature

\override Staff.TimeSignature #'stencil = ##f 
\time 3/16
\override Score.BarLine.stencil = ##f 
\xNotesOn
 d'8.  
 d'8.  
 d'8.  
 d'8.  
 d'8.  
 d'8.  
 d'8.  
 d'8.  
 d'8.  
 d'8.  
 d'8.  
 d'8.  
 d'8.  
 d'8.  
 d'8.  
 d'8.  
 d'8.  
 d'8.  
 d'8.  
 d'8.  
\xNotesOff
\revert Staff.TimeSignature #'stencil
\revert Score.BarLine.stencil 
\time 1/1
 b'1 \downbow \f\> 
~ b'1  
~ b'1 \mf\> 
~ b'1 \mp\< 
~ b'1 \mf\! 
~ b'1 \mp\<\glissando 
~ beh'1 \mf\>\glissando 
~ b'1 \mp\!\glissando 
\<
~ b'1 ~ 
\time 1/2
 b'8 \sf 
 r4.  
\time 1/1
 r1  
 c''1 \downbow \ppp\< 
~ c''1 \mp\<\glissando 
~ ceh''1 \mf\>\glissando 
~ c''1 \mp\!\glissando 
\>
~ c''1  
\time 1/2
 r2 \! 
\time 3/4
 g'4  
\times 2/3{
 g'4  
 d'4  
 f'4  
}
\time 4/4
 a'1 :32 
\time 1/1
 r1  
 b'1 :32 \ppp\< 
~ b'1 \mp\<\glissando 
~ beh'1 \mf\>\glissando 
~ b'1 \mp\!\glissando 
\>
~ b'1  
\time 1/2
 r2 \! 
\override Staff.TimeSignature #'stencil = ##f 
\time 3/16
\override Score.BarLine.stencil = ##f 
\xNotesOn
 d'8.  
 d'8.  
 d'8.  
 d'8.  
 d'8.  
 d'8.  
\xNotesOff
\revert Staff.TimeSignature #'stencil
\revert Score.BarLine.stencil 
\break
\time 5/4
\times 2/3{
 e'4  
 g'4  
 f'4  
}
 c''4  
 c'4  
 a'4  
\time 4/4
 e'1 :32 
\time 3/4
 g'4  
\times 2/3{
 g'4  
 d'4  
 f'4  
}
\time 4/4
 a'1 :32 
\time 2/4
\times 2/3{
 b'4  
 d'4  
 g'4  
}
\time 4/4
 b'1 :32 
\time 1/4
 r4  
\break
\time 1/4
 r4  
\time 1/1
 c''1 \downbow \f\> 
~ c''1  
~ c''1 \mp\<\glissando 
~ ceh''1 \mf\>\glissando 
~ c''1 \mp\!\glissando 
~ c''1 \mp\<\glissando 
~ ceh''1 \mf\>\glissando 
~ c''1 \mp\!\glissando 
\>
~ c''1  
\time 1/2
 r2 \! 	%vibes
	}	
}
>>
}
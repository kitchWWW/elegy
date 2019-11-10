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

	%clar
	}	
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

	%vibes
	}	
}
>>
}
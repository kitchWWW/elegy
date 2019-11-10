import random

sents = [
'I want to see your faces',
'Earlier today I met with student leaders to discuss ways that our community can come together during this difficult time',
'His voice was magical, and his gifts and talents touched students throughout campus.',
'We were too slow to let the entire campus know about the stabbings after they happened',
'The events of the past day are a reminder of how diligent we must be in communicating accurate information in the age of social media',
]

lilyNoteNames = ['c','cis','d','ees','e','f','fis','g','gis','a','bes','b']
lilyDurations = ['N/A','16','8','8.','4','XXX','4.','4..','2','XXX','XXX','XXX','2.','XXX','2..','2...','1']
lilyQuarterTone = ['eseh','es','eh','','ih','is','isih']
	#-3,-2,-1,0,1,2,3
GLOBAL_TRANSPOSE = 60
scale = [0,2,4,5,7,9,11,12,14]

stableNoteStrings = ['r','s']

class note():
	def __init__(self, *args):
		self.midiNoteNumber = 0
		self.lilyduration=4
		self.postlily = ""
		self.prelily = ""
		self.quarterToneInfo = 0
		self.onlyRaw = False
		if len(args) == 1 and type(args[0]) == str:
			self.onlyRaw = True
			self.postlily = args[0]
		else:
			for i in range(len(args)):
				if i == 0:
					self.midiNoteNumber = args[i]
				if i == 1:
					self.lilyduration = args[i]
				if i == 2:
					self.postlily = args[i]
				if i == 3:
					self.prelily = args[i]
				if i == 4:
					self.quarterToneInfo = args[i]

	def __str__(self):
		return "("+str(self.midiNoteNumber)+", "+str(self.lilyduration)+")"
	def __repr__(self):
		return "("+str(self.midiNoteNumber)+", "+str(self.lilyduration)+")"

	def tolily(self):
		if self.onlyRaw:
			return self.postlily
		if self.midiNoteNumber in stableNoteStrings:
			noteString = self.midiNoteNumber
		else:
			pitchClass = self.midiNoteNumber%12
			if self.quarterToneInfo == 0:
				pitchString = lilyNoteNames[pitchClass]
			else:
				pitchString = lilyNoteNames[pitchClass][:1]
				pitchString = pitchString+lilyQuarterTone[3+self.quarterToneInfo]

			numberOfUpTicks = int((GLOBAL_TRANSPOSE + self.midiNoteNumber)/12) - 4
			noteString = ''
			if numberOfUpTicks > 0:
				noteString= pitchString + "'"*numberOfUpTicks
			else:
				noteString= pitchString + ","*(-1*numberOfUpTicks)
		return self.prelily+" "+noteString+str(lilyDurations[self.lilyduration])+" "+self.postlily+" "


def getyourfuckingwordsizes(howMany):
	BREAK = '\\break'
	breakText = []
	listSizes = [0]
	index = 0
	for i in range(howMany):
		if listSizes[index] < 12:
			listSizes[index] += 1
		else:
			listSizes.append(1)
			index+=1
	print(listSizes)
	while abs(max(listSizes) - min(listSizes)) > 1:
		indexOfAdd = listSizes.index(min(listSizes))
		indexOfRemove = listSizes.index(max(listSizes))
		listSizes[indexOfRemove] -= 1
		listSizes[indexOfAdd] += 1
	print(listSizes)
	for	i in range(len(listSizes)):
		if i > 0:
			listSizes[i] += listSizes[i-1]
	print(listSizes)
	for i in range(howMany):
		thisText = ''
		if i == 0:
			thisText = BREAK
		if i in listSizes:
			thisText = BREAK
		breakText.append(thisText)

	print(breakText)
	return breakText










def getMelodySegment(trilltype):
	vibSeg = []
	claSeg = []

	chords = []
	lengthOfThisOne = random.randint(3,6)


	melNotes = random.sample(range(7),lengthOfThisOne)
	for j in melNotes:
		if random.random()<.5:
			vibSeg.append(note(scale[j]))
			claSeg.append(note(scale[j+1]))
		else:
			vibSeg.append(note(scale[j+1]))
			claSeg.append(note(scale[j]))

	eithNoteVersion = random.random()<.5
	if eithNoteVersion:
		onesToMakeEight = random.sample(range(lengthOfThisOne),2)
		print(onesToMakeEight)
		for i in onesToMakeEight:
			vibSeg[i].lilyduration = 2
			claSeg[i].lilyduration = 2

	if not eithNoteVersion:
		indexOfTrip = random.randint(0,lengthOfThisOne-3)
		vibSeg.insert(indexOfTrip,note("\\times 2/3{"))
		claSeg.insert(indexOfTrip,note("\\times 2/3{"))
		
		vibSeg.insert(indexOfTrip+4,note("}"))
		claSeg.insert(indexOfTrip+4,note("}"))


	vibSeg.insert(0,note("\\time {0}/4".format(lengthOfThisOne-1)))               
	claSeg.insert(0,note("\\time {0}/4".format(lengthOfThisOne-1)))

	vibSeg.append(note("\\time 4/4"))
	claSeg.append(note("\\time 4/4"))

	vibSeg.append(note(scale[melNotes[0]+1],16,":32"))
	claSeg.append(note(scale[melNotes[0]],16,trillOptions[whereToTrill[trilltype]]))

	return(claSeg,vibSeg)


def getBreak():
	vibSeg = []
	claSeg = []
	claSeg.append(note("\\break"))
	vibSeg.append(note("\\break"))
	return(claSeg,vibSeg)


def getRest(timeSig,duration):
	vibSeg = []
	claSeg = []

	vibSeg.append(note("\\time "+timeSig))
	vibSeg.append(note('r', duration))

	claSeg.append(note("\\time "+timeSig))
	claSeg.append(note('r', duration))
	return(claSeg,vibSeg)


WORDS_ONLY = 0
WORDS_AND_VIBE = 1


def getWords(wordsToUse,clarPitch,vibeNoteString,xNotes):
	vibSeg = []
	claSeg = []


	vibSeg.append(note("\\override Staff.TimeSignature #'stencil = ##f "))
	claSeg.append(note("\\override Staff.TimeSignature #'stencil = ##f "))

	words = sents[wordsToUse].split(" ")
	howMany = len(words)
	vibSeg.append(note("\\time 3/16"))
	claSeg.append(note("\\time 3/16"))
	vibSeg.append(note("\\override Score.BarLine.stencil = ##f "))
	claSeg.append(note("\\override Score.BarLine.stencil = ##f "))

	if xNotes:
		vibSeg.append(note("\\xNotesOn"))
		claSeg.append(note("\\xNotesOn"))
	


	wordsSeg = []
	notesSeg = []
	breakText = getyourfuckingwordsizes(howMany)

	magicNumb = 7

	for i in range(howMany):
		descriptionText = ""
		if i == 0:
			descriptionText='^\\markup{ \\tiny "speak in unison, normal talking pace"}'
		claSeg.append(note("r",2,'^\\markup{ \\tiny "'+words[i]+'"}',breakText[i]))
		claSeg.append(note("s",1,))
		vibSeg.append(note(2,3))
	claSeg.append(note("\\break"))

	if xNotes:
		vibSeg.append(note("\\xNotesOff"))
		claSeg.append(note("\\xNotesOff"))


	vibSeg.append(note("\\revert Staff.TimeSignature #'stencil"))
	claSeg.append(note("\\revert Staff.TimeSignature #'stencil"))
	vibSeg.append(note("\\revert Score.BarLine.stencil "))
	claSeg.append(note("\\revert Score.BarLine.stencil "))


	return(claSeg,vibSeg)




def getSustainSegment(pitchToSustainOn):
	CLAR = 0
	VIBE = 1
	vibSeg = []
	claSeg = []

	n = pitchToSustainOn
	bowOrTrem = ""
	if random.randint(0,1) == 1:
		bowOrTrem = ":32 "
	else:
		bowOrTrem = "\\downbow "

	whoStarts = random.randint(0,1)
	if whoStarts == CLAR:
		claSeg.append(note(n,16,'\\f\\>'))
		claSeg.append(note(n,16,'','~'))
		vibSeg.append(note('r',16))
		vibSeg.append(note(n,16,bowOrTrem+'\\ppp\\<'))
	else:
		vibSeg.append(note(n,16,bowOrTrem+'\\f\\>'))
		vibSeg.append(note(n,16,'','~'))
		claSeg.append(note('r',16))
		claSeg.append(note(n,16,'\\ppp\\<'))

	howManyBends = random.randint(1,2);
	for i in range(howManyBends):
		whoBends = random.randint(0,1)
		if whoBends == CLAR:
			claSeg.append(note(n,16,'\\mp\\<\\glissando','~'))
			claSeg.append(note(n,16,'\\mf\\>\\glissando','~',random.sample([-3,-2,-1,1,2,3],1)[0]))
			claSeg.append(note(n,16,'\\mp\\!\\glissando','~'))

			vibSeg.append(note(n,16,'\\mf\\>','~'))
			vibSeg.append(note(n,16,'\\mp\\<','~'))
			vibSeg.append(note(n,16,'\\mf\\!','~'))
		else:
			vibSeg.append(note(n,16,'\\mp\\<\\glissando','~'))
			vibSeg.append(note(n,16,'\\mf\\>\\glissando','~',-1))
			vibSeg.append(note(n,16,'\\mp\\!\\glissando','~'))

			claSeg.append(note(n,16,'\\mf\\>','~'))
			claSeg.append(note(n,16,'\\mp\\<','~'))
			claSeg.append(note(n,16,'\\mf\\!','~'))
	whoEnds = random.randint(0,1)

	if whoEnds == CLAR:
		claSeg.append(note("\\<"))
		claSeg.append(note(n,16,'~','~'))
		claSeg.append(note("\\time 1/2"))
		claSeg.append(note(n,2,"\\sf"))
		claSeg.append(note('r',6))

		vibSeg.append(note("\\>"))
		vibSeg.append(note(n,16,"",'~'))
		vibSeg.append(note("\\time 1/2"))
		vibSeg.append(note('r', 8,"\\!"))
	else:
		vibSeg.append(note("\\<"))
		vibSeg.append(note(n,16,'~','~'))
		vibSeg.append(note("\\time 1/2"))
		vibSeg.append(note(n,2,"\\sf",))
		vibSeg.append(note('r',6))

		claSeg.append(note("\\>"))
		claSeg.append(note(n,16,"",'~'))
		claSeg.append(note("\\time 1/2"))
		claSeg.append(note('r', 8,"\\!"))



	vibSeg.insert(0,note("\\time 1/1"))
	claSeg.insert(0,note("\\time 1/1"))

	return(claSeg,vibSeg)

















toWrite = []
vibePart = []
clarPart = []

whereToTrill = [0,1,2]
random.shuffle(whereToTrill)
trillOptions = [
"",
"\\trill ^\\markup { \\sharp }",
"\\trill ^\\markup { \\natural }",
]

sustains = random.sample(scale,3)
breaks = getBreak()


words1 = getWords(1,3,4,3)
clarPart.extend(words1[0])
vibePart.extend(words1[1])

sus1 = getSustainSegment(sustains[0])
clarPart.extend(sus1[0])
vibePart.extend(sus1[1])

sus2 = getSustainSegment(sustains[1])
clarPart.extend(sus2[0])
vibePart.extend(sus2[1])


mel1 = getMelodySegment(whereToTrill[0])
clarPart.extend(mel1[0])
vibePart.extend(mel1[1])


sus3 = getSustainSegment(sustains[0])
clarPart.extend(sus3[0])
vibePart.extend(sus3[1])


words1 = getWords(0,3,4,3)
clarPart.extend(words1[0])
vibePart.extend(words1[1])



clarPart.extend(breaks[0])
vibePart.extend(breaks[1])



mel2 = getMelodySegment(whereToTrill[1])
clarPart.extend(mel2[0])
vibePart.extend(mel2[1])

# mel1 = getMelodySegment(whereToTrill[0])
clarPart.extend(mel1[0])
vibePart.extend(mel1[1])

mel3 = getMelodySegment(whereToTrill[2])
clarPart.extend(mel3[0])
vibePart.extend(mel3[1])

rest1 = getRest("1/4",4)
clarPart.extend(rest1[0])
vibePart.extend(rest1[1])


clarPart.extend(breaks[0])
vibePart.extend(breaks[1])



rest1 = getRest("1/4",4)
clarPart.extend(rest1[0])
vibePart.extend(rest1[1])

sus4 = getSustainSegment(sustains[1])
clarPart.extend(sus4[0])
vibePart.extend(sus4[1])




vibePrint = []
for c in vibePart:
	vibePrint.append(c.tolily())
	# print(c.tolily())

clarPrint = []
for c in clarPart:
	clarPrint.append(c.tolily())
	# print(c.tolily())










fd = open("score.ly")
out = open("out.ly",'w')
for l in fd.readlines():
	if "%vibes" in l:
		out.write("\n".join(vibePrint))
	if "%clar" in l:
		out.write("\n".join(clarPrint))
	else:
		out.write(l)
out.close()
fd.close()
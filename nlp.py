

fd = open("text.txt")
sents = []
for l in fd.readlines():
	sents.extend(l.split("."))

sents[:] = [x for x in sents if x != '\n']

print sents



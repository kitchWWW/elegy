

for i in range(30):
    howMany = i
    if howMany > 12:
        minBreaks = howMany / 6.0
        maxBreaks = howMany / 12.0
        whereToBreak = sum([minBreaks,maxBreaks])/2
        howManyPerBeforeBreak = int(howMany / whereToBreak)
        print(howManyPerBeforeBreak)

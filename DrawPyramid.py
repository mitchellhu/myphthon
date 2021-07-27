starlist = [1,3,5,7,9]
maxwidth = max(starlist)
blankSpace = ' '
startSpace = '*'
tempcount = 0

def printLine(level):
    startline = ''
    spaceLeft = ''
    spaceRight = ''
    starline = startSpace * level
    tempcount = int((maxwidth - level) / 2)
    spaceLeft = blankSpace * tempcount
    spaceRight = spaceLeft
    print(spaceLeft + starline + spaceRight)

for i in starlist:
    printLine(i)
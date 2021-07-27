blankSpace = ' '
startSpace = '*'
tempcount = 0
maxwidth = 0

def printLine(level):
    startline = ''
    spaceLeft = ''
    spaceRight = ''
    starline = startSpace * level
    tempcount = int((maxwidth - level) / 2)
    spaceLeft = blankSpace * tempcount
    print(spaceLeft + starline)

def Is_evennumber(anumber):
    if int(anumber) % 2 == 0:
        return False
    else:
        return True


while True:
    usernumber = input('請輸入金字塔層數:')
    if isinstance(usernumber, int):
        print('請輸入整數數字！！！')
        continue
    if not Is_evennumber(usernumber):
        print('請輸入單數整數數字！！！')
        continue
    print('\n')
    maxwidth = int(usernumber);
    for i in range(1,int(usernumber)+1,2):
        printLine(i)
    break
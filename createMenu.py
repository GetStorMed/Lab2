#
def createMenu(optionList):
    tmp = ' '; ct = 0
    for opt in optionList:
        tmp += str(ct)
        ct += 1
    return tmp

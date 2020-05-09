import random

def getString(minLength, maxLength, lowercase=True, caps=False, symbols=False, numbers=False):
    lowercaseString = "abcdefghijklmnopqrstuvwxyz"
    uppercaseString = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numsString= "1234567890"
    symbolsString = r"""!@#$%^&*()~`,./<>?;:'"[]{}-=_+"""


    charString  = ""
    if lowercase:
        charString = charString + lowercaseString
    if caps:
        charString = charString + uppercaseString
    if symbols:
        charString = charString + symbolsString
    if numbers:
        charString = charString + numsString
    
    charList = list(charString)
    length = random.randint(minLength, maxLength)

    returnList = []
    l = 0
    while l < length:
        r = random.randint(0, len(charList)-1)
        returnList.append(charList[r])
        l+=1
    
    print(returnList)
    string = ''.join(returnList)
    return string
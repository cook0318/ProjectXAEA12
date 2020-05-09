import random

def getString(minWordLength=3, maxWordLength=10, lowercase=True, uppercase=False, symbols=False, numbers=False):
    # Define characters.
    lowercaseString = "abcdefghijklmnopqrstuvwxyz"
    uppercaseString = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numsString= "1234567890"
    symbolsString = r"""!@#$%^&*()~`,./<>?;:'"[]{}-=_+"""

    # Add characters specified in parameters to main character string.
    charString  = ""
    if lowercase:
        charString = charString + lowercaseString
    if uppercase:
        charString = charString + uppercaseString
    if symbols:
        charString = charString + symbolsString
    if numbers:
        charString = charString + numsString
    
    # Turn it to list for ease of accessing index, use random.randint to get a length between users parameters.
    charList = list(charString)
    length = random.randint(minWordLength, maxWordLength)

    # Add random characters to string until string is as long as length.
    returnList = []
    l = 0
    while l < length:
        r = random.randint(0, len(charList)-1)
        returnList.append(charList[r])
        l+=1
    
    # Join list into return string.
    string = ''.join(returnList)
    return string



def getSentence(minWords=3, maxWords=10, minWordLength=3, maxWordLength=10, lowercase=True, uppercase=False, symbols=False, numbers=False):
    # Get a random number of words to make between users parameters, using random.randint.
    numWords = random.randint(minWords, maxWords)
    listOfStrings = []

    # Using getString, add strings to sentence until its number of words reaches specified length above.
    w = 0
    while (w<numWords):
        string = getString(minWordLength, maxWordLength, lowercase, uppercase, symbols, numbers)
        listOfStrings.append(string)
        w+=1

    # To make the sentence seem more realistic, we will capitalize the first letter (if it's a letter) and add a period at the end.
    # Turn the first string to a list.
    firstString = listOfStrings[0]
    firstStringAsList = list(firstString)

    # If the first character of the first string can be made into uppercase, do it. Otherwise, we will generate a random 1 character
    # string from the list of uppercase letters.
    try:
        firstStringAsList[0] = firstStringAsList[0].upper()
    except Exception:
        firstStringAsList[0] = getString(1,1, False, True, False, False)
    
    # Now that the first character has been capitalized, we can turn it back to a string and add it back to the listOfStrings variable.
    firstString = ''.join(firstStringAsList)
    listOfStrings[0] = firstString
    
    # Join all strings into a sentence.
    sentence = ' '.join(listOfStrings)

    # Add a period at the end.
    sentence = sentence + "."
    
    return sentence



def getParagraph(minSentences=3, maxSentences=10, minWords=3, maxWords=10, minWordLength=3, maxWordLength=10, lowercase=True, uppercase=False, symbols=False, numbers=False):
    # Randomly chose the number of sentences between the users parameters using random.randint.
    numSentences = random.randint(minSentences,maxSentences)

    # Call getSentence for however many sentences we need to create.
    s = 0
    paragraph = []
    while s < numSentences:
        sentence = getSentence(minWords=3, maxWords=10, minWordLength=3, maxWordLength=10, lowercase=True, uppercase=False, symbols=False, numbers=False)
        sentence = sentence + " "
        paragraph.append(sentence)
        s+=1

    # Join the list of sentences into one string.
    paragraph = ''.join(paragraph)

    # Add a line break at the end.
    paragraph = paragraph + "\n"

    return paragraph


def getMuskBabyName():
    firstLetter = getString(1,1,False,True,False,False)

    specialChars = ['Æ', 'Œ', 'ᚠ', 'ᛘ','г', 'л', 'ъ', 'б', 'Ↄ', 'ꝯ̄','ꝋ','q̱','q̱̃','gͣ', 'Ꜿ', 'ꜿ','Ꝭ', 'ꝭ', 'Ꝅ', 'ꝅ', 'Ꝉ', 'ꝳ','ꝴ','Ꝓ',
    'Ꝙ', 'Ꝝ', 'ꝝ', 'Ꝟ',]

    planes = ["SR-71", "A-12", "B-52", "F-16", "H-4", "A320", "B-747", "VC-25", "10-E", "X-1", "B-25", "SR22", "AC-130", "DC-3", "C-172",
    "B-29", "G6", "G500", "F-35", "MQ-1", "J-3", "MiG-21"]

    name = firstLetter + " " + specialChars[random.randint(0,len(specialChars)-1)] + " " + planes[random.randint(0,len(planes)-1)]

    return name

print(getMuskBabyName())
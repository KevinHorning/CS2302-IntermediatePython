#6.37

import string

def scaryDict(textFile):
    List = []
    with open(textFile) as File:
        text = File.read()  
        translator = text.maketrans('','', string.punctuation)
        text = text.translate(translator)
        text = text.split(' ')

        wordCountsDict = {}      
        for word in text:
            if "\n" in word:
                word = word.replace("\n", "")
            notAdded = True
            for addedWord in wordCountsDict:
                if (word == addedWord):
                    wordCountsDict[addedWord] += 1
                    notAdded = False
                    continue
            if notAdded:
                wordCountsDict[word] = 1

        count = len(wordCountsDict)
        for word in sorted(wordCountsDict, key = wordCountsDict.get):
            print(word + ", " + str(wordCountsDict[word]) + ", " + str((wordCountsDict[word] / len(text)) / count))
            count -= 1
            
scaryDict("D:\Coding\Python\Bowler\HW2\LICENSE.txt")

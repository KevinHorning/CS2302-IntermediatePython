#6.23

import string

def scaryDict(textFile):
    'doc string yo'
    List = []
    with open(textFile) as File:
        text = File.read()  
        translator = text.maketrans('','', string.punctuation)
        text = text.translate(translator)
        text = text.split(' ')
        return sorted(list(set(text)))
    
print(len(scaryDict("D:\Coding\Python\Bowler\HW2\LICENSE.txt")))
#12.17

import string
import sqlite3

with open('LICENSE.txt', 'r') as file:
    text = file.read()  
    translator = text.maketrans('','', string.punctuation)
    text = text.translate(translator)
    text = text.split(' ')
    
    wordCountsDict = {}  
    for word in text:
        notAdded = True
        if "\n" in word:
            word = word.replace("\n", "")
        for addedWord in wordCountsDict:
            if (word == addedWord):
                wordCountsDict[addedWord] += 1
                notAdded = False
                continue
        if notAdded:
            wordCountsDict[word] = 1

con = sqlite3.connect('Wordcounts.db')
cur = con.cursor()

cur.execute('CREATE TABLE Wordcounts (Word text, Frequency int)')

for word in wordCountsDict:
    cur.execute("INSERT INTO Wordcounts VALUES ('{0}' , {1})".format(word, wordCountsDict[word]))

'''
cur.execute('SELECT * FROM Wordcounts')
print(cur.fetchall())
'''
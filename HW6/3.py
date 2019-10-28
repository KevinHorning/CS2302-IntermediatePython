#12.22

import itertools

def panagram(wordList):
    for word in wordList:
        print(["".join(perm) for perm in itertools.permutations(word)])
        
'''
panagram(['rock', 'kit'])
'''
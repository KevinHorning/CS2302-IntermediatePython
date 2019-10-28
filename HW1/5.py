#4.25
def vowelCount(string):
    List = []
    List.append(string.count('a') + string.count('A'))
    List.append(string.count('e') + string.count('E'))
    List.append(string.count('i') + string.count('I'))
    List.append(string.count('o') + string.count('O'))
    List.append(string.count('u') + string.count('U'))
    print ("a, e, i, o and u appear, respectively, %d, %d, %d, %d, and %d times" % (List[0], List[1], List[2], List[3], List[4]))
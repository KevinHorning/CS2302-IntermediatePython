#4.23
def average():
    Input = input("Enter a sentence: ")
    List = Input.split(' ')
    i = len(List)
    while(i > 0):
        if (List[i - 1] == ''):
            List.remove(List[i - 1])
        i -= 1
    totalLetters = 0
    for word in List:
        totalLetters += len(word)
    print(totalLetters / len(List))
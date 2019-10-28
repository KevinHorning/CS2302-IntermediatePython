#HW Assignment 1
#2302 Python 2
#Professor Bowler
#1-26-19

#3.29
Input = input("Enter an int: ")

def PrintDivisors(num):
    global Input
    if (num <= 0):
        num = num    
    else:
        PrintDivisors(num - 1)
        if (int(Input) % num == 0):
            print(num)

PrintDivisors(int(Input))

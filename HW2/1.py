#HW Assignment 2
#2302 Python 2
#Professor Bowler
#2-10-19

#5.28

def geometric(list):
    for Int in list:
        if (type(Int) is not int):
            return False
        if (list.index(Int) + 1 < len(list)):
            if Int * 2 != list[list.index(Int) + 1]:
                return False
    return True

#print(geometric([1, 2, 4, 8]))
    
            

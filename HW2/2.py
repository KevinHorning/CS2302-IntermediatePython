#5.37

def mssl(List):
    maxSum = 0
    bestSlice = []
    startIndex = 0

    while (startIndex < len(List)):
        for endIndex in range(startIndex + 1, len(List) + 1):
            if (sum(List[startIndex:endIndex]) > maxSum):
                maxSum = sum(List[startIndex:endIndex])
                bestSlice = List[startIndex:endIndex]
        startIndex += 1
                
    return maxSum

#print(mssl( [3,4,5] ))
          

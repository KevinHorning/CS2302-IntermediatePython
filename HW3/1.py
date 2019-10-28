#HW Assignment 3
#2302 Python 2
#Professor Bowler
#3-4-19

#8.35

class stack(object):
    top = -1
    data = []
    
    def peek(self):
        return self.data[self.top]
    
    def isEmpty(self):
        if self.top is -1:
            return True
        else:
            return False
    
    def push(self, item):
        self.top += 1
        self.data += [item]
        
    def pop(self):
        if self.isEmpty:
            raise Exception('Cannot pop empty stack') 
        else:
            popped = self.peek()
            self.top -= 1
            return popped
        
    def __len__(self):
        return len(self.top + 1)
    
    def __str__(self):
        listString = []
        for item in self.data[0:self.top + 1]:
            listString += [item]
        return str(listString)
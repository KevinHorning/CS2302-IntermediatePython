#HW Assignment 6
#2302 Python 2
#Professor Bowler
#4-13-19

#11.16
from html.parser import HTMLParser

class ListCollector(HTMLParser):
    def __init__(self):
        super().__init__()
        self.lists = []
        self.listCounter = -1
        self.isReadingList = False
        
    def handle_starttag(self, tag, attrs):
        if tag == 'ol' or tag == 'ul':
            self.isReadingList = True
            self.listCounter += 1
            self.lists.append([])
            
    def handle_endtag(self, tag):
        if tag == 'ol' or tag == 'ul':
            self.isReadingList = False

    def handle_data(self, data):
        if self.isReadingList:
            if data[0:1] != '\n' and data[0:1] != '\t':
                self.lists[self.listCounter].append(data)
               
    def getLists(self):
        print(self.lists)

'''  
with open('html.html', 'r') as file:
    html = file.read()
    reader = ListCollector()
    reader.feed(html)
    reader.getLists()
'''
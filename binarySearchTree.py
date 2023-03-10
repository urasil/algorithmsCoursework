import string
import random

class BinarySearchTreeSet():
    
    def __init__(self, element): 
        self.right = None
        self.left = None
        self.element = element
        
    def insertElement(self, element):
        inserted = False
        
        if self.element == element:
            inserted = True
            
        elif self.element > element:
            if self.left is None:
                self.left = BinarySearchTreeSet(element)
                inserted = True
            else:
                self.left.insertElement(element)
                
        else:
            if self.right is None:
                self.right = BinarySearchTreeSet(element)
                inserted = True
            else:
                self.right.insertElement(element)
        
        return inserted

    def searchElement(self, element):     
        found = False
        if element == self.element:
            found = True
        
        elif self.element > element:
            if self.left is not None:
                return self.left.searchElement(element)
        else:
            if self.right is not None:
                return self.right.searchElement(element)
        
        return found 

# tree = BinarySearchTreeSet(5)
# tree.insertElement(2)
# tree.insertElement(1)
# tree.insertElement(19)
# print(tree.searchElement(2))
 

class TestDataGenerator():
    
    def __init__(self):

        pass           
        
    def generateData(self, size):     
        # ADD YOUR CODE HERE
        data = [""]*size

        for i in range(len(data)):
            length = random.randint(1,10)
            for _ in range(length):
                data[i] += (random.choice(string.ascii_lowercase)) 
                
        return data   

tree = BinarySearchTreeSet("start")
def toRead():
    file = open(input("enter the file name: "), "r")
    for line in file:
        for word in line.split():
            tree.insertElement(word)
    file.close()


toRead()
#/home/uras/Documents/COMP0002/Python/algorithmsCoursework/testfiles/test1-mobydick.txt
print(tree.searchElement("foolishness"))
print(tree.searchElement("uras"))


class SequentialSearchSet():
    
    def __init__(self):    
        self.lst = []
        pass           
     
    def insertElement(self, element):
        inserted = False
        if element in self.lst:
            inserted = False
        else:
            self.lst.append(element)
            inserted = True

        return inserted
    
    

    def searchElement(self, element):     
        found = False
        if element in self.lst:
            found = True
    
        return found    

x = SequentialSearchSet()
def toRead(a):
    file = open(input("enter the file name: "), "r")
    for line in file:
        for word in line.split():
            a.insertElement(word)
    file.close()

# toRead(x)
# print(x.searchElement("coral"))
# print(x.searchElement("uras"))

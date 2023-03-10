class BloomFilterSet():
    
    def __init__(self,size):
        # ADD YOUR CODE HERE
        self.size = size 
        self.buckets = [0] * self.size           
        
    def insertElement(self, element):
        inserted = False
        hashValue = self.hashFunction(element)
        self.buckets[hashValue] = 1
        return hashValue

    def searchElement(self, element):     
        found = False
        # ADD YOUR CODE HERE
        hashValue = self.hashFunction(element)
        if self.buckets[hashValue] == 1:
            found = True
        return found    

    def hashFunction(self, element):
        return hash(element) % self.size

x = BloomFilterSet(1000000)

def toRead():
    file = open(input("enter the file name: "), "r")
    for line in file:
        for word in line.split():
            x.insertElement(word)
    file.close()

toRead()
print(x.searchElement("times"))
print(x.searchElement("qayyum"))
print(x.searchElement("uras"))

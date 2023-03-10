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
import random
import string

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
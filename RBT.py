import timeit

class Node:
        def __init__(self, element):
            self.element = element
            self.left = None
            self.right = None
            self.color = "BLACK"

class LeftLeaningRedBlackTree:
    def __init__(self):
        self.root = None

    def isRed(self, node):
        if node is None:
            return False
        return node.color == "RED"

    def rotateLeft(self, node):
        temp = node.right
        node.right = temp.left
        temp.left = node
        temp.color = node.color
        node.color = "RED"
        return temp

    def rotateRight(self, node):
        temp = node.left
        node.left = temp.right
        temp.right = node
        temp.color = node.color
        node.color = "RED"
        return temp

    def flipColors(self, node):
        node.color = "RED"
        node.left.color = "BLACK"
        node.right.color = "BLACK"

    def insertElement(self, element):
        inserted = False
        self.root = self.recursiveInsert(self.root, element)
        self.root.color = "BLACK"
        return inserted

    def recursiveInsert(self, node, element):
        if node is None:
            return Node(element)

        if element < node.element:
            node.left = self.recursiveInsert(node.left, element)
        elif element > node.element:
            node.right = self.recursiveInsert(node.right, element)

        # Maintain left-leaning property
        if self.isRed(node.right) and not self.isRed(node.left):
            node = self.rotateLeft(node)
        if self.isRed(node.left) and self.isRed(node.left.left):
            node = self.rotateRight(node)
        if self.isRed(node.left) and self.isRed(node.right):
            self.flipColors(node)

        return node

    def searchElement(self, element):
        found = self.recursiveSearch(self.root, element)
        return found

    def recursiveSearch(self, node, element):
        if node is None:
            return False
        if element < node.element:
            return self.recursiveSearch(node.left, element)
        elif element > node.element:
            return self.recursiveSearch(node.right, element)
        else:
            return True

x = LeftLeaningRedBlackTree()
def toRead():
    file = open(input("enter the file name: "), "r")
    for line in file:
        for word in line.split():
            x.insertElement(word)
    file.close()

def toSearch():
    file = open("/home/uras/Documents/COMP0002/Algorithms/algorithmsCoursework/testfiles/test-search.txt")
    for line in file:
        for word in line.split():
            result = x.searchElement(word)
            print("Word ", word, "is in the list: ", result)

    file.close()
    
toRead()
toSearch()


# toRead()
# print(x.searchElement("disconcerted"))
# print(x.searchElement("qayyum"))
# print(x.searchElement("uras"))



# ADD YOUR TEST CODE HERE TO WORK ON REAL DATA

# x.insertElement("uras")
# def takingTime(codeToExecInString, numberOfExecution):
#     code = codeToExecInString
#     executionTime = timeit.timeit(code, globals=globals(), number=numberOfExecution)
#     print(f"Execution time: {executionTime} seconds")

# takingTime("x.searchElement('Uras')", 10000000)


class Node:
    def __init__(self, element):
        self.element = element
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insertElement(self, element):
        inserted = False

        if self.root is None:
            self.root = Node(element)
        else:
            inserted = self.recursiveInsert(element, self.root, inserted)
        return inserted 
    
    def recursiveInsert(self, element, currentNode, inserted):
        if element < currentNode.element:
            if currentNode.left is None:
                currentNode.left = Node(element)
                return True
            else:
                self.recursiveInsert(element, currentNode.left)
        elif element > currentNode.element:
            if currentNode.right is None:
                currentNode.right = Node(element)
                return True
            else:
                self.recursiveInsert(element, currentNode.right)
        else:
            print("Element already in tree.")
    
    def searchElement(self, element):
        found = False
        if self.root is None:
            return False
        else:
            found = self.recursiveSearch(element, self.root, found)

        return found
    
    def recursiveSearch(self, element, currentNode, found):
        if currentNode is None:
            return False
        elif element == currentNode.element:
            return True
        elif element < currentNode.element:
            return self.recursiveSearch(element, currentNode.left)
        else:
            return self.recursiveSearch(element, currentNode.right)


# Create a new binary search tree
bst = BinarySearchTree()

# Insert some elements into the tree
bst.insert(8)
bst.insert(3)
bst.insert(10)
bst.insert(1)   
bst.insert(14)
bst.insert(4)
bst.insert(7)
bst.insert(13)

# Search for an element in the tree
if bst.search(6):
    print("Found 6 in the tree!")
else:
    print("Did not find 6 in the tree.")

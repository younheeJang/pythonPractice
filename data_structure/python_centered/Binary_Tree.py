
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, new):
        if self.value:
            if new < self.value:
                if self.left is None:
                    self.left = Node(new)
                else:
                    self.left.insert(new)
            elif new > self.value:
                if self.right is None:
                    self.right = Node(new)
                else:
                    self.right.insert(new)
        else:
            self.value = new

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.value)
        if self.right:
            self.right.printTree()

# Use the insert method to add nodes
root = Node(10)
root.insert(6)
root.insert(14)
root.insert(1)

root.printTree()



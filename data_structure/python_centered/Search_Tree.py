class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def printAll(self):
        if self.left:
            self.left.printAll()
        print(self.value)
        if self.right:
            self.right.printAll()
    def insert(self, value):
        if self.value:
            if value < self.value:
                if self.left is None:
                    self.left = Node(value)
                else:
                    self.left.insert(value)
            elif value > self.value:
                if self.right is None:
                    self.right = Node(value)
                else:
                    self.right.insert(value)
        else:
            self.value = value


root = Node(10)
root.insert(11)
root.insert(9)
root.printAll()
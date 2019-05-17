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
    def findOne(self, value):
        if value < self.value:
            if self.value is None:
                return str(value)+" is not Found"
            return self.left.findOne(value)
        elif value > self.value:
            if self.right is None:
                return str(value)+" is not Found"
            return self.right.findOne(value)
        else:
            return value

root = Node(10)
root.insert(11)
root.insert(9)
root.printAll()

print()

print(root.findOne(9))
print(root.findOne(11))
print(root.findOne(99))
print(root.findOne(10))
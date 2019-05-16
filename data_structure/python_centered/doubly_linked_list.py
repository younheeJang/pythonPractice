class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class doubly_linked_list:

    def __init__(self):
        self.head = None

    #맨 앞에 넣자
    def push(self, new):
        newNode = Node(new)
        newNode.next = self.head
        if self.head is not None:
            self.head.prev = newNode
        self.head = newNode

    #가운데 넣자: 앞 뒤 작업
    def insert(self, prev, new):
        if prev is None:
            return
        newNode = Node(new)
        newNode.next = prev.next
        prev.next = newNode
        newNode.prev = prev
        if newNode.next is not None:
            newNode.next.prev = newNode

    #맨 끝에 넣자 : 맨 끝으로 가기전까지 계속 while
    def append(self, new):
        newNode = Node(new)
        newNode.next = None
        if self.head is None:
            newNode.prev = None
            self.head = newNode
            return
        last = self.head
        while(last.next is not None):
            last = last.next
        last.next = newNode
        newNode.prev = last
        return

    def printAll_each(self):
        printValue = self.head
        while printValue is not None:
            print(printValue.value, end=" ")
            printValue = printValue.next
        print()


d_Linked_list = doubly_linked_list()
d_Linked_list.push("doubly_linked_list")
d_Linked_list.push("jeager")
d_Linked_list.push("curious")
d_Linked_list.printAll_each()

d_Linked_list.insert(d_Linked_list.head.next, "study")
d_Linked_list.printAll_each()

d_Linked_list.append("so sweet")
d_Linked_list.printAll_each()
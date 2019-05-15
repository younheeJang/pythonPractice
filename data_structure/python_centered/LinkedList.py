class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None
    def listprint(self):
        printvalue = self.head
        while printvalue  is not None:
            print(printvalue .value)
            printvalue = printvalue.next
    def atBegining(self, new):
        newNode = Node(new)
        newNode.next = self.head
        self.head = newNode
    def atEnd(self, new):
        newNode = Node(new)
        if self.head is None:
            self.head = newNode
            return
        lastElement = self.head
        while lastElement.next:
            lastElement = lastElement.next
        lastElement.next = newNode
    def atBetween(self, middle_node, new):
        if middle_node is None:
            print("the mentioned node is absent")
            return
        newNode = Node(new)
        newNode.next = middle_node.next
        middle_node.next = newNode
    def removeNode(self, removeKsy):
        head  = self.head


        #만약 헤드가 논이 아니고, 헤드가 지워야 할 노드가 아니라면,
        #헤드가 논이 될 떄까지
        while(head is not None):
            if (head.value == removeKsy):
                break
            prev = head
            head = head.next
        prev.next = head.next
        head = None

        if (head is not None):
            if (head.value == removeKsy):
                self.head = head.next
                head = None
                return

        if(head == None):
            return





list1 = SLinkedList()
list1.head = Node("this is")
e2 = Node("jeager")
e3 = Node("watermelon")
list1.head.next = e2
e2.next = e3
list1.listprint()

print()

list1.atBegining("i love you")
list1.listprint()

print()

list1.atEnd("so mushroom")
list1.listprint()

print()

list1.atBetween(list1.head, "바로 앞에 거 다음으로 들어갈.")
list1.listprint()


print()

list1.removeNode("바로 앞에 거 다음으로 들어갈.")
list1.removeNode("so mushroom")
list1.listprint()


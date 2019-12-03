
class LinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def addFront(self, node):
        tmp_head = self.head
        
        if self.head == None:
            self.head = node
            self.tail = node
            return
        
        self.head = node
        self.head.next = tmp_head
        return


    def addRear(self, node):
        tmp_tail = self.tail
        
        if self.tail == None:
            self.head = node
            self.tail = node
            return 
        
        self.tail = node
        tmp_tail.next = self.tail
        return


from node import Node

start = Node(0)

current = start
for i in range(1, 10):
    current.next = Node(i)
    current = current.next

currNode = start
while (currNode != None):
    print(currNode.value)
    currNode = currNode.next

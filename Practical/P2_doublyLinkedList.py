class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def insertAtBeginning(self, item):
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    
    def insertAtEnd(self, item):
        new_node = Node(item)
        if self.head is None:
            self.insertAtBeginning(item)
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp
    
    def insertAtPosition(self, item, at):
        new_node = Node(item)
        if at <= 0:
            print("Postion must be greater than 0")
            return
        if self.head is None and at == 1:
            self.insertAtBeginning(item)
            return
        temp = self.head
        for i in range(1, at - 1):
            temp = temp.next
            if temp is None:
                print("Index out of bounds")
                return
        if temp.next is None:
            temp.next = new_node
            new_node.prev = temp
        else:
            new_node.next = temp.next
            temp.next.prev = new_node
            temp.next = new_node
            new_node.prev = temp
    
    def deleteAtBeginning(self):
        if self.head is None:
            return
        self.head = self.head.next
        if self.head:
            self.head.prev = None
    
    def deleteAtEnd(self):
        if self.head is None:
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        if temp.prev:
            temp.prev.next = None
        else:
            self.head = None
    
    def traverseForward(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()
    
    def traverseBackward(self):
        temp = self.head
        if not temp:
            return
        while temp.next:
            temp = temp.next
        while temp:
            print(temp.data, end=" ")
            temp = temp.prev
        print()
    

doublylinkedlist = DoublyLinkedList()

doublylinkedlist.insertAtBeginning(96)
doublylinkedlist.insertAtPosition(95, 1)
doublylinkedlist.insertAtEnd(94)

doublylinkedlist.traverseBackward()

doublylinkedlist.deleteAtBeginning()
doublylinkedlist.deleteAtEnd()

doublylinkedlist.traverseForward()

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insertAtBeginning(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node
    
    def insertAtEnd(self, item):
        new_node = Node(item)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
    
    def inserAtPosition(self, item, at):
        if at == 0:
            self.insertAtBeginning(item)
            return
        
        new_node = Node(item)
        current = self.head

        for _ in range(at-1):
            if not current:
                raise IndexError("Postiton out of bounds")
            current = current.next
        new_node.next = current.next
        current.next = new_node
    
    def deleteFromBeginning(self):
        if not self.head:
            raise IndexError("List is empty")
        self.head = self.head.next
    
    def deleteFromEnd(self):
        if not self.head:
            raise IndexError("List is empty")
        if not self.head.next:
            self.head = None
            return
        second_last = self.head
        while second_last.next:
            second_last = second_last.next
            second_last.next = None
    
    def traverse(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements
    


Singlylinkedlist = SinglyLinkedList()

Singlylinkedlist.insertAtBeginning(56)
Singlylinkedlist.inserAtPosition(65, 1)
Singlylinkedlist.inserAtPosition(69, 2)
Singlylinkedlist.insertAtEnd(96)

print(Singlylinkedlist.traverse())

Singlylinkedlist.deleteFromBeginning()
Singlylinkedlist.deleteFromEnd()

print(Singlylinkedlist.traverse())

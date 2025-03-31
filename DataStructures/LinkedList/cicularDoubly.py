class Node:
    def __init__(self, data: any):
        self.data = data
        self.next = None
        self.prev = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def insert(self, data: any, toPosition: bool = False, position: int = 0):
        """
        Inserts a node at the beginning, a specific position, or the end.

        Time Complexity:
            - for insertion at beginning: O(1)
            - for insertion at a specific position: O(n)
            - for insertion at the end: O(1)
        """
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            self.head.next = self.head
            self.head.prev = self.head
            self.size += 1
            return

        if toPosition:
            if position > self.size or position < 0:
                print("ERROR: Invalid position for insertion")
                return
            
            if position == 0:
                tail = self.head.prev
                new_node.next = self.head
                new_node.prev = tail
                tail.next = new_node
                self.head.prev = new_node
                self.head = new_node
                self.size += 1
                return

            current = self.head
            for _ in range(position - 1):
                current = current.next
            
            new_node.next = current.next
            new_node.prev = current
            current.next.prev = new_node
            current.next = new_node
            self.size += 1
            return
        
        tail = self.head.prev
        tail.next = new_node
        new_node.prev = tail
        new_node.next = self.head
        self.head.prev = new_node
        self.size += 1

    def delete(self, toPosition: bool = False, position: int = 0):
        """
        Deletes a node from the beginning, a specific position, or the end.

        Time Complexity:
            - for deletion at beginning: O(1)
            - for deletion at a specific position: O(n)
            - for deletion at the end: O(1)
        """
        if not self.head:
            print("ERROR: Linked list is empty")
            return
        
        if toPosition:
            if position >= self.size or position < 0:
                print("ERROR: Invalid position for deletion")
                return
            
            if position == 0:
                tail = self.head.prev
                self.head = self.head.next
                self.head.prev = tail
                tail.next = self.head
                self.size -= 1
                return

            current = self.head
            for _ in range(position - 1):
                current = current.next

            current.next = current.next.next
            current.next.prev = current
            self.size -= 1
            return
        
        tail = self.head.prev
        tail.prev.next = self.head
        self.head.prev = tail.prev
        self.size -= 1

    def traverse(self, backward: bool = False):
        if not self.head:
            print("Linked list is empty")
            return
        
        current = self.head

        if backward:
            tail = self.head.prev
            while True:
                print(tail.data, end=" <- ")
                tail = tail.prev
                if tail == self.head.prev: break
            print()
            return

        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head: 
                print() 
                return
        

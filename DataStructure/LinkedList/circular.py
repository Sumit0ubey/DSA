class Node:
    def __init__(self, data: any):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def insert(self, data: any, toPosition: bool = False, position: int = 0):
        """
        Inserts a node at the beginning, a specific position, or the end.

        Time Complexity:
            - for insertion at beginning: O(1)
            - for insertion at a specific position: O(n)
            - for insertion at the end: O(n)
        """
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            self.head.next = self.head
            self.size += 1
            return
        
        if toPosition:
            if position > self.size or position < 0:
                print("ERROR: Invalid position for insertion")
                return

            if position == 0:
                tail = self.head
                while tail.next != self.head:
                    tail = tail.next
                
                new_node.next = self.head
                self.head = new_node
                tail.next = self.head
                self.size += 1
                return

            current = self.head
            for _ in range(position - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
            self.size += 1
            return
        
        current = self.head
        while current.next != self.head:
            current = current.next
        current.next = new_node
        new_node.next = self.head
        self.size += 1

    def delete(self, toPosition: bool = False, position: int = 0):
        """
        Deletes a node from the beginning, a specific position, or the end.

        Time Complexity:
            - for deletion at beginning: O(1)
            - for deletion at a specific position: O(n)
            - for deletion at the end: O(n)
        """
        if not self.head:
            print("ERROR: Linked list is empty")
            return

        if toPosition:
            if position >= self.size or position < 0:
                print("ERROR: Invalid position for deletion")
                return

            if position == 0:
                tail = self.head
                while tail.next != self.head:
                    tail = tail.next
                if self.head == self.head.next:
                    self.head = None
                else:
                    self.head = self.head.next
                    tail.next = self.head
                
                self.size -= 1
                return

            current = self.head
            for _ in range(position - 1):
                current = current.next
            current.next = current.next.next
            self.size -= 1
            return
        
        current = self.head
        prev = None
        while current.next != self.head:
            prev = current
            current = current.next
        if prev:
            prev.next = self.head
        self.size -= 1

    def traverse(self):
        if not self.head:
            print("Linked list is empty")
            return
        
        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head: break

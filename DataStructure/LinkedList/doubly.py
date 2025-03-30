class Node:
    def __init__(self, data: any):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
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
            self.size += 1
            return

        if toPosition:
            if position > self.size or position < 0:
                print("ERROR: Invalid position for insertion")
                return

            if position == 0:
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
                self.size += 1
                return

            current = self.head
            for _ in range(position - 1):
                current = current.next

            new_node.next = current.next
            if current.next:
                current.next.prev = new_node
            current.next = new_node
            new_node.prev = current
            self.size += 1
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current
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
                self.head = self.head.next
                if self.head:
                    self.head.prev = None
                self.size -= 1
                return

            current = self.head
            for _ in range(position - 1):
                current = current.next

            if current.next:
                current.next = current.next.next
                if current.next:
                    current.next.prev = current
                self.size -= 1
            return
        
        current = self.head
        while current.next:
            current = current.next
        if current.prev:
            current.prev.next = None
        self.size -= 1

    def traverse(self, backward: bool = False):
        if not self.head:
            print("Linked list is empty")
            return
        
        if backward:
            current = self.head
            while current.next:
                current = current.next
            while current:
                print(current.data, end=" <- " if current.prev else "\n")
                current = current.prev
            return

        current = self.head
        while current:
            print(current.data, end=" -> " if current.next else "\n")
            current = current.next

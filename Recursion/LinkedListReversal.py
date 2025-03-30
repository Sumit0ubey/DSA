class Node:
    def __init__(self, data:any):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, infoEnable:bool=True):
        self.head = None
        self.info = infoEnable
    
    def insert(self, item:any):
        if self.head is None:
            self.head = Node(item)
            if self.info: print(f"{item} added at the beginning of the list")
        else:
            current = self.head
            while current.next:
                current = current.next
            newNode = Node(item)
            current.next = newNode
            if self.info: print(f"{item} added at the end of the list")
    
    def delete(self):
        if self.head is None:
            if self.info: print("There is no element to delete.")
        else:
            current = self.head
            while current.next.next:
                current = current.next
            if self.info: print(f"{current.next.data} is deleted from the list")
            current.next = None
            
    def transverse(self):
        current = self.head
        while current:
            print(current.data, sep=" -> ", end=" ")
            current = current.next
        print()
    
    def reverseLinkedList(self, node=None):
        if node is None: node = self.head
        if node is None or node.next is None:
            self.head = node
            return node

        previous = self.reverseLinkedList(node.next)
        node.next.next = node
        node.next = None

        return previous


linkedlist = LinkedList(infoEnable=False)
linkedlist.insert(1)
linkedlist.insert(2)
linkedlist.insert(3)
linkedlist.insert(4)
linkedlist.insert(5)
linkedlist.insert(6)
linkedlist.insert(7)
linkedlist.delete()
linkedlist.transverse()

linkedlist.reverseLinkedList()
linkedlist.transverse()






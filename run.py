# from DataStructure.Array.dynamic1DArray import Array
# from DataStructure.Array.dynamic2DArray import Array
# from DataStructure.Array.oneDArray import Array
# from DataStructure.Array.twoDArray import Array
# from DataStructure.LinkedList.singly import SinglyLinkedlist
# from DataStructure.LinkedList.doubly import DoublyLinkedlist
# from DataStructure.LinkedList.circular import CicularLinkedlist
from DataStructure.LinkedList.cicularDoubly import CircularDoublyLinkedList

# array = Array()
# array.insert(65)
# array.insert(98)
# array.insert(42)
# array.delete(1)
# if array.search(42): print("Found.")
# array.traverse()
# array

# array = Array()
# array.insert(65, 0)
# array.insert(98, 1)
# array.insert(35, 0)
# array.insert(12, 1)
# array.insert(26, 0)
# array.delete(1, 1)
# if array.search(12): print("found.")
# array.update(63, 0, 1)
# array.traverse()

# array = Array(10, 0)
# array.insert(65, 0)
# array.insert(98, 1)
# array.insert(42, 2)
# array.insert("you", 3)
# array.delete(1)
# if array.search(42): print("Found.")
# array.traverse()

# array = Array(3, 3, 0)
# for i in range(3):
#     for j in range(3):
#         array.insert(2+((i+j)*3)//2,i, j)
# array.update("you", 0, 0)
# array.delete(2, 1)
# if array.search(42): print("Found.")
# array.traverse()
# array.show()

# linkedlist = SinglyLinkedlist()
# linkedlist.insert(65) # insert at beignning
# linkedlist.insert(98) # insert at end
# linkedlist.insert(42, toPosition=True, position=1) # insert at position
# linkedlist.insert(51, toPosition=True, position=2)
# linkedlist.insert(84)
# linkedlist.insert(98)
# linkedlist.delete()
# linkedlist.delete(toPosition=True, position=-2)
# linkedlist.delete(toPosition=True, position=1)
# linkedlist.traverse()

# linkedlist = DoublyLinkedlist()
# linkedlist.insert(65) # insert at beignning
# linkedlist.insert(98) # insert at end
# linkedlist.insert(42, toPosition=True, position=1) # insert at position
# linkedlist.insert(51, toPosition=True, position=2)
# linkedlist.insert(84)
# linkedlist.insert(98)
# linkedlist.delete()
# linkedlist.delete(toPosition=True, position=-2)
# linkedlist.delete(toPosition=True, position=1)
# linkedlist.traverse()
# linkedlist.traverse(backword=True)

# linkedlist = CicularLinkedlist()
# linkedlist.insert(65) # insert at beignning
# linkedlist.insert(98) # insert at end
# linkedlist.insert(42, toPosition=True, position=1) # insert at position
# linkedlist.insert(51, toPosition=True, position=2)
# linkedlist.insert(84)
# linkedlist.delete()
# linkedlist.delete(toPosition=True, position=-1)
# linkedlist.delete(toPosition=True, position=1)
# linkedlist.traverse()

linkedlist = CircularDoublyLinkedList()
linkedlist.insert(65) # insert at beignning
linkedlist.insert(98) # insert at end
linkedlist.insert(42, toPosition=True, position=1) # insert at position
linkedlist.insert(51, toPosition=True, position=2)
linkedlist.insert(84)
linkedlist.insert(98)
linkedlist.delete()
linkedlist.delete(toPosition=True, position=-2)
linkedlist.delete(toPosition=True, position=1)
linkedlist.traverse()
linkedlist.traverse(backward=True)

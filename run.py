# from DataStructures.Array.dynamic1DArray import Array
# from DataStructures.Array.dynamic2DArray import Array
# from DataStructures.Array.oneDArray import Array
# from DataStructures.Array.twoDArray import Array
# from DataStructures.LinkedList.singly import SinglyLinkedlist
# from DataStructures.LinkedList.doubly import DoublyLinkedlist
# from DataStructures.LinkedList.circular import CicularLinkedlist
# from DataStructures.LinkedList.cicularDoubly import CircularDoublyLinkedList
# from DataStructures.Stack.stackUsingArray import Stack
# from DataStructures.Stack.stackUsingLinkedlist import Stack
from DataStructures.Queue.UsingArray import queue, deque, CircularQueue, PriorityQueue

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

# linkedlist = CircularDoublyLinkedList()
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
# linkedlist.traverse(backward=True)

# stack = Stack()
# stack.push(53)
# stack.push(69)
# stack.push(32)
# stack.push(73)
# stack.pop()
# stack.pop()
# stack.peek()
# stack.isEmpty()
# stack.size()

# stack = Stack()
# stack.push(53)
# stack.push(69)
# stack.push(32)
# stack.push(73)
# stack.pop()
# stack.pop()
# stack.peek()
# stack.isEmpty()

# Queue = queue()
# Queue.enqueue(62)
# Queue.enqueue(21)
# Queue.enqueue(54)
# Queue.enqueue(74)
# Queue.dequeue()
# Queue.dequeue()
# Queue.front()
# Queue.rear()
# Queue.size()

# Queue = deque()
# Queue.enqueueFront(62)
# Queue.enqueueRear(21)
# Queue.enqueueFront(54)
# Queue.enqueueRear(74)
# Queue.dequeueFront()
# Queue.dequeueRear()
# Queue.front()
# Queue.rear()
# Queue.size()

# Queue = CircularQueue(4)
# Queue.enqueue(62)
# Queue.enqueue(21)
# Queue.enqueue(54)
# Queue.enqueue(74)
# Queue.dequeue()
# Queue.dequeue()
# Queue.front()
# Queue.rear()
# Queue.size()

Queue = PriorityQueue()
Queue.enqueue(62)
Queue.enqueue(21)
Queue.enqueue(54)
Queue.enqueue(74)
Queue.dequeue()
Queue.dequeue()
Queue.front()
Queue.rear()
Queue.size()

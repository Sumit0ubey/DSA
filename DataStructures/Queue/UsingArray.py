class queue:
    """
    A Simple Queue follows the FIFO (First In, First Out) principle, meaning the first element added is the first to be removed. It has two main operations:
        - Enqueue: Adds an element to the rear.
        - Dequeue: Removes an element from the front.

    Other operations include checking the front element, rear element, and size
    """
    def __init__(self):
        self.__queue = []
    
    def enqueue(self, data):
        """
        This method adds an element to the rear.

        Time Complexity: O(1)
        """
        self.__queue.append(data)
        print(f"{data} is enqueued in the queue")
    
    def dequeue(self):
        """
        This method removes an element from the front.

        Time Complexity: O(1)
        """
        if len(self.__queue) == 0:
            print("ERROR: Queue is Empty")
            return
        
        print(f"{self.__queue.pop(0)} is dequeued from the queue")
    
    def front(self):
        if len(self.__queue) == 0:
            print("ERROR: Queue is Empty")
            return
        
        print(f"{self.__queue[0]} is the front element of the queue")
    
    def rear(self):
        if len(self.__queue) == 0:
            print("ERROR: Queue is Empty")
            return
        
        print(f"{self.__queue[-1]} is the rear element of the queue")
    
    def size(self):
        print(f"{len(self.__queue)} is the size of the queue")


class deque:
    """
    A Deque (Double-Ended Queue) allows insertion and deletion from both the front and rear. It supports four main operations:
        - Enqueue Front: Inserts an element at the front.
        - Enqueue Rear: Inserts an element at the rear.
        - Dequeue Front: Removes an element from the front.
        - Dequeue Rear: Removes an element from the rear.

    Deques can be input-restricted (insertion at one end only) or output-restricted (deletion at one end only). They are more flexible than simple queues and can be used in scenarios like sliding window problems and caching. 
    """
    def __init__(self):
        self.__deque = []
    
    def enqueueFront(self, data):
        """
        This method adds an element at the front.

        Time Complexity: O(1)
        """
        self.__deque.insert(0, data)
        print(f"{data} is enqueued at the front of the deque")
    
    def enqueueRear(self, data):
        """
        This method adds an element at the rear.

        Time Complexity: O(1)
        """
        self.__deque.append(data)
        print(f"{data} is enqueued at the rear of the deque")
    
    def dequeueFront(self):
        """
        This method removes an element from the front.

        Time Complexity: O(1)
        """
        if len(self.__deque) == 0:
            print("ERROR: Deque is Empty")
            return
        
        print(f"{self.__deque.pop(0)} is dequeued from the deque")
    
    def dequeueRear(self):
        """
        This method removes an element from the rear.

        Time Complexity: O(1)
        """
        if len(self.__deque) == 0:
            print("ERROR: Deque is Empty")
            return
        
        print(f"{self.__deque.pop(-1)} is dequeued from the deque")
    
    def front(self):
        if len(self.__deque) == 0:
            print("ERROR: Queue is Empty")
            return
        
        print(f"{self.__deque[0]} is the front element of the deque")
    
    def rear(self):
        if len(self.__deque) == 0:
            print("ERROR: Queue is Empty")
            return
        
        print(f"{self.__deque[-1]} is the rear element of the deque")
    
    def size(self):
        print(f"{len(self.__deque)} is the size of the deque")
    

class CircularQueue:
    def __init__(self, size : int = 8):
        self.__size = size
        self.__queue = [None] * size
        self.__front = 0
        self.__rear = -1
        self.__count = 0

    def enqueue(self, data):
        if self.__count == self.__size:
            print("ERROR: Circular Queue is full")
            return
        
        self.__rear = (self.__rear + 1) % self.__size
        self.__queue[self.__rear] = data
        self.__count += 1
        print(f"{data} is enqueued in the Circular Queue")

    def dequeue(self):
        if self.__count == 0:
            print("ERROR: Circular Queue is empty")
            return
        
        print(f"{self.__queue[self.__front]} is dequeued from the Circular Queue")
        self.__queue[self.__front] = None
        self.__front = (self.__front + 1) % self.__size
        self.__count -= 1

    def front(self):
        if self.__count == 0:
            print("ERROR: Circular Queue is empty")
            return
        print(f"{self.__queue[self.__front]} is the front element")

    def rear(self):
        if self.__count == 0:
            print("ERROR: Circular Queue is empty")
            return
        print(f"{self.__queue[self.__rear]} is the rear element")

    def size(self):
        print(f"{self.__count} is the current size of the circular queue")

    
class PriorityQueue:
    def __init__(self):
        self.__queue = []
    
    def enqueue(self, data):
        self.__queue.append(data)
        self.__queue.sort(reverse=True)
        print(f"{data} is enqueued in the Priority Queue")
    
    def dequeue(self):
        if len(self.__queue) == 0:
            print("ERROR: Priority Queue is empty")
            return
        
        print(f"{self.__queue.pop(0)} is dequeued from the Priority Queue")
    
    def front(self):
        if len(self.__queue) == 0:
            print("ERROR: Priority Queue is empty")
            return
        
        print(f"{self.__queue[0]} is the front element of the priority queue")
    
    def rear(self):
        if len(self.__queue) == 0:
            print("ERROR: Priority Queue is empty")
            return
        
        print(f"{self.__queue[-1]} is the rear element of the priority queue")
    
    def size(self):
        print(f"{len(self.__queue)} is the current size of the priority queue")

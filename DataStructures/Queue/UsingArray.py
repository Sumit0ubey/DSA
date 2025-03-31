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
    """
    A Circular Queue is a linear data structure that follows the FIFO (First In, First Out) principle but connects the rear to the front, forming a circle. It prevents memory wastage by reusing empty spaces.

    It supports the following operations:
        - Enqueue: Inserts an element at the rear.
        - Dequeue: Removes an element from the front.
        - Get Front: Retrieves the front element.
        - Get Rear: Retrieves the rear element.

    When the queue reaches the end, it wraps around to utilize available space. Circular Queues are commonly used in buffering systems, scheduling algorithms, and network packet handling.
    """
    def __init__(self, size : int = 8):
        self.__size = size
        self.__queue = [None] * size
        self.__front = 0
        self.__rear = -1
        self.__count = 0

    def enqueue(self, data):
        """
        This method adds an element at the rear.

        Time Complexity: O(1)
        """
        if self.__count == self.__size:
            print("ERROR: Circular Queue is full")
            return
        
        self.__rear = (self.__rear + 1) % self.__size
        self.__queue[self.__rear] = data
        self.__count += 1
        print(f"{data} is enqueued in the Circular Queue")

    def dequeue(self):
        """
        This method removes an element from the front.

        Time Complexity: O(1)
        """
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
    """
    A Priority Queue is a special type of queue where elements are dequeued based on priority rather than the order of insertion. Each element has an associated priority, and elements with higher priority are served first.

    It supports the following operations:
        - Enqueue: Inserts an element with a priority.
        - Dequeue: Removes the element with the highest priority.
        - Peek: Retrieves the highest-priority element without removing it.

    Priority Queues can be implemented using arrays, linked lists, or heaps (min-heap or max-heap). They are widely used in scheduling systems, Dijkstra’s algorithm, and event-driven simulations.
    """
    def __init__(self):
        self.__queue = []
    
    def enqueue(self, data):
        """
        This method removes an element from the front.

        Time Complexity: O(1)
        """
        self.__queue.append(data)
        self.__queue.sort(reverse=True)
        print(f"{data} is enqueued in the Priority Queue")
    
    def dequeue(self):
        """
        This method removes an element from the front.

        Time Complexity: O(1)
        """
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

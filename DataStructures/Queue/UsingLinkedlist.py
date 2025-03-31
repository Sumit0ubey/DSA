class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class queue:
    """
    A Simple Queue follows the FIFO (First In, First Out) principle, meaning the first element added is the first to be removed. It has two main operations:
        - Enqueue: Adds an element to the rear.
        - Dequeue: Removes an element from the front.

    Other operations include checking the front element, rear element, and size
    """
    def __init__(self):
        self.__front = self.__rear = None
        self.__size = 0
    
    def enqueue(self, data):
        """
        This method adds an element to the rear.

        Time Complexity: O(1)
        """
        new_node = Node(data)
        if self.__front is None:
            self.__front = self.__rear = new_node
            print(f"{data} is equeued in the queue")
            self.__size += 1
            return
        
        self.__rear.next = new_node
        self.__rear = new_node
        self.__size += 1
        print(f"{data} is equeued in the queue")
    
    def dequeue(self):
        """
        This method removes an element from the front.

        Time Complexity: O(1)
        """
        if self.__front is None:
            print("ERROR: Queue is empty")
            return
        
        temp = self.__front
        self.__front = self.__front.next
        self.__size -= 1
        print(f"{temp.data} is dequeued from the queue")
    
    def front(self):
        if self.__front is None:
            print("ERROR: Queue is empty")
            return None
        
        print(f"{self.__front.data} is the front element of the queue")
    
    def rear(self):
        if self.__rear is None:
            print("ERROR: Queue is empty")
            return None
        
        print(f"{self.__rear.data} is the rear element of the queue")
    
    def size(self):
        print(f"Size of the queue is {self.__size}")


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
        self.__front = self.__rear = None
        self.__size = 0
    
    def enqueueFront(self, data):
        """
        This method adds an element at the front.

        Time Complexity: O(1)
        """
        new_node = Node(data)
        if self.__front is None:
            self.__front = self.__rear = new_node
            print(f"{data} is equeued in the deque")
            self.__size += 1
            return
        
        new_node.next = self.__front
        self.__front = new_node
        self.__size += 1
        print(f"{data} is equeued in the deque")
    
    def enqueueRear(self, data):
        """
        This method adds an element at the rear.

        Time Complexity: O(1)
        """
        new_node = Node(data)
        if self.__front is None:
            self.__front = self.__rear = new_node
            print(f"{data} is equeued in the deque")
            self.__size += 1
            return
        
        self.__rear.next = new_node
        self.__rear = new_node
        self.__size += 1
        print(f"{data} is equeued in the deque")
    
    def dequeueFront(self):
        """
        This method removes an element from the front.

        Time Complexity: O(1)
        """
        if self.__front is None:
            print("ERROR: Deque is empty")
            return None
        
        temp = self.__front.data
        self.__front = self.__front.next
        self.__size -= 1
        print(f"{temp} is dequeued from the deque")
    
    def dequeueRear(self):
        """
        This method removes an element from the rear.

        Time Complexity: O(n)
        """
        if self.__rear is None:
            print("ERROR: Deque is empty")
            return None
        
        current = self.__front
        while current.next.next:
            current = current.next
        temp = current.next.data
        current.next = None
        self.__rear = current
        self.__size -= 1
        print(f"{temp} is dequeued from the deque")
    
    def front(self):
        if self.__front is None:
            print("ERROR: Deque is empty")
            return None
        print(f"{self.__front.data} is the front element of the deque")
    
    def rear(self):
        if self.__rear is None:
            print("ERROR: Deque is empty")
        print(f"{self.__rear.data} is the rear element of the deque")
    
    def size(self):
        print(f"Size of the deque is {self.__size}")


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
    def __init__(self):
        self.__front = self.__rear = None
        self.__size = 0
    
    def enqueue(self, data):
        """
        This method adds an element at the rear.

        Time Complexity: O(1)
        """
        new_node = Node(data)
        if self.__front is None:
            self.__front = self.__rear = new_node
            self.__rear.next = self.__front
            self.__size += 1
            print(f"{data} is enqueued in the Cicular queue")
            return
        
        self.__rear.next = new_node
        self.__rear = new_node
        self.__rear.next = self.__front
        self.__size += 1
        print(f"{data} is enqueued in the Cicular queue")
    
    def dequeue(self):
        """
        This method removes an element from the front.

        Time Complexity: O(1)
        """
        if self.__front is None:
            print("ERROR: Circular queue is empty")
            return None
        
        data = self.__front.data

        if self.__front != self.__rear:
            self.__front = self.__front.next
            self.__rear.next = self.__front
        else:
            self.__front = self.__rear = None
        self.__size -= 1

        print(f"{data} is dequeued from the Circular queue")
    
    def front(self):
        if self.__front is None:
            print("ERROR: Circular queue is empty")
            return
        print(f"{self.__front.data} is the front element of the Circular queue")
    
    def rear(self):
        if self.__rear is None:
            print("ERROR: Circular queue is empty")
            return
        print(f"{self.__rear.data} is the rear element of the Circular queue")
    
    def size(self):
        print(f"Size of the Circular queue is {self.__size}")


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
        self.__front = self.__rear = None
        self.__size = 0
    
    def enqueue(self, data):
        """
        This method removes an element from the front.

        Time Complexity: O(1)
        """
        new_node = Node(data)
        if self.__front is None:
            self.__front = self.__rear = new_node
            print(f"{data} is equeued in the queue")
            self.__size += 1
            return
        
        self.__rear.next = new_node
        self.__rear = new_node
        self.__size += 1
        print(f"{data} is equeued in the queue")
    
    def dequeue(self):
        """
        This method removes an element from the front.

        Time Complexity: O(1)
        """
        if self.__front is None:
            print("ERROR: Queue is empty")
            return
        
        temp = self.__front
        self.__front = self.__front.next
        self.__size -= 1
        print(f"{temp.data} is dequeued from the queue")
    
    def front(self):
        if self.__front is None:
            print("ERROR: Queue is empty")
            return None
        
        print(f"{self.__front.data} is the front element of the queue")
    
    def rear(self):
        if self.__rear is None:
            print("ERROR: Queue is empty")
            return None
        
        print(f"{self.__rear.data} is the rear element of the queue")
    
    def size(self):
        print(f"Size of the queue is {self.__size}")


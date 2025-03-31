class Stack:
    def __init__(self):
        """
        Stack works on LIFO (last in first out) principle
        """
        self.data = []

    def push(self, data:any):
        """
        push adds the data at the top of the stack

        Time Complexity: O(1)
        """
        self.data.append(data)
        print(f"{data} added in the stack")
    
    def pop(self):
        """
        pop removes the data from the top of the stack

        Time Complexity: O(1)
        """
        print(f"{self.data.pop(-1)} removed from the stack")
    
    def peek(self):
        """
        peek returns the top element of the stack

        Time Complexity: O(1)
        """
        print(f"{self.data[-1] } is on the top in the stack")
    
    def isEmpty(self):
        print(len(self.data) == 0)

    def size(self):
        print(f"Size of the stack is {len(self.data)}")

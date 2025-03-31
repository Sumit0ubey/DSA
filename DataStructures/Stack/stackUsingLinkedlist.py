class Node:
    def __init__(self, data:any):
        self.data:any = data
        self.next = None

class Stack:
    def __init__(self):
        self.top:Node = None
        self.size:int = 0
    
    def push(self, data:any):
        new_node = Node(data)
        if self.top is None: self.top = new_node 
        else:
            new_node.next = self.top 
            self.top = new_node
        
        self.size += 1
        print(f"{data} is pushed to the stack")
    
    def pop(self):
        if self.top is None:
            print("ERROR: Stack is empty")
            return

        pop_node = self.top
        self.top = self.top.next
        self.size -= 1

        print(f"{pop_node.data} is poped from the stack")
    
    def peek(self):
        if self.top is None:
            print("ERROR: Stack is empty")
            return

        print(f"{self.top.data} is the top element of the stack")

    def isEmpty(self):
        print("Stack is not empty") if self.size != 0 else print("Stack is Empty")
    
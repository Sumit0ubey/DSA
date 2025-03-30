# implementing Stack with insertion and deletion.

class Stack:
    def __init__(self) -> None:
        self.stack = []
    
    def count(self):
        return len(self.stack)

    def push(self, data):
        self.stack.append(data)
    
    def pop(self):
        if self.count() != 0:
            self.stack.pop()
        else:
            print("Stack Under-Flow")
    
    def display(self):
        if self.count() != 0:
            for item in self.stack:
                print(item, end=' ')
            print()
        else:
            print("There is no element in Stack")
    
numbers = Stack()

numbers.push(5)
numbers.push(45)
numbers.push(10)
numbers.push(13)

numbers.display()
numbers.pop()
numbers.display()

print(numbers.count())

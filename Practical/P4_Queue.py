# Inplemention of queue with insertion, deletion, etc.

class Queue:

    def __init__(self) -> None:
        self.queue = []

    def size(self):
        return len(self.queue)

    def enqueue(self, data):
        self.queue.append(data)
    
    def dequeue(self):
        self.queue.pop(0)
    
    def peek(self):
        return self.queue[-1]
    
    def display(self):
        for item in self.queue:
            print(item, end=', ')
        print()
    

student_for_admission = Queue()

student_for_admission.enqueue('Rag')
student_for_admission.enqueue('raghav')
student_for_admission.enqueue('rajiv')

student_for_admission.display()
print(student_for_admission.size())
student_for_admission.dequeue()

student_for_admission.display()
print(student_for_admission.peek())
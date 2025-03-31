class Array:
    def __init__(self, capacity:int, dataType:any):
        self.type:any = dataType
        self.capacity:int = capacity
        self.data = [None] * capacity
        self.size:int = 0
    
    def insert(self, data:any, index:int):
        if index > self.size or self.size > self.capacity: 
            print("ERROR: Index out of range") 
            return
        if type(self.type) != type(data): 
            print("ERROR: Data Type Mis-Match")
            return
        for i in range(self.size, index, -1): self.data[i] = self.data[i-1]
        self.data[index] = data
        self.size += 1
        print(f"{data} inserted in Array.")
    
    def delete(self, index:int):
        if index > self.size: 
            print("ERROR: Index out of range") 
            return
        for i in range(index, self.size - 1): self.data[i] = self.data[i+1]
        self.data[self.size - 1] = None
        self.size -= 1
        print(f"Element at index {index} deleted from Array.")
    
    def update(self, data:any, index:int):
        if index > self.size or self.size > self.capacity: 
            print("ERROR: Index out of range") 
            return
        if type(self.type) != type(data): 
            print("ERROR: Data Type Mis-Match")
            return
        self.data[index] = data
        print(f"Updated {data[index]} to {data}")
    
    def search(self, data:any):
        if data in self.data: return True
        return False
    
    def traverse(self):
        print("[", end="")
        for i in range(self.size):
            if i+1 == self.size: 
                print(self.data[i], end=" ")
            else:
                print(self.data[i], end=", ")
        print("]")
        
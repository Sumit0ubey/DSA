class Array:
    def __init__(self):
        self.data:list = []
    
    def insert(self, data:any):
        self.data.append(data)
        print(f"{data} inserted in Array.")
    
    def delete(self, index:int):
        self.data.pop(index)
        print(f"Element at index {index} deleted from Array.")
    
    def search(self, data:any) -> bool:
        if data in self.data: return True
        return False
    
    def traverse(self):
        print(self.data)
    
    def __str__(self):
        print(self.data)
class Array:
    def __init__(self):
        self.data:list = [[] for _ in range(2)]
    
    def insert(self, data:any, row:int):
        self.data[row].append(data)
        print(f"{data} inserted in Array.")
    
    def delete(self, rowIndex:int, colIndex:int):
        self.data[rowIndex].pop(colIndex)
        print(f"Element from row:{rowIndex} col:{colIndex} is removed.")
    
    def update(self, data:any, row:int, col:int):
        print(f"updated {self.data[row][col]} to {data}.")
        self.data[row][col] = data
    
    def traverse(self):
        print(self.data)
    
    def search(self, data:any):
        if data in self.data: return True
        return False

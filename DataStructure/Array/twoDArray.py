class Array:
    def __init__(self, rows, cols, dataType:any):
        self.type = dataType
        self.rows = rows
        self.cols = cols
        self.data = [[None for _ in range(cols)] for _ in range(rows)]
    
    def insert(self, data:any, row:int, col:int):
        if (row < 0 or row > self.rows) or (col < 0 or col > self.cols):
            print("ERROR: Index out of range")
            return
        if type(self.type) != type(data):
            print("ERROR: Type Mis-Match")
            return
        self.data[row][col] = data
        print(f"{data} added in the Array")
    
    def delete(self, row:int, col:int):
        if (row < 0 or row > self.rows) or (col < 0 or col > self.cols):
            print("ERROR: Index out of range")
            return
        self.data[row][col] = None
        print(f"Element is removed from row:{row} col:{col}")
    
    def update(self, data:any, row:int, col:int):
        if (row < 0 or row > self.rows) or (col < 0 or col > self.cols):
            print("ERROR: Index out of range")
            return
        if type(self.type) != type(data):
            print("ERROR: Type Mis-Match")
            return
        print(f"{self.data[row][col]} updated to {data}")
        self.data[row][col] = data

    def search(self, data:any):
        if data in self.data: return True
        return False
    
    def traverse(self):
        print("[")
        for i in range(self.rows):
            print(" "*4+"[", end="")
            for j in range(self.cols):
                if self.data[i][j] != None: print(self.data[i][j], end=" ")
            print("]")
        print("]")
    
    def show(self):
        print("[")
        for i in range(self.rows):
            print(" "*4+"[", end="")
            for j in range(self.cols):
                print(self.data[i][j], end=" ")
            print("]")
        print("]")
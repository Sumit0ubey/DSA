class Hash:
    def __init__(self, size : int = 10):
        self.__size = size
        self.__hash = [[] for _ in range(size)]
    
    def __hashFunction(self, key):
        return hash(key) % self.__size
    
    def set(self, key, value):
        index = self.__hashFunction(key)
        self.__hash[index].append([key, value])
        print(f"Data added in hash with id: {key} - value: {value}")
    
    def put(self, key, value):
        index = self.__hashFunction(key)
        for pair in self.__hash[index]:
            if pair[0] == key:
                pair[1] = value
                print(f"Updated the value of key: {key} to value: {value}")
                return

    def get(self, key):
        index = self.__hashFunction(key)
        for pair in self.__hash[index]:
            if pair[0] == key:
                print(f"Value of key: {key} is {pair[1]}")
                return
    
    def delete(self, key):
        index = self.__hashFunction(key)
        for i, pair in enumerate(self.__hash[index]):
            if pair[0] == key:
                print(f"Deleted value: {pair[1]} with key: {key} from the hash")
                del self.__hash[index][i]
                return
    

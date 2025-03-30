def linearSearch(data:list, find) -> int:
    length = len(data)
    for i in range(length):
        if data[i] == find:
            return i
    else:
        return -1


items = [45, 78, 12, 69, 10, 84]
tofind = int(input("What to find: "))

result = linearSearch(items, tofind)
if result != -1:
    print("Found at index", result)
else:
    print("Not found")

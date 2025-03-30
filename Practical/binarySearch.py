def binarySearch(data:list, find, start:int = 0, mid:int = 0, end:int = 0) -> int:
    """
    Passed data should be sorted for proper working of binary search algorithm.
    There is no need to provide start, mid, end values
    """

    if end == 0: end = len(data)
    if end >= start:
        mid = (start + end) // 2
        if data[mid] == find:
            return mid
        elif data[mid] < find:
            return binarySearch(data=data, find=find, start=mid+1)
        else:
            return binarySearch(data=data, find=find, end=mid-1)
    else:
        return -1

items = [45, 98, 12, 47, 32, 9, 54, 76]
toFind = int(input("What to find: "))

result = binarySearch(sorted(items), toFind)
if result != -1:
    print("Found at index", result)
else:
    print("Not found")
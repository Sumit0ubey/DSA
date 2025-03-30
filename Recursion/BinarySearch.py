
def binarySearch(data:int, target:int, right:int=0, left:int=0) -> int:
    if right == 0: right = len(data)
    if left > right: return -1
    mid = (left + right) // 2
    if data[mid] == target:
        return mid
    elif data[mid] > target:
        return binarySearch(data=data, target=target, left=left, right=mid-1)
    else:
        return binarySearch(data=data, target=target, left=mid+1, right=right)

print(binarySearch([5, 7, 9, 11, 15, 17, 19, 23, 27], 17))
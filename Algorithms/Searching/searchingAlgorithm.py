def linearSearch(data:list, target:any) -> int:
    """
    Searches for the target in the given data list using linear search algorithm.
    Returns index of the target in the array/list if found else -1.

    Time Complexity: O(n)
    """
    for i in range(len(data)):
        if data[i] == target:
            return i
    return -1

def binarySearch(data:list, target:any) -> int:
    """
    Searches for the target in the given data list using binary search algorithm.
    Returns index of the target in the array/list if found else -1.
    This function assumes the input list is sorted in ascending order.

    Time Complexity: O(log n)
    
    """
    left, right = 0, len(data) - 1
    while left <= right:
        mid = (left + right) // 2
        if data[mid] == target: return mid
        elif data[mid] < target: left = mid + 1
        else: right = mid - 1
    return -1

def interpolationSearch(data:list, target:any) -> int:
    """
    Searches for the target in the given data list using interpolation search algorithm.
    Returns index of the target in the array/list if found else -1.

    Time complexity: O(log log n)
    """
    left, right = 0, len(data) - 1
    while left <= right and data[left] <= target <= data[right]:
        pos = int(left + ((target - data[left])*(right - left)/(data[right] - data[left])))
        if data[pos] == target: return pos
        elif data[pos] < target: left = pos + 1
        else: right = pos - 1
    return -1

def jumpSearch(data:list, target:any) -> int:
    """
    Searches for the target in the given data list using jump search algorithm.
    Returns index of the target in the array/list if found else -1.
    This function assumes the input list is sorted in ascending order.

    Time Complexity: O(√n)
    """
    prev, length = 0, len(data) - 1
    step = int(length ** 0.5)

    while prev < length and data[min(step, length) - 1] < target:
        prev = step
        step += int(length ** 0.5)
        if prev >= length: return -1
    
    for i in range(prev, min(step, length)):
        if data[i] == target: return i
    return -1

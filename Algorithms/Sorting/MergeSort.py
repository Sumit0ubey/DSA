def merge(leftArray:list, rightArray:list, Array:list):
    leftSize:int = len(Array) // 2
    rightSize:int = len(Array) - leftSize
    i, l, r = 0

    while(l < leftSize and r < rightSize):
        if (leftArray[l] < rightArray[r]):
            Array[i] = leftArray[i]
            i += 1
            l += 1
        else:
            Array[i] = rightArray[r]
            i += 1
            r += 1
    while (l < leftSize):
        Array[i] = leftArray[l]
        i += 1
        l += 1

    while (r < rightSize):
        Array[i] = rightArray[r]
        i += 1 
        r += 1


def MergeSort(Array:list) -> list:
    """
    Merge Sort is a sorting algorithm that sorts an array in ascending or descenting order.

    Parameters:
        Array: Takes list as a input.
        Descending: Takes boolean input, tells in which order does array will be sorted.
            Defaultly sorts in ascending order.
            set Descending=True to sort in descending order.
        Return: 
            Returns a List in sorted order.

    Alogithm_Complexity:
        Time complexity: O(n log n)
        Space complexity: O(n)
    
    Working:
        1. Go through the array, one value at a time.
        2. For each value, compare the value with the next value.
        3. If the value is higher than the next one, swap the values so that the highest value comes last.

    """
    length:int = len(Array)
    if length <= 1: return;
    leftArray:list
    rigthArray:list
    middle:int = length // 2;
    j = 0
    for i in range(length):
        if(i < middle):
            leftArray[i] = Array[i]
        else:
            rigthArray[j] = Array[j]
            j += 1
    MergeSort(leftArray)
    MergeSort(rigthArray)
    merge(leftArray, rigthArray, Array)
    return Array

array = [45, 64, 2, 68, 12, 3]
print(MergeSort(array))
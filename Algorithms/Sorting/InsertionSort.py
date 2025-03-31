def InsertionSort(Array:list) -> list:
    """
    Insertion Sort is a sorting algorithm that sorts an array in ascending order.

    Parameters:
        Array: Takes list as a input. 
        Return: Returns a List in sorted order.

    Alogithm_Complexity:
        Time complexity: O(n^2)
        Space complexity: O(1)
    
    Working:
        1. Take the first value from the unsorted part of the array.
        2. Move the value into the correct place in the sorted part of the array.
        3. Go through the unsorted part of the array again as many times as there are values.

    """
    length = len(Array)
    for i in range(1, length):
        Currentvalue = Array[i]
        j:int = i - 1
        while(j >= 0 and Array[j] > Currentvalue):
            Array[j + 1] = Array[j]
            j -= 1
        Array[j+1] = Currentvalue
    return Array

Array = [85, 12, 3, 65, 45, 2, 8]
print(InsertionSort(Array))
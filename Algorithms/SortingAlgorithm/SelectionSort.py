def SelectionSort(Array:list) -> list:

    """
    Selection Sort is a sorting algorithm that finds the lowest value in an array and moves it to the front of the array.

    Parameters:
        Array: Takes list as a input.
        Return: Returns a List in sorted order.

    Alogithm_Complexity:
        Time complexity: O(n^2)
        Space complexity: O(1)
    
    Working:
        1. Go through the array to find the lowest value.
        2. Move the lowest value to the front of the unsorted part of the array.
        3. Go through the array as many times as there are values in the array.

    """
    length:int = len(Array)

    for i in range(length - 1):
        min_:int = i
        for j in range(i + 1, length):
            if Array[j] < Array[min_]:
                min_ = j
        Array[i], Array[min_] = Array[min_], Array[i]
    return Array

Array:list = [45, 32, 14, 2, 78, 96, 1]

print("Original Array: ", Array)
print("Selection Sorted Array: ", SelectionSort(Array))

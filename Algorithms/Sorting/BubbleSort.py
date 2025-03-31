def BubbleSort(Array:list, Descending:bool=False) -> list:
    """
    Bubble Sort is a sorting algorithm that sorts an array in ascending or descenting order.

    Parameters:
        Array: Takes list as a input.
        Descending: Takes boolean input, tells in which order does array will be sorted.
            Defaultly sorts in ascending order.
            set Descending=True to sort in descending order.
        Return: 
            Returns a List in sorted order.

    Alogithm_Complexity:
        Time complexity: O(n^2)
        Space complexity: O(1)
    
    Working:
        1. Go through the array, one value at a time.
        2. For each value, compare the value with the next value.
        3. If the value is higher than the next one, swap the values so that the highest value comes last.

    """

    length:int = len(Array)

    if Descending != True:
        for i in range(length-1):
            for j in range(length-i-1):
                if Array[j] > Array[j+1]:
                    Array[j], Array[j+1] = Array[j+1], Array[j]
    else:
        for i in range(length-1):
            for j in range(length-i-1):
                if Array[j] < Array[j+1]:
                    Array[j], Array[j+1] = Array[j+1], Array[j]

    return Array


Array:list = [45, 87, 12, 3, 62, 1, 4, 25]
print("Original Array: ", Array)
print("Bubble Sorted Array: ", BubbleSort(Array))
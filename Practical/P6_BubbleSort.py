def bubble_sort(Array):
    length = len(arr)
    for i in range(length):
        for j in range(0, length-i-1):
            if Array[j] > Array[j+1]:
                Array[j], Array[j+1] = Array[j+1], Array[j]


arr = [64, 34, 25, 12, 22, 11, 90]
print("Original array:", arr)
    
bubble_sort(arr)
print("Sorted array:", arr)

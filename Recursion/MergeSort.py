def merge(data:list, start:int, mid:int, end:int) -> None:
    temp:list = [0]*(end-start + 1)
    i, j, k = start, mid+1, 0
    while i <= mid and j <= end:
        if data[i] <= data[j]:
            temp[k] = data[i]
            i += 1
            k += 1
        else:
            temp[k] = data[j]
            k += 1
            j += 1
    
    while i <= mid:
        temp[k] = data[i]
        i += 1
        k += 1
    
    while j <= end:
        temp[k] = data[j]
        j += 1
        k += 1
    
    for m in range(start, end+1):
        data[m] = temp[m-start]


def mergeSort(data:list, start:int=0, end:int=None) -> list:
    if end is None: end = len(data) - 1
    if (start < end):
        mid:int = (start + end) // 2
        mergeSort(data, start, mid)
        mergeSort(data, mid+1, end)
        merge(data, start, mid, end)
    return data

print(mergeSort([5, 2, 8, 4, 63, 4]))

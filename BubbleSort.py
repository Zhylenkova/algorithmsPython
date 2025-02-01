def BubbleSort(arr):
    length = len(arr)

    for i in range(length):
        for j in range(0, length-i-1):
            if arr[j]> arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

print(BubbleSort([2,1,5,3,7,6]))
        

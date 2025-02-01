def SelectionSort(array, size):
    for s in range(size):
        min_index = s

        for i in range(s+1,size):
            if array[i] < array[min_index]:
                min_index = i
        
        (array[s], array[min_index]) = (array[min_index], array[s])

data = [7,2,4,8,6,9]
size = len(data)
SelectionSort(data, size)

print(data)
# return array of 2 indexes that meet a target 

def find(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            start = i
            while i+1 < len(arr) and arr[i+1] == target:
                i +=1 
            return [start, i]
    return [-1, -1]


# using binary search for finding the first index

 
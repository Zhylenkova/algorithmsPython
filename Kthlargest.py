def kth_largest(arr,k):
    for i in range(k-1):
        arr.remove(max(arr))
    return max(arr)


def kth_largest_sorted(arr, k):
    n = len(arr)
    arr.sort()
    return arr[n-k]


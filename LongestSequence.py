def Longest(nums):
    numSet = set(nums)
    sequence = 0

    for n in nums:
        #check if the start
        if(n-1) not in numSet:
            length = 0
            while (n+length) in numSet:
                length += 1
            sequence = max(length, sequence)
    return sequence

def TwoSums(nums, target):
   for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return ([i,j])
            

print(TwoSums([2,3,4], 5))
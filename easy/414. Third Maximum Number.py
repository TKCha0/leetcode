nums = [-1,2,3]
nums = list(set(nums))
nums.sort()
if len(nums) < 3:
    return max(nums)
else:
    return nums[-3]
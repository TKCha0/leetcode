nums = [1,3,5,6]
target = 7
if target in nums:
    print(nums.index(target))
else:
    for i in nums:
        if target > max(nums):
            print(len(nums))
            break
        elif target < min(nums):
            print(0)
            break
        elif i > target:
            print(nums.index(i))
            break
    
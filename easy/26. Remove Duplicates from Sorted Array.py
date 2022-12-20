nums = [1,1,2,3,4]
for i in nums:
    if nums.count(i) != 1:
        for j in range(nums.count(i)-1):
            nums.remove(i)
print(len(nums))
print(nums)



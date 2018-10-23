def twoSum(nums,target):
	for i in range(len(nums)):
		left = target - nums[i]
		if left in nums:
			if nums.index(left) == i:#if nums=[3,3] target=6,then nums.index(left) may return 0,but 1 is true
				continue
			return[i,nums.index(left)]

nums = [2,7,11,15]
target = 26
result = twoSum(nums, target)
print(result)
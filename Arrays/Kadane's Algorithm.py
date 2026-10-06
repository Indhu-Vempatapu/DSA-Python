#Maximum Subarray Sum - Kadane's Algorithm
nums = list(map(int, input().split()))
curr_sum = nums[0]
max_sum = nums[0]
for i in range(1, len(nums)):
  curr_sum = max(nums[i], nums[i]+curr_sum)
  max_sum = max(max_sum, curr_sum)
print(max_sum)

#Example 
#Input: [-2 1 -3 4 -1 2 1 -5 4] 
#Output: 6 

#Input: [5,4,-1,7,8]
#Output: 23

#Input: [-5,-1,-8,-9]
#Output: -1

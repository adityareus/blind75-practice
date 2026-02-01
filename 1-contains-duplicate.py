#Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.
#Example 1:
#Input: nums = [1, 2, 3, 3]
#Output: true
#Example 2:
#Input: nums = [1, 2, 3, 4]
#Output: false

#Approach 1:
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        nums.sort()

        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False
    
#Approach 2:
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        result = {}
        for num in nums:
            if num in result:
                result[num] += 1
            else:
                result[num] = 1

        for j in list(result.values()):
            if j > 1:
                return True
        return False
       

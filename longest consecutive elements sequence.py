#Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence. You must write an algorithm that runs in O(n) time.

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        count = 1 # 1 is the minimum value
        max_count = 1 # 1 is the minimum value
        if len(nums) == 0: # if the list is empty
            return 0 # return 0
        for i in range(1,len(nums)): # loop through the list
            if nums[i] == nums[i-1]+1: # if the current number is equal to the previous number + 1
                count += 1 # increment the count
            elif nums[i] == nums[i-1]: # if the current number is equal to the previous number
                continue # continue
            else:
                max_count = max(max_count,count) # update the max_count
                count = 1 # reset the count
        return max(max_count,count) # return the max_count



 

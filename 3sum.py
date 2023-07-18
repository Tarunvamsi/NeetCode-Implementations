#Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

#Notice that the solution set must not contain duplicate triplets.



class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #using pointers'
        nums.sort()
        res = []
        for i in range(len(nums)-2):                                    #we need to have 3 elements
            if i == 0 or nums[i] != nums[i-1]:                          #to avoid duplicates
                left = i+1                                              #left pointer
                right = len(nums)-1                                     #right pointer
                while left < right:                                     # we need to make sure that left pointer is less than right pointer
                    total = nums[i] + nums[left] + nums[right]          #total sum
                    if total == 0:
                        res.append([nums[i],nums[left],nums[right]])
                        while left < right and nums[left] == nums[left+1]: #to avoid duplicates
                            left += 1                                   #move left pointer
                        while left < right and nums[right] == nums[right-1]:  #to avoid duplicates
                            right -=1                                   #move right pointer
                        left += 1
                        right -= 1
                    elif total > 0:                                     #if total is greater than 0, we need to decrease the right pointer
                        right -= 1                                      #move right pointer
                    else:                                               #if total is less than 0, we need to increase the left pointer
                        left += 1                                       #move left pointer
        return res

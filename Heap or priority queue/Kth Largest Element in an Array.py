'''Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

 '''

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)                       #sorts the list nums in descending order. 
        return nums[k-1]                              #returns the element at index k-1 from the sorted list.

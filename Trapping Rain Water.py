#Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 
 class Solution:
    def trap(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        leftmax=height[left]
        rightmax=height[right]
        res=0
        while left<right:
            if leftmax<rightmax:
                left+=1
                leftmax=max(leftmax, height[left])   #update leftmax
                res=res+(leftmax-height[left])       #add the difference between leftmax and height[left] to res
            else:
                right-=1  
                rightmax=max(rightmax, height[right]) #update rightmax
                res = res+(rightmax-height[right])    #add the difference between rightmax and height[right] to res
        return res        



        

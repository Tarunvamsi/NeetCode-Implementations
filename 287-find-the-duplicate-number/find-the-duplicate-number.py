class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        
        while True:
            slow = nums[slow]           # Move slow one step
            fast = nums[nums[fast]]     # Move fast two steps
            
            # If they meet, it indicates a cycle
            if slow == fast:
                break
        
        # Step 2: Find the entrance to the cycle (the repeated number)
        slow2 = 0
        while True:
            slow = nums[slow]       # Move slow one step
            slow2 = nums[slow2]     # Move slow2 one step
            
            if slow == slow2:
                return slow

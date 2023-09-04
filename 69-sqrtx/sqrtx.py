class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        left, right = 1, x // 2  # Initialize the search range
        while left <= right:
            mid = left + (right - left) // 2  # Calculate the middle point
            if mid * mid == x:
                return mid
            elif mid * mid > x:
                right = mid - 1
            # If mid^2 is less than x, move the left boundary to mid+1
            else:
                left = mid + 1
        return right

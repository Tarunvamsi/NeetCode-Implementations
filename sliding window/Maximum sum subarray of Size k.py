'''Given an array of positive integers, and a positive number k, find the maximum sum of any contiguous subarray of size k.

Input: [3, 5, 2, 1, 7], k=2
Output: 8'''

def getMaxSum(arr, k):
    maxSum = 0
    windowSum = 0
    start = 0
    
    for i in range(len(arr)):
        windowSum += arr[i]
        
        if ((i - start + 1) == k):
            maxSum = max(maxSum, windowSum)
            windowSum -= arr[start]
            start += 1
    
    return maxSum

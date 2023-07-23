'''Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.'''
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:  
        stack = []                                                                # store the index of the bar
        max_area = 0                                                              # store the max area

        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:                      # if the current bar is lower than the bar in the stack
                height = heights[stack.pop()]                                     # pop the bar in the stack                   
                width = i if not stack else i - stack[-1] - 1                     # calculate the width
                max_area = max(max_area, height * width)                          #

            stack.append(i)                                                       # push the current bar into the stack
            
        while stack:
            height = heights[stack.pop()]                                         # pop the bar in the stack
            width = len(heights) if not stack else len(heights) - stack[-1] - 1   # calculate the width
            max_area = max(max_area, height * width)                             # calculate the max area

        return max_area                                                           # return the max area

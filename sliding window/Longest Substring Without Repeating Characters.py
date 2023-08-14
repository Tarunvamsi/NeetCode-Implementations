'''
Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.'''



class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()                                       # Set to store characters in the current substring
        l = 0                                                 # Left pointer of the sliding window
        res = 0                                               # Length of the longest substring without repeating characters

        for r in range(len(s)):                               # Right pointer of the sliding window
            while s[r] in charSet:
                                                              # If the character at position 'r' is already in the set,
                                                              # remove the character at position 'l' from the set and move the left pointer 'l' one step ahead.
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])                                 # Add the character at position 'r' to the set
            res = max(res, r - l + 1)                         # Update the maximum length of substring without repeating characters
        return res                                            # Return the length of the longest substring without repeating characters

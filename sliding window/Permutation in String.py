'''Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.'''


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:           # Calculate the length of the sliding window (s1's length)
        window = len(s1)
        rev = s1[::-1]
        
        if len(s2) < window:
            return False
        
        s1_count = [0] * 26       # Initialize frequency arrays for characters in s1 and the current window of s2
        s2_count = [0] * 26
        
        for i in range(window):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1
        
        if s1_count == s2_count:
            return True
        
        for i in range(window, len(s2)):
            s2_count[ord(s2[i - window]) - ord('a')] -= 1
            s2_count[ord(s2[i]) - ord('a')] += 1
            if s1_count == s2_count:
                return True
        
        return False

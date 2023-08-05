#Given a string s, find the length of the longest substring without repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest=0
        if len(s)==0:
            return 0
        if len(s)==1:
            return 1
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                if(len(set(s[i:j]))==len(s[i:j])):
                    longest = max(longest, len(s[i:j]))
     
        return longest 
     
        '''charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res'''
           
        

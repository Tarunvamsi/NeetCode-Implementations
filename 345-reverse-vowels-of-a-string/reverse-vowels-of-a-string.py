class Solution(object):
    def reverseVowels(self, s):
        s = list(s)
        left = 0
        right = len(s) - 1
        
        while left < right:
            while left < right and s[left].lower() not in {'a', 'e', 'i', 'o', 'u'}:
                left += 1
            while left < right and s[right].lower() not in {'a', 'e', 'i', 'o', 'u'}:
                right -= 1
                
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        return ''.join(s)

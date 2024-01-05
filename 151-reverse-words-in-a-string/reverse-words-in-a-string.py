class Solution(object):
    def reverseWords(self, s):
        reversed_string = ' '.join(reversed(s.split()))
        return reversed_string
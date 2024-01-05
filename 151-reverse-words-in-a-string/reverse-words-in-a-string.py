class Solution(object):
    def reverseWords(self, s):
        words = s.split()
        reversed_string = ' '.join(reversed(words))
        return reversed_string

# class Solution(object):
#     def reverseWords(self, s):
#         def reverse_word(word):
#             return word[::-1]

#         def reverse_string(string):
#             reversed_str = ""
#             for char in string:
#                 reversed_str = char + reversed_str
#             return reversed_str

#         words = []
#         start = 0
#         for end in range(len(s)):
#             if s[end] == ' ':
#                 if start < end:
#                     words.append(reverse_word(s[start:end]))
#                 start = end + 1

#         if start < len(s):
#             words.append(reverse_word(s[start:]))

#         reversed_string = reverse_string(' '.join(words))
#         return reversed_string




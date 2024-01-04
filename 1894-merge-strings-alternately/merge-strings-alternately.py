class Solution(object):
    def mergeAlternately(self, word1, word2):
        merged =[]
        track=0
        while track < len(word1) or track <len(word2):
            if track < len(word1):
                merged.append(word1[track])
            if track < len(word2) :
                merged.append(word2[track])
            track +=1
        return ''.join(merged)                 


        
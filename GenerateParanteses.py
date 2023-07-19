'''Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]'''

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n==0:
            return []
        res=[]    
        def backtrack(S='', left=0, right=0):
            
            if len(S)==n*2:
                res.append(S)
                return
            if left<n:
                backtrack(S+'(',left+1, right)
            if right<left:
                backtrack(S+')',left, right+1 ) 
        backtrack()
        return res           

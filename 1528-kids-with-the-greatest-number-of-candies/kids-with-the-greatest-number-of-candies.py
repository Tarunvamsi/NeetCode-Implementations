class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        res=[]
        maxc= max(candies)
        for i in range(len(candies)):
            if (candies[i]+extraCandies >= maxc):
                res.append(True)
            else:
                res.append(False)    
        return res        

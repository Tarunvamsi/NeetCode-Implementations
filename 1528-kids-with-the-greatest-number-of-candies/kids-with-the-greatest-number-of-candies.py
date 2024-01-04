class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        max_candies = max(candies)
        return [candy + extraCandies >= max_candies for candy in candies]


# class Solution(object):
#     def kidsWithCandies(self, candies, extraCandies):
#         res=[]
#         maxc= max(candies)
#         for i in range(len(candies)):
#             if (candies[i]+extraCandies >= maxc):
#                 res.append(True)
#             else:
#                 res.append(False)    
#         return res        

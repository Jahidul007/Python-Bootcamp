class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        ss=set(candies)
        if len(ss)>=len(candies)//2:
            return len(candies)//2
        else:
            return len(ss)
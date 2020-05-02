class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxi = max(candies)
        mylist = []
        for i in range(len(candies)):
            if candies[i] + extraCandies >= maxi:
                mylist.append(True)
            else:
                mylist.append(False)
        return mylist

# Method 1(not efficient solution) complexity- O(N^2)
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        arr_s = list(set(arr))
        new = arr_s[::-1]
        new.sort()
        print(new)
        rank = []
        for i in range(len(arr)):
            for j in range(len(new)):
                if arr[i] == new[j]:
                    rank.append(j+1)
        return rank

# Method 2(efficient) complexity- O(N)
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        n=len(arr)
        if n==0:return []
        if n==1:return [1]
        rst=[]
        arr_s=sorted(arr)
        order_idx,t={},1
        for i in range(n):
            if arr_s[i] not in order_idx:
                order_idx[arr_s[i]]=t
                t+=1
        return [order_idx[arr[i]] for i in range(n)]
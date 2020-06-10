class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        idxList=list(range(len(A)))
        ans = idxList[1::2]
        ans1 = idxList[::2]
        result = A[:]
        count = 0
        count2 = 0
        for i in A:
            if i % 2 == 0:
                result[ans[count]] = i
                count += 1
            else:
                result[ans1[count2]] = i
                count2 += 1
        return(result[::-1])
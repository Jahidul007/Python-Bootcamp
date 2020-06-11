class Solution:
    def commonChars(self, A: List[str]) -> List[str]:

        ans = []
        for i in A[0]:
            j = 0
            while j < (len(A) - 1):
                if i not in A[j + 1]:
                    break
                else:
                    lst = list(A[j + 1])
                    p = lst.index(i)
                    del (lst[p])
                    A[j + 1] = "".join(lst)  # from lst to string
                    j += 1
            if j == len(A) - 1:
                ans.append(i)

        return ans
class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        list_A = A.split(' ')
        list_B = B.split(' ')
        ans= []
        dict_ = {}
        for i in list_A:
            if i not in dict_:
                dict_[i] = True
            else:
                dict_[i] = False
        for i in list_B:
            if i not in dict_:
                dict_[i] = True
            else:
                dict_[i] = False
        for k,v in dict_.items():
            if v == True:
                ans.append(k)
        return ans
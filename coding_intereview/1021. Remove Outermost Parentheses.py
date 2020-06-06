class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        count = 0
        final = ""
        for i in S:
            if i=="(":
                count+=1
                if count!=1:
                    final+=i
            else:
                count-=1
                if count!=0:
                    final += i
        return final
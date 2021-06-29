class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        maxOne = 0
        maxZero = 0
        oneCount = 0
        zeroCount = 0
        for i in range(len(s)):
            if(s[i]=="1"):
                oneCount +=1
                zeroCount = 0
                if(oneCount>maxOne):
                    maxOne = oneCount
            if(s[i]=="0"):
                zeroCount +=1
                oneCount = 0
                if(zeroCount>maxZero):
                    maxZero = zeroCount
        print(maxOne, maxZero)
        if(maxOne>maxZero):
            return True
        else:
            return False

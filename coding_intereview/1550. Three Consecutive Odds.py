class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        cont = 0
        for  i in range(0, len(arr)):
            if  arr[i]%2==1:
                cont +=1
                if cont == 3:
                    return True 
            else:
                cont = 0
            
        return False

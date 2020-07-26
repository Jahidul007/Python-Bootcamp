class Solution:
    def arrangeWords(self, text: str) -> str:
        arr=[]
        for index, x in enumerate(text.split(" ")):
       
            arr.append( (len(x), index,  x) )
            
        r = [x[2] for x in sorted(arr)]
        
        
        return (" ".join(r) ).capitalize()

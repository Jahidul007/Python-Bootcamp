class Solution:
    def reformatNumber(self, number: str) -> str:
         
        number = number.replace(' ', '')
        number = number.replace('-', '')
        
        blocks = []
        
        while len(number) > 4:
            
            blocks.append( number[:3])
            number = number[3:]
        
        if len(number) <= 3:
            blocks.append( number )
        else:
            blocks.append( number[:2])
            blocks.append( number[2:])
        
        return '-'.join(blocks)

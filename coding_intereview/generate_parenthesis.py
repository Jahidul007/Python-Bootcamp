class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        def rescue(i, left, right, li):
            if i ==2*n-1:
                result.append("".join(li))
                return
            if left < n:
                li.append('(')
                rescue(i+1, left+1, right, li)
                li.pop()
            if right< left:
                li.append(')')
                rescue(i+1, left, right+1, li)
                li.pop()
        rescue(-1,0,0,[])
        return result
class Solution:
    def convert(s):
        stack =[]
        for i in s:
            if i == '#':
                if stack:
                    stack.pop(-1)
            else:
                stack.append(i)
        res = ''
        for i in stack:
            res+=i
        return res
    def backspaceCompare(self, S: str, T: str) -> bool:
        return Solution.convert(S) == Solution.convert(T)

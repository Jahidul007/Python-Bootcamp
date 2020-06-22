class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        stack = []
        for c in S:
            if c.isalpha():
                stack.append(c)
        new_s = ''
        for c in S:
            if c.isalpha():
                new_s += stack.pop()
            else:
                new_s += c
        return new_s
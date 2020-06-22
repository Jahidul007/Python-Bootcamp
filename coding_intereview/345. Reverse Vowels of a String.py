class Solution:
    def reverseVowels(self, S: str) -> str:
        st = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        stack = []
        for c in S:
            if c in st:
                stack.append(c)
        new_s = ''

        for c in S:
            if c in st:
                new_s += stack.pop()
            else:
                new_s += c
        return new_s
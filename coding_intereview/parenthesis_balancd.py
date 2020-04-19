class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {")": "(",
                 "}": "{",
                 "]": "["}

        for c in s:
            if(c in ["(", "{", "["]):
                stack.append(c)
            elif(len(stack) == 0 or pairs[c] != stack.pop()):
                return False

        return stack == []
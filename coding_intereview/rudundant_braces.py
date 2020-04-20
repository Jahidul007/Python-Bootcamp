class Solution:
    # @param A : string
    # @return an integer
    def braces(self, A):
        stack = []
        for item in A:
            if item in "(+-*/":
                stack.append(item)
            elif item in ")":
                last_item = stack.pop()
                if last_item == "(":
                    return True
                while "(" != stack.pop():
                    continue
        return False

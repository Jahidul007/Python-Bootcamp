class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count = 0
        for log in logs:
            if log == './':
                continue
            if log[-2] != '.':
                count += 1
            if log == '../':
                if count == 0:
                    continue
                else:
                    count -= 1
        return count

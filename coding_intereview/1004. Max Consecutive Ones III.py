from collections import deque


class Solution:
    def longestOnes(self, A, K: int) -> int:
        len_max_ones_array = 0
        zeros_count = 0
        ones_array = deque()

        for a in A:
            ones_array.append(a)
            if a == 0:
                zeros_count += 1
                while zeros_count > K:
                    if ones_array.popleft() == 0:
                        zeros_count -= 1
            len_max_ones_array = max(len_max_ones_array, len(ones_array))
        return len_max_ones_array

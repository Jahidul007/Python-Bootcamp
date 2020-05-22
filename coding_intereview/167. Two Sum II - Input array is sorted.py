from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        i = 0
        j = len(numbers) - 1

        while i != j:
            if numbers[i] + numbers[j] == target:
                break
            if numbers[i] + numbers[j] > target:
                j -= 1
            if numbers[i] + numbers[j] < target:
                i += 1
        # eval() is used for basic calculation
        return [i + 1, j + 1]

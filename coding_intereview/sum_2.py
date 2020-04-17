class Solution:
    def twoSum(self, nums, target: int):
        n = len(nums)
        sum = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                sum = (nums[i] + nums[j])
                if sum == target:
                    return [i, j]


print(Solution().twoSum([2, 7, 11, 15], 13))


def binary_search(ara, left, right, target):
    if left > right:
        return -1

    while left <= right:
        mid = (left + right) // 2
        if ara[mid] == target:
            return mid
        if ara[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def two_sum_v1(numbers):
    numbers.sort()
    n = len(numbers)
    for i in range(n - 1):
        target = 15
        print(target)
        target_index = binary_search(numbers, i + 1, n - 1, target)
        if target_index > i:
            return i, target_index


def two_sum_v2(numbers):
    found = dict()
    for n in numbers:
        m = 0 - n
        try:
            if found[m]:
                return m, n
        except KeyError:
            found[n] = 1


print(two_sum_v2([3, 0, -1, 2, -3, -1, -4]))

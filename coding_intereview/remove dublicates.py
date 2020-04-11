def remove_duplicates(nums):
    unique_nums = [];
    unique_nums.append(nums[0])

    n = len(nums)
    if n == 0:
        return 0
    for i in range(1, n):
        if (nums[i] != nums[i - 1]):
            unique_nums.append(nums[i])
    return len(unique_nums)


class Solution:
    def removeDuplicates(self, nums):
        n = len(nums)
        if n < 2:
            return len(nums)

        current_index = 1

        for i in range(1, n):
            if (nums[i] != nums[i - 1]):
                nums[current_index] = nums[i]
                current_index += 1
        return current_index


def remove_duplicates1(nums):
    unique_nums = list(set(nums))
    unique_nums.sort()

    return unique_nums


print(remove_duplicates1([1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4]))

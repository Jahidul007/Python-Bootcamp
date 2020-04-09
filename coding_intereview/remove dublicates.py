def remove_duplicates(nums):
    unique_nums = [];
    unique_nums.append(nums[0])

    n = len(nums)
    for i in range(1, n):
        if (nums[i] != nums[i - 1]):
            unique_nums.append(nums[i])
    return len(unique_nums)


def remove_duplicates1(nums):
    unique_nums = list(set(nums))
    unique_nums.sort()

    return len(unique_nums)



print(remove_duplicates1([1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4]))

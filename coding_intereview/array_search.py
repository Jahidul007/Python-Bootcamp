def binary_search(nums, target):
    n = len(nums)
    if (n == 0):
        return 0
    left = 0
    right = n - 1

    while left <= right:
        if target < nums[left]:
            return left
        if target > nums[right]:
            return left
        mid = int(left + (right - left) / 2)

        if target == nums[mid]:
            if mid == left or nums[mid - 1] != target:
                return mid
            right = mid

        elif target < nums[mid]:
            if mid > left and target > nums[mid - 1]:
                return mid
            right = mid - 1
        else:
            if mid < right and target < nums[mid + 1]:
                return mid + 1
            left = mid + 1
    return -1


nums = [1, 2, 4, 4, 4, 5, 7, 7]

print(binary_search(nums, 4))

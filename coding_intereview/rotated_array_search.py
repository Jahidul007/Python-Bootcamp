def searchRange(nums, target):
    try:
        i = nums.index(target)
    except:
        return -1
    return i

'''
https://www.interviewbit.com/problems/rotated-sorted-array-search/
'''
def binary_search(nums, target):
    n = len(nums)
    if (n == 0):
        return 0
    left = 0
    right = n - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        if nums[left] < nums[mid] and target < nums[mid] and target >= nums[left]:
            right = mid - 1
        elif nums[mid] < nums[right] and target <= nums[right] and target > nums[mid]:
            left = mid + 1
        elif nums[left] > nums[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1


def search(A, key):
    left, right = 0, len(A) - 1

    while left <= right:
        mid = (left + right) // 2
        if A[mid] == key:
            return mid
        if A[left] < A[mid] and key < A[mid] and key >= A[left]:
            right = mid - 1
        elif A[mid] < A[right] and key > A[mid] and key <= A[right]:
            left = mid + 1
        elif A[left] > A[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return -1

nums = [1, 2, 4, 4, 4, 5, 6,7, 7]

print(search(nums, 4))

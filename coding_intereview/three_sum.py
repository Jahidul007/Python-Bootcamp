def threeSum1(nums):
    n = len(nums)
    nums.sort()
    found = []
    for i in range(0, n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    found.append([nums[i], nums[j], nums[k]])

    return found


def threeSum(nums):
    if len(nums) < 3:
        return []
    nums.sort()

    result = []
    i = 0
    n = len(nums)
    while i < n - 2:
        k = n - 1
        j = i + 1
        while j < k:
            sum = nums[i] + nums[j] + nums[k]
            if sum == 0:
                result.append([nums[i], nums[j], nums[k]])
                while nums[j] == nums[j + 1] and j < k - 1:
                    j += 1
                while nums[k] == nums[k - 1] and j < k - 1:
                    k -= 1
                j += 1
            elif sum > 0:
                k -= 1
            else:
                j += 1
        while i < n - 3 and nums[i] == nums[i + 1]:
            i += 1
        i +=1
    return result


nums = [-1, 0, 1, 2, -1, -4]

print(threeSum1(nums))

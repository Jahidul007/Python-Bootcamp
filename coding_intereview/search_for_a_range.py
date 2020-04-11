def searchRange(nums, target):
    try:
        i = nums.index(target)
    except:
        return [-1, -1]
    j = list(reversed(nums)).index(target)
    return [i, len(nums)-j-1]

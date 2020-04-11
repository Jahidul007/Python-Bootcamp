def searchRange(nums, target):
    try:
        i = nums.index(target)
    except:
        return -1
    return i
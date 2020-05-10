class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums = []
        length = len(nums2)
        for i in nums1:
            if (nums2.index(i) + 1) < length:
                for j in range(nums2.index(i) + 1, length):
                    if nums2[j] > i:
                        nums.append(nums2[j])
                        break
                    elif j == length - 1:
                        nums.append(-1)
            else:
                nums.append(-1)
        return nums


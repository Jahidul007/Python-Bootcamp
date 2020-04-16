class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        list3 = nums1 + nums2
        list3.sort()
        list_len = len(list3)
        if list_len % 2 == 1:
            m =(list_len//2)
            print("odd", m)
            return list3[m]
        else:
            m = (list_len // 2)
            print("even" , m)
            return (list3[m]+list3[m-1])/2


nums1 = [1, 2]
nums2 = [3, 4]
print(Solution().findMedianSortedArrays(nums1, nums2))

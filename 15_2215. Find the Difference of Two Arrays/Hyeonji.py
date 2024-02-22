class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1 = set(nums1)
        nums2 = set(nums2)

        intersection = nums1 & nums2

        for i in intersection:
            nums1.remove(i)
            nums2.remove(i)

        return [list(nums1),list(nums2)]

"""
Runtime: 139 ms
Memory Usage: 17 MB
"""
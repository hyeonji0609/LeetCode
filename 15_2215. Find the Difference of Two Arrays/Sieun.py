class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        result = []
        numset1 = set(nums1)
        numset2 = set(nums2)

        result.append(numset1-numset2)
        result.append(numset2-numset)

        return result

"""
Runtime 135 ms
Memory 17.15 MB
"""
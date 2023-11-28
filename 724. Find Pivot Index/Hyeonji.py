class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for pivot in range(len(nums)):
            if sum(nums[:pivot]) == sum(nums[pivot+1:]) :
                return pivot
        return -1

"""
Runtime: 6590 ms
Memory Usage: 17.5 MB
"""
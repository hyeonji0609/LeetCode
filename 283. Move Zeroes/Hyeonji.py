class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return nums
        else :
            sum_zero = nums.count(0)
            for i in nums[:]:
                if i == 0:
    	            nums.remove(0)
            nums.extend([0] * sum_zero)

"""
Runtime: 447 ms
Memory Usage: 18 MB
"""
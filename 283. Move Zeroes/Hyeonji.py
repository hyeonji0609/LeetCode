class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return nums
        else :
            sum_zero = nums.count(0) # 0의 갯수 세기
            for i in nums[:]: 
                if i == 0:
    	            nums.remove(0) # 0인 값들 리스트에서 remove
            nums.extend([0] * sum_zero) # 0 갯수만큼 list 뒤에 추가

"""
Runtime: 447 ms
Memory Usage: 18 MB
"""
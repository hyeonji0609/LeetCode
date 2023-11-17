class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_count = nums.count(0)
        zero_list = []
        for i in range(int(zero_count)):
            zero_list.append(0)
            nums.remove(0)
        nums.extend(zero_list)
        
        
'''
Runtime: 471 ms - Beats 13.75%
Memory: 17.96MB - Beats 13.36%
'''
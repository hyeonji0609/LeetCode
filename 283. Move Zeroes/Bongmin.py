class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        for i in nums:
            if i == 0:        
                nums.append(nums.pop(nums.index(0)))
        """
        Do not return anything, modify nums in-place instead.
        """
        
        """
        runtime : 766 ms
        memory : 17.8 MB
        """
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        for i in nums:
            if i == 0:
                count += 1
        
        for j in range(count):
            nums.remove(0)
            nums.append(0)

"""
Runtime 444ms
Memory 17.83MB
"""
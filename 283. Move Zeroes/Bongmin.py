class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        count = 0
        for i in nums:
            if i == 0:
                count+=1
        for i in range(count):
            nums.remove(0)
            nums.append(0)
        
"""
runtime : 437 ms
memory : 17.8 MB
"""
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        MaxSum = sum(nums[:k])
        iSum = MaxSum

        for i in range(k, len(nums)):
            iSum = iSum - nums[i-k] + nums[i]
            if iSum > MaxSum:
                MaxSum = iSum

        return MaxSum / k

"""
Rumtime 956 ms
Memory 27.9 MB
"""
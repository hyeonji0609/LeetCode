class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = 0
        for i in range(len(nums)):
            if sum(nums[:i]) == sum(nums[i+1:]):
                n = i
                break
            else:
                n = -1
        return n
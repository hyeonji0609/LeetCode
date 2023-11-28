class Solution:
    def pivotIndex(self, nums: List[int]) -> int:        
        result = -1

        for i in range(len(nums)):
            leftsum = sum(nums[:i])
            rightsum = sum(nums[i+1:])

            if leftsum == rightsum:
                result = i
                break
        
        return result
    

"""
Rumtime 6663 ms
Memory 17.7 MB
"""
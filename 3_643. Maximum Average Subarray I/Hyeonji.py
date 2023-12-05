class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum_arr = []
        max_sum = 0

        if len(nums) == k :
            return sum(nums) / k
        
        else:
            for i in range(len(nums)-k+1):
                if sum(nums[i:i+k]) / k > max_sum :
                    max_sum = sum(nums[i:i+k]) / k
            
            return max_sum

"""
Time Limit Exceeded
"""
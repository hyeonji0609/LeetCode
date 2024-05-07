class Solution:
    def rob(self, nums: List[int]) -> int:
        total = [0] * len(nums)
        
        if len(nums) < 2: # 0과 1까지는 담아줌
            return max(nums)
            
        total[:2] = nums[:2]
        
        for i in range(2, len(nums)):
            total[i] = max(total[i-2], total[i-3]) + nums[i] # 선택 가능한 경우의 수는 전전과 전전전 !
        
        return max(total[-1], total[-2])
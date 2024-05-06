class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        
        res_ls = [0] * len(nums)
        res_ls[0] = nums[0]
        res_ls[1] = max(nums[0],nums[1])
        # 턴다 : 앞전까지 있던거 vs. (턴거 + 앞앞집 턴거 합)
        for i in range(2,len(nums)):
            
            res_ls[i] = max(res_ls[i-2] + nums[i], res_ls[i-1])
            print(res_ls)
            
        return max(res_ls)


'''
runtime : 49ms beats : 5.12%
memory : 16.64 beats : 12.16%

'''
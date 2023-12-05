class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        unique_value = list(set(nums))
        value_count = {}
        for value in unique_value:
            value_count[nums.count(value)] = value
        return value_count.get(1)
    
'''
Runtime 3241ms - Beats 11.94%
Memory 19.86MB - Beats 5.36%
'''
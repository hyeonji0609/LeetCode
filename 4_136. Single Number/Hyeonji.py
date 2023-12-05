class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        remove_dup = list(dict.fromkeys(nums)) # 고윳값 찾기
        output_dic = {}
        
        if len(nums) == 1 : # 만약 인자가 하나만 있을 경우
            return nums[0] # 인자 하나 그대로 리턴
        else:
            for i in remove_dup:
                output_dic[str(i)] = nums.count(i) # nums에서 갯수 세서 dict에 고윳값과 갯수를 key, value로 저장 
        
        return int({key for key, value in output_dic.items() if value == 1}.pop()) # value값이 1인 key값을 int로 반환

"""
Runtime: 3175 ms
Memory Usage: 18.8 MB
"""
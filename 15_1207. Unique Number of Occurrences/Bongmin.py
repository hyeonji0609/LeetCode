class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        digit_dict = {}
        for i in arr:
            if i not in digit_dict:
                digit_dict[i] = 1
            else:
                digit_dict[i] +=1
        # 고유값을 카운트를 해서 같으면 유니크하다는 뜻이므로 True
        if len(set(digit_dict.values())) ==len(digit_dict.values()):
            return True
        else:
            return False
"""
runtime : 41ms : beats : 57.56%
memory : 16.56mb : beats : 98.35%
"""
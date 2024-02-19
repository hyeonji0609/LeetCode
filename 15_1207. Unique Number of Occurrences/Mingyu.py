class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # 발생횟수를 저장할 딕셔너리 생성
        occur_dict = {}
        # arr를 순회하면서 발생횟수 카운트하여 딕셔너리에 업데이트
        for num in arr:
            if num in occur_dict:
                occur_dict[num] += 1
            else:
                occur_dict[num] = 1
        # 딕셔너리의 고유한 value들을 set으로 생성
        unique_occur = set(occur_dict.values())
        
        # 딕셔너리의 길이와 set의 길이가 같으면 True 아니면 False
        return len(occur_dict) == len(unique_occur)
    
    '''
    Runtime 37 ms - Beats 80.92%
    Memory 16.56 MB - Beats 99.73%
    '''
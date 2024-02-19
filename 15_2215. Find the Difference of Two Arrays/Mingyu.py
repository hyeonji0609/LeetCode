class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # 두 배열의 집합 생성
        set_num1, set_num2 = set(nums1), set(nums2)
        # 결과를 저장할 리스트 생성
        res = []
        # res에 s1-s2와 s2-s1 차례대로 append
        res.append(set_num1 - set_num2)
        res.append(set_num2 - set_num1)
        
        return res
    
    '''
    Runtime 145 ms - Beats 52.98%
    Memory 17.15 MB - Beats 62.87%
    '''
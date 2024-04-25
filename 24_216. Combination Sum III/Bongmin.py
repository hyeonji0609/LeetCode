class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        
        def back(comb):
            if len(comb) == k and sum(comb) == n: # k개이면서 n이라면
                res.append(comb[:]) # comb안에거 모두 들고오기 [:]주의
                return 
            for i in range(1, 10): # 1 ~ 9 까지
                if i not in comb: # 중복 확인
                    comb.append(i) # 숫자 추가
                    back(comb) # 재귀
                    comb.pop()
        
        comb = []
        back(comb)
        # 중복 제거 # [124] [142] [412] 등등 같은 값을 제거 -> 런타임 바보, 메모리 바보 만드는 주범
        # 다른 방법이 생각이 나지않음.
        res2 = []
        for i in res:
            i.sort()
            if i not in res2:
                res2.append(i)
                
        return res2



'''
runtine : 8859ms / beats : 5.05%
memory : 76.86mb / beats : 6.37%
'''
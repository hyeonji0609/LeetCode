class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        res = []
        potions.sort() # 작은거부터 돌려야댐
        print(potions)
        potions_len = len(potions)
        for s in spells:
            cnt = potions_len
            for p in potions:
                if s * p >= success: # 조합이 success보다 크면 멈추고 거기까지만 세고
                    break
                else: # 아니라면 실패했다는거니까 총 포션 길이에서 1빼주기
                    cnt -=1
            res.append(cnt)

        return res
## 타임 리밋
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort() # 정렬
        res = [] # 결과

        for s in spells:
            start = 0 
            end = len(potions) - 1 
            
            while start <= end: 
                mid = (start + end) // 2
                # 최소 success보다 크면 되므로
                # success 미만일 때는 start를 키우고
                if s * potions[mid] < success:
                    start = mid + 1
                else: # success 이상이면 end를 낮추고
                    end = mid - 1
            # 총 길이에서 start idx만큼 빼주면 되므로
            res.append(len(potions) - start)

        return res

'''
runtime : 1176ms / beats : 63.12%
memory : 39.67mb / beats : 49.45%
'''




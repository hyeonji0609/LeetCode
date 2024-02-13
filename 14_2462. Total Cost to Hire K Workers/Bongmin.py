import math

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        result = []
        if len(costs) > candidates:
            for _ in range(k):
                indexing = math.ceil(len(costs)/2) # 절반만 iter하기 위한 나누기 2
                first, first_index = float("inf"),0 # first는 무한대, first_indexing은 0으로 초기화
                last, last_index = float("inf"),0 # last는 무한대, last_indexing은 0으로 초기화

                for i in range(indexing): # costs길이의 절반만 돌릴건데
                    if first > costs[i]:
                        first = costs[i]
                        first_index = i

                    if last > costs[-i-1]:
                        last = costs[-i-1]
                        last_index = -i-1
                if first < last:
                    result.append(costs.pop(first_index))
                elif last < first:
                    result.append(costs.pop(last_index))
                else: # 동점
                    result.append(costs.pop(first_index))
        else:
            result.append(min(costs))
        return sum(result)

# 아직 못풀었습니다

                
                
            

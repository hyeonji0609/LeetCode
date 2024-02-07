from heapq import *
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify(stones)

        while len(stones) > 1 : # 남아있는 stone이 1보다 클때까지 반복
            if stones[0] == stones[1]: # 만약 리스트에서 맨 앞 두 숫자들이 같으면
                stones.pop(0) # 둘 다 리스트에서 제거
                stones.pop(0)
            else:
                weight = stones[0] - stones[1] # 무게의 차를 구하고
            
                stones.pop(0) # 둘 다 리스트에서 제거
                stones.pop(0)
                
                stones.append(weight) # 다시 리스트에 무게의 차를 넣어주고 
                stones.sort(reverse=True) # 재정렬
        
        return stones[0] if stones else 0 # 리스트에 남아있는게 있으면 리턴, 아니면 0 리턴

"""
Runtime: 34 ms
Memory Usage: 16.5 MB
"""
import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while True:
            try:
                y,x = heapq.nlargest(2, stones) # 큰 순서대로 2개를 y,x에 담겠다. 문제에서 y > x이므로 순서를 반대로
                if y == x: # 같다면 둘다 pop
                    stones.pop(stones.index(x))
                    stones.pop(stones.index(y))
                elif y != x: # 다르다면 
                    stones.pop(stones.index(x)) # x는 부숴지니 pop
                    stones[stones.index(y)] = y-x # y는 y-x로 재정의
                if len(stones) <= 1: # stones의 길이가 1보다 작아지면 pop
                    break
            except: # except의 이유 stones에 남은 것이0이 되어버릴 수 있기 때문
                break
        return stones[0] if stones else 0 # 이때 남아있다면 stones[0], 없다면 0

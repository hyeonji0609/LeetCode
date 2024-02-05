import heapq

class SmallestInfiniteSet:

    def __init__(self):
        self.current_smallest = 1 # 현재 가장 작은 수 1로 초기화
        self.heap = [] # 힙 초기화
        self.num_set = set() # pop 된 숫자 추적할 집합

    def popSmallest(self) -> int:
        if not self.heap: # 힙에 숫자가 없으면 
            smallest = self.current_smallest # smallest를 가장 작은 숫자로 업데이트
            self.current_smallest += 1 # 현재 가장 작은 수 1 증가

        else:  # 힙에 숫자가 있으면 그 중 가장 작은 숫자 반환
            smallest = heapq.heappop(self.heap)
            self.num_set.remove(smallest)  # 뽑힌 숫자는 집합에서 제거

        return smallest

    def addBack(self, num: int) -> None:
        # num이 현재 가장 작은 수보다 작고, 아직 집합에 없으면 추가
        if (num < self.current_smallest) and (num not in self.num_set):
            heapq.heappush(self.heap, num)
            self.num_set.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)

'''
Runtime 88 ms - Beats 90.87%
Memory 17.19 MB - Beats 79.64%
'''
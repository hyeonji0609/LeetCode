import heapq

# 1. popSmallest의 else
# 2. addBack의 if 
# 3. popSmallest의 if
class SmallestInfiniteSet:

    def __init__(self):
        self.cnt = 0 # 계속 올라가는 숫자
        self.heap = [] # 빈 heap list 초기화
        heapq.heapify(self.heap)
        return None

    def popSmallest(self) -> int:
        # self.heap이 0이 아니라면 즉, 들어온 num이 카운트하고 있는 숫자보다 작아서 heap에 추가가 되어 있다면
        # heap에서 먼저 빠질 수 있도록 해주기
        if len(self.heap) != 0: 
            return heapq.heappop(self.heap)
        else:
            self.cnt+=1 # 0부터 시작하므로 1 더해줘서
            return self.cnt # return 출력
    def addBack(self, num: int) -> None:
        # 카운트가 올라가다가 addBack을 만나면 카운트와 들어오는 num을 비교해서 들어오는 아이가 작으면 heap에 추가
        # 근데 여기서 같은 숫자가 나오는 경우도 있으므로 not in 즉, 없다면 추가.
        if num <= self.cnt and num not in self.heap:
            heapq.heappush(self.heap, num)
        return None

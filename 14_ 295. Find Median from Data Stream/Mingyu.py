import heapq as hq

# 풀이 1: 이렇게 하면 입력 요소가 너무 많은 경우에 TimeLimit 뜸
class MedianFinder:

    def __init__(self):
        # arr 리스트 초기화
        self.arr = []

    def addNum(self, num: int) -> None:
        # heapify를 이용해 self.arr를 최소힙 정렬 수행
        hq.heapify(self.arr)
        # self.arr에 num push
        hq.heappush(self.arr, num)

    def findMedian(self) -> float:
        # self.arr는 0번 요소만 가장 작은 값이고, 그 뒤 인덱스의 요소들은 정렬되어 있지 않으므로
        # sorted 함수로 직접 정렬 수행
        sorted_arr = sorted(self.arr)
        # sorted_arr의 길이가 짝수이면,
        if len(sorted_arr) % 2 == 0:
            # sorted_arr에서 center 앞 인덱스 값 추출
            pre_center_value = sorted_arr[(len(sorted_arr)//2) - 1]
            # sorted_arr에서 center 인덱스 값 추출
            center_value = sorted_arr[len(sorted_arr)//2]
            # 두 값의 중앙값을 return
            return ((pre_center_value+center_value)/2)
        # 그렇지 않으면, 홀수이면,
        else:
            # sorted_arr의 중앙값 return
            return sorted_arr[(len(sorted_arr)//2)]
        
# 풀이 2: 이렇게 풀어야 Time Limit 안뜸.
class MedianFinder:

    def __init__(self):
        # 최소힙과 최대힙 초기화
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        # addNum이 호출되면, 우선 -num으로 최대힙에 값 할당
        hq.heappush(self.max_heap, -num)
        # 그 후, 최대힙의 최대값을 pop하여 최소힙으로 할당
        # 이렇게 하면, 특정 시점부터는 최소힙의 구성요소가 최대힙보다 더 많게 됨.
        hq.heappush(self.min_heap, -hq.heappop(self.max_heap))
        # 그 순간이 오면, 최소힙의 최솟값을 pop하여 최대힙으로 할당
        # 이로 인해, 최소힙은 항상 최대힙보다 큰 값들을 갖고 있고,
        # 최대힙은 항상 최소힙보다 작은 값들을 갖고 있게 됨.
        # addNum이 여러번 호출되고 나면, 두 heap의 길이는 항상 같거나 max_heap이 하나 더 많은 값을 갖게 됨.
        if len(self.min_heap) > len(self.max_heap):
            hq.heappush(self.max_heap, -hq.heappop(self.min_heap))

    def findMedian(self) -> float:
        # 따라서 findMedian이 호출됐을 때,
        # 두 힙의 길이가 같으면, 즉, 전체 값의 갯수가 짝수이면
        # 중앙값은 최소힙의 루트값과 최대힙의 루트값의 평균이 됨.
        if len(self.min_heap) == len(self.max_heap):
            return ((-self.max_heap[0] + self.min_heap[0]) / 2)
        # 그렇지 않으면, 전체 값의 갯수가 홀수이므로
        # 중앙값은 최대힙의 루트값이 됨.
        else:
            return -self.max_heap[0]
        
'''
Rumtime 414 ms - Beats 37.97%
Memory 38.43 MB - Beats 70.24%
'''
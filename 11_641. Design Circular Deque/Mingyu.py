class MyCircularDeque:

    def __init__(self, k: int):
        self.k = k # size k 초기화
        self.deque = [0] * k # size k만큼 deque 초기화
        self.front = 0 # front 인덱스
        self.rear = 0 # rear 인덱스
        self.count = 0 # count 초기화

    def insertFront(self, value: int) -> bool:
        # deque가 가득 찬 경우, False를 리턴
        if self.isFull():
            return False
        # front 인덱스를 현재 front인덱스 - 1을 size k만큼 나눈 나머지로 업데이트
        self.front = (self.front - 1) % self.k
        # 업데이트 된 front에 value 할당
        self.deque[self.front] = value
        # count 1 증가
        self.count += 1
        # True return
        return True

    def insertLast(self, value: int) -> bool:
        # deque가 가득 찬 경우, False를 리턴
        if self.isFull():
            return False
        # 현재 rear에 value 할당
        self.deque[self.rear] = value
        # rear 인덱스를 현재 rear 인덱스 + 1을 size k만큼 나눈 나머지로 업데이트
        self.rear = (self.rear + 1) % self.k
        # count 1 증가
        self.count += 1
        # True return
        return True

    def deleteFront(self) -> bool:
        # deque가 빈 경우, return False
        if self.isEmpty():
            return False
        # front 인덱스를 현재 front 인덱스 + 1을 size k만큼 나눈 나머지로 업데이트
        self.front = (self.front + 1) % self.k
        # count 1 감소
        self.count -= 1
        # return True
        return True

    def deleteLast(self) -> bool:
        # deque가 빈 경우, return False
        if self.isEmpty():
            return False
        # rear 인덱스를 현재 rear 인덱스 - 1로 반환하되, 음수가 되지 않게끔
        # size k만큼 더하고 size k만큼 나눈 나머지로 업데이트
        self.rear = (self.rear - 1 + self.k) % self.k
        # count 1 감소
        self.count -= 1
        # return True
        return True

    def getFront(self) -> int:
        # deque가 빈 경우 -1을 return
        if self.isEmpty():
            return -1
        # front 인덱스에 해당하는 value를 return
        return self.deque[self.front]

    def getRear(self) -> int:
        # deque가 빈 경우 -1을 return
        if self.isEmpty():
            return -1
        # rear - 1 인덱스에 해당하는 value 반환
        return self.deque[(self.rear - 1 + self.k) % self.k]

    def isEmpty(self) -> bool:
        # self.count가 0이면 True, 그렇지 않으면 False
        return self.count == 0

    def isFull(self) -> bool:
        # self.count가 k이면 True, 그렇지 않으면 False
        return self.count == self.k
    
    '''
    Runtime 63 ms - Beats 46.06%
    Memory 17.18 MB - Beats 94.86%
    '''
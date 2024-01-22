from collections import deque

class MyCircularDeque:
    def __init__(self, k: int):
        self.k = k
        self.dec = deque(maxlen = self.k)
        return None

    def insertFront(self, value: int) -> bool:
        if len(self.dec) < self.k:
            self.dec.appendleft(value)
            return True
        else:
            return False


    def insertLast(self, value: int) -> bool:
        if len(self.dec) < self.k:
            self.dec.append(value)
            return True
        else:
            return False

    def deleteFront(self) -> bool:
        if len(self.dec) >=1:
            self.dec.popleft()
            return True
        else:
            return False
        

    def deleteLast(self) -> bool:
        if len(self.dec) >= 1:
            self.dec.pop()
            return True
        else:
            return False
        

    def getFront(self) -> int:
        if len(self.dec) >=1:
            return self.dec[0]
        else:
            return -1
        

    def getRear(self) -> int:
        if len(self.dec) >=1:
            return self.dec[-1]
        else:
            return -1

    def isEmpty(self) -> bool:
        if len(self.dec) >=1:
            return False
        else:
            return True

    def isFull(self) -> bool:
        if len(self.dec) == self.k:
            return True
        else:
            return False
'''
Runtime : 70ms beats : 34.08%
Memoru : 17.21mb beats : 70.06%
'''

# deque로 풀면 안될 것 같습니다

class MyCircularDeque:
    def __init__(self, k: int):
        self.k = k # circular deque의 길이
        self.ls = [] # 빈 리스트

    def insertFront(self, value: int) -> bool:
        # 길이가 k보다 작을 때에만 추가할 수 있도록 구현
        if len(self.ls) < self.k:
            temp_ls = [value] # value를 리스트로 만들어주고
            self.ls = temp_ls + self.ls # 앞에다 붙여주기
            return True
        else:
            False
            
    def insertLast(self, value: int) -> bool:
        # 길이가 k보다 작을 때에만 추가할 수 있도록 구현
        if len(self.ls) < self.k:
            temp_ls = [value] # value를 리스트로 만들어주고
            self.ls = self.ls + temp_ls # 뒤에다 붙여주기
            return True
        else:
            False

    def deleteFront(self) -> bool:
        if len(self.ls) >= 1:
            self.ls.pop(0)
            return True
        else:
            return False

    def deleteLast(self) -> bool:
        if len(self.ls) >= 1: # 길이가 1보다 커야 pop 가능하므로 이 코드를 작성
            self.ls.pop() 
            return True
        else: # 아니라면 False
            return False
        
    def getFront(self) -> int:
        if len(self.ls) >= 1: # 길이가 1보다 커야 값이 있는 것이므로
            return self.ls[0] 
        else: # 아니라면 -1
            return -1

    def getRear(self) -> int:
        if len(self.ls) >= 1: # 길이가 1보다 커야 값이 있는 것이므로
            return self.ls[-1]
        else: # 아니라면 -1
            return -1

    def isEmpty(self) -> bool:
        if len(self.ls) >= 1: # 길이가 1보다 크면 비어있지 않으므로
            return False # False
        else: # 0일때만 True
            return True
    def isFull(self) -> bool:
        if len(self.ls) == self.k: # k와 같으면 full 상태
            return True
        else:
            return False
        
'''
Runtime : 60ms : beats : 78.66%
Memory : 17.10ms : beats : 75.16%
'''
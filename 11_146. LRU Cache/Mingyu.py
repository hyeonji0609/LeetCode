class LRUCache:

    def __init__(self, capacity: int):
        # Cache 용량 및 딕셔너리 초기화
        self.capacity = capacity
        self.cache = {}

    def get(self, key: int) -> int:
        # key가 cache 딕셔너리에 있는 경우
        if key in self.cache:
            # cache에서 해당 value를 반환
            value = self.cache[key]
            # cache에서 해당 key 제거 및 최근 위치로 업데이트
            self.cache.pop(key)
            self.cache[key] = value
            # value 반환
            return value
        # 그렇지 않으면 -1 반환
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # key가 cache에 있는 경우
        if key in self.cache:
            # cache에서 key 제거 및 해당하는 value 업데이트
            self.cache.pop(key)
            self.cache[key] = value
        # key가 cache에 없는 경우
        else:
            # cache의 용량이 꽉 찬 경우
            if len(self.cache) == self.capacity:
                # cache에서 가장 앞쪽에 있는(오래된) key를 조회
                old_key = next(iter(self.cache))
                # 오래된 key를 제거
                self.cache.pop(old_key)
                # 새로 입력된 key로 value 업데이트
                self.cache[key] = value
            # cache의 여유가 있는 경우
            else:
                # key에 value 업데이트
                self.cache[key] = value
                
    '''
    Runtime 515 ms - Betas 96.37%
    Memory 78.04 MB - Beats 22.32%
    '''
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

    def get(self, key: int) -> int:
        if key in self.cache: # 만약 캐시안에 key가 있으면
            value = self.cache[key]
            self.cache.pop(key) # 해당 key를 pop
            self.cache[key] = value # 제일 앞순서로 보내줌
            return value
        else :
            return -1 # 캐시안에 key가 없으면 -1 리턴
            
    def put(self, key: int, value: int) -> None:
        if key in self.cache: # 캐시안에 key가 있으면 
                self.cache.pop(key)
                self.cache[key] = value # 제일 앞순서로 보내줌
        else : # 캐시안에 키가 없으면
            if len(self.cache) == self.capacity : # 캐시가 꽉 찼을 경우
                first_key = next(iter(self.cache))
                self.cache.pop(first_key) # 제일 옛날 key를 없애주고
                self.cache[key] = value # 새로운 값을 넣어줌
            else :
                self.cache[key] = value

"""
Runtime: 565 ms
Memory Usage: 78.1 MB
"""
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.LRUcache = dict()

    def get(self, key: int) -> int:
        # 딕셔너리에 key가 존재한다면
        if key in self.LRUcache:
            # 순서를 업데이트하기 위해
            # key에 해당하는 value를 저장
            value = self.LRUcache[key]
            # 현 위치의 key-value 삭제
            del self.LRUcache[key]
            # 새 위치에 key-value 추가
            self.LRUcache[key] = value
            return value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # 딕셔너리에 key가 존재한다면 key의 값을 업데이트
        if key in self.LRUcache:
            del self.LRUcache[key]
        # 딕셔너리에 key가 존재하지 않으면 key-value을 cache에 추가
        # 이 때, key의 수가 용량을 초과하면 가장 오래전에 사용한 ket를 제거한 후 추가
        elif len(self.LRUcache) == self.capacity:
            # 딕셔너리의 첫번째로 입력된 key 찾기 (티스토리 참고)
            first_key = next(iter(self.LRUcache))
            del self.LRUcache[first_key]

        # 공통으로 key의 값을 업데이트(업데이트 시 가장 최근에 접근했으므로 끝으로 이동)
        self.LRUcache[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

"""
Runtime 531 ms
Memory 77.96 MB
"""
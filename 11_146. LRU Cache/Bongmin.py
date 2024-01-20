class LRUCache:
    def __init__(self, capacity: int):
        self.cache_dict = {}
        self.ls = []
        self.capacity = capacity

    def get(self, key: int) -> int:
        # 키가 없다면
        if key not in self.cache_dict:
            return -1
        # 키가 있다면
        # ls에서 key를 지우고 다시 append하기 -> 맨 뒤로 보내는 작업
        self.ls.remove(key)
        self.ls.append(key)

        return self.cache_dict[key]

    def put(self, key: int, value: int) -> None:
        # 키가 원래 있는경우
        if key in self.cache_dict:
            # dict는 갈아끼워주고
            self.cache_dict[key] = value
            # ls에서는 맨 뒤로 보내기
            self.ls.remove(key)
            self.ls.append(key)
        # 키가 없는 경우
        else:
            # ls에도, dict에도 추가만 해주기
            self.ls.append(key)
            self.cache_dict[key] = value

            # 추가 해준 다음 capacity보다 key의 len값이 더 길때는 
            if len(self.ls) > self.capacity:
                # 기존 키를 pop해서
                oldest_key = self.ls.pop(0)
                # cache_dict에서도 pop해주기
                self.cache_dict.pop(oldest_key)
                
"""
runtime : 1742ms beats : 8.78% ..?
memory : 76.82mb beats : 98.85%
메모리는 적게 들지만 느리다.
"""
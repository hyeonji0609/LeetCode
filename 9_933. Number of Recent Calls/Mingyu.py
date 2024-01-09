class RecentCounter:

    def __init__(self):
        self.count = [] # count list 초기화

    def ping(self, t: int) -> int:
        # count 리스트에 t를 할당
        self.count.append(t)
        
        # count의 첫번째 요소가 t-3000보다 작은 동안 반복하며 첫번째 요소 제거
        while self.count[0] < t - 3000:
            self.count.pop(0)

        # count 리스트의 길이를 반환
        return len(self.count)
        
# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

'''
Runtime 180ms - Beats 99.24%
Memory 22.99MB - Beats 21.55%
'''
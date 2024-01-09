class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]  # 초기 홈페이지 URL 추가
        self.curr = 0              # 현재 페이지 위치 초기화

    def visit(self, url: str) -> None:
        self.history = self.history[:self.curr+1] # 현재 페이지 이후 기록 삭제
        self.history.append(url)   # 새 URL 추가
        self.curr = len(self.history)-1 # 현재 위치 업데이트

    def back(self, steps: int) -> str:
        if self.curr - steps >= 0:
            self.curr -= steps     # 뒤로 이동 가능 시, 위치 업데이트
        else:
            self.curr = 0          # 뒤로 이동 불가능 시, 홈페이지로 이동
        
        return self.history[self.curr] # 현재 페이지 URL 반환

    def forward(self, steps: int) -> str:
        if self.curr + steps < len(self.history):
            self.curr += steps     # 앞으로 이동 가능 시, 위치 업데이트
        else:
            self.curr = len(self.history)-1 # 앞으로 이동 불가능 시, 최신 페이지로 이동
        
        return self.history[self.curr] # 현재 페이지 URL 반환


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)

"""
Runtime 169 ms
Memory 19.97 MB
"""
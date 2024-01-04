class BrowserHistory:
    
    def __init__(self, homepage: str):
        self.prev = []
        self.front = []
        self.current = homepage

    def visit(self, url: str) -> None:
        # 방문하면 현재 페이지를 prev에 담아주기
        self.prev.append(self.current)
        # 현재 페이지를 들어온 url로 교체
        self.current = url
        if self.front != None:
            self.front.clear()
        return None

    def back(self, steps: int) -> str:
        # step에 맞게 꺼내기
        for i in range(steps):
            # prev 0이 아닐때 까지만 돌리기
            if len(self.prev) != 0:
                # 현재 페이지를 먼저 front 담아주고
                self.front.append(self.current)
                # 현재 페이지를 이전 페이지들에서 꺼내서 고쳐주기
                self.current = self.prev.pop()
            # prev 비어있다면
            else:
                break # 멈추고
        return self.current # 현재 페이지를 return

    def forward(self, steps: int) -> str:
        # step에 맞게 꺼내기
        for i in range(steps):
            # front 0이 아닐때 까지만 돌리기
            if len(self.front) != 0:
                # 현재 페이지를 먼저 이전 페이지에 담아주고
                self.prev.append(self.current)
                # 현재 페이지를 이후 페이지에서 꺼내서 고쳐주기
                self.current = self.front.pop()
            else:
                break
        return self.current
        
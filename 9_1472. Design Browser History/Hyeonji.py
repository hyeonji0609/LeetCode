class BrowserHistory:

    def __init__(self, homepage: str):
        self.data = [homepage]
        self.stack = []

    def visit(self, url: str) -> None:
        if len(self.data) == 0:
            self.data.append(self.stack[-1])
        self.data.append(url)
        self.stack.clear()
        
    def back(self, steps: int) -> str:
        if steps >= len(self.data):
            for i in range(len(self.data)) :
                self.stack.append(self.data.pop(-1))
            return self.stack[-1]
        
        else :
            for i in range(steps) :
                self.stack.append(self.data.pop(-1))
            return self.data[-1]

    def forward(self, steps: int) -> str:
        if len(self.stack) == 0:
            return self.data[-1]
        
        elif steps <= len(self.stack):
            if len(self.data) == 0 :
                self.data.append(self.stack.pop(-1))
            for i in range(min(steps, len(self.stack))):
                self.data.append(self.stack.pop(-1))
            return self.data[-1]
        
        else :
            if len(self.data) == 0 :
                self.data.append(self.stack.pop(-1))
            for i in range(len(self.stack)):
                self.data.append(self.stack.pop(-1))
            return self.data[-1]

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
        
"""
Runtime: 208 ms
Memory Usage: 20 MB
"""
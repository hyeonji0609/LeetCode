class BrowserHistory:
    def __init__(self, homepage: str):
        # 클래스 초기화 시 back 스택에 homepage 할당 및 forward 스택 초기화
        self.back_stack = [homepage]
        self.forward_stack = []

    def visit(self, url: str) -> None:
        # visit하면, back_stack에 url 할당 후 forward 스택 비우기
        self.back_stack.append(url)
        self.forward_stack.clear()

    def back(self, steps: int) -> str:
        # steps가 0보다 크고 back 스택의 길이가 1보다 클 때까지 루프
        while steps > 0 and len(self.back_stack) > 1:
            # forward 스택에 back 스택의 마지막 요소 할당
            self.forward_stack.append(self.back_stack.pop())
            # steps 1씩 감소
            steps -= 1
        # back 스택의 마지막 요소 return
        return self.back_stack[-1]

    def forward(self, steps: int) -> str:
        # steps가 0보다 크고 forward 스택이 비어있지 않을때 까지 루프
        while steps > 0 and self.forward_stack:
            # back 스택에 forward 스택의 마지막 요소 할당
            self.back_stack.append(self.forward_stack.pop())
            # steps 1씩 감소
            steps -= 1
        # back 스택의 마지막 요소 return
        return self.back_stack[-1]
'''
Runtime 204 ms - Beats 71.41%
Memory 20 MB - Beats 18.5%
'''

# Linked List로 풀기
class ListNode:
    def __init__(self, url):
        self.url = url
        self.prev = None
        self.next = None

class BrowserHistory:
    def __init__(self, homepage: str):
        # 클래스 초기화 시 current를 homepage로 초기화
        self.current = ListNode(homepage)

    def visit(self, url: str) -> None:
        # newNode에 url을 할당
        newNode = ListNode(url)
        # nuwNode의 이전을 current로 할당
        newNode.prev = self.current
        # current의 next를 newNode로 업데이트
        self.current.next = newNode
        # current를 newNode로 업데이트
        self.current = newNode

    def back(self, steps: int) -> str:
        # current의 prev가 비어있지 않고, steps가 1 이상일 때 동안 루프
        while self.current.prev and steps > 0:
            # current에 current의 이전값으로 업데이트
            self.current = self.current.prev
            # steps를 1씩 감소
            steps -= 1
        # current의 head 노드(url)를 return
        return self.current.url

    def forward(self, steps: int) -> str:
        # current의 next가 비어있지 않고, steps가 1 이상일 때 동안 루프
        while self.current.next and steps > 0:
            # current를 current의 next로 업데이트
            self.current = self.current.next
            # steps를 1씩 감소
            steps -= 1
        # current의 head 노드(url)를 return 
        return self.current.url
    
'''
Runtime 209ms - Beats 64.38%
Memory 19.94MB - Beats 18.05%
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 빈 경우 제외
        if not head:
            return None
        
        stack = []
        while head:
            stack.append(head.val)  # 현재 값을 링크드 리스트에 넣기
            head = head.next # 다음 것에 연결하기

        stack_len = len(stack) # 스택 길이 계산 해서 pop할거 계싼하기
        if stack_len == 1: # 스택 길이가 1이라면 중간이 없으므로 None
            return None
        elif stack_len % 2 == 0:
            index = round(stack_len // 2)
        else:
            index = (stack_len -1) // 2
        stack.pop(index)
        
        top = ListNode(stack[0]) # 초기 선언
        current = top # current에 담아주고

        # 연결 시켜주면 끝
        for i in stack[1:]:
            current.next = ListNode(i)
            current = current.next

        return top
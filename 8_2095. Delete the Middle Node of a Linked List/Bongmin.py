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

        stack_len = len(stack) # 스택 길이 계산 해서 pop할거 계산하기
        if stack_len == 1: # 스택 길이가 1이라면 중간이 없으므로 None
            return None
        elif stack_len % 2 == 0: # 길이가 짝수라면 round처리 # 길이가 4하면 인덱스는 3까지 있으므로 2로 처리하기위함
            index = round(stack_len // 2)
        else: # 길이가 홀수라면 길이에서 하나빼면 딱 떨어짐 # 길이가 5라면 처리할 인덱스는 2이므로 (5-1)//2
            index = (stack_len -1) // 2
        stack.pop(index)
        
        top = ListNode(stack[0]) # 초기 선언
        current = top # current에 담아주고

        # 연결 시켜주면 끝
        for i in stack[1:]:
            current.next = ListNode(i)
            current = current.next

        return top
'''
runtime 1074ms 상위 13%!!
memory : 61.7mb 상위 17%!!
'''
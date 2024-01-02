# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 비어있는 경우를 제외
        if not head:
            return head
        
        stack = []
        while head:
            stack.append(head.val)  # 현재 값을 링크드 리스트에 넣기
            head = head.next # 다음 것에 연결하기
        
        even_ls, odd_ls = [],[] # 짝홀 인덱스 구분

        for i in range(len(stack)):
            if i % 2 ==0: # 나눠서 0은 짝수 인덱스
                even_ls.append(stack[i])
            else: # 아니라면 홀수 인덱스
                odd_ls.append(stack[i])


        top = ListNode(stack[0]) # 초기 선언
        current = top # current에 담아주고

        # 짝수먼저 돌려주기
        for i in even_ls[1:]:
            current.next = ListNode(i)
            current = current.next
        # 그 다음 홀수 돌려주기
        for i in odd_ls:
            current.next = ListNode(i)
            current = current.next

        return top

'''
runtime : 96ms 상위 95% ...
memory : 19.9 mb # 하위 95%............
'''
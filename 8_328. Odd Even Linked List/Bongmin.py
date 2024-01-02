# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# 1 리스트를 3개 만들어서 이게 공간복잡도가 어떻게 되는지 잘모르겠습니다 ..!
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
런타임도 안좋고 메모리도 안좋다
'''

# 2 O(1) 1개만 추가로 허용한다 해서 stack 하나만 가지고 풀었습니다.

import math
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

        top = ListNode(stack[0]) # top 설정
        current = top 
        
        len_stack = len(stack) # stack의 길이 계산
        for_iter = math.ceil(len_stack / 2) # 반복문 돌릴 것 계산 # 칠판 설명 필요..?
        
        for i in range(for_iter):
            # top이 설정되어 있기 때문에 0일때는 예외 처리
            if i == 0:
                stack.pop(i)
                continue
            # 0이 아닐때는 아래와 같이 
            else:
                current.next = ListNode(stack[i])
                current = current.next
                stack.pop(i)
        # 팝 하고 스택에 남은것들 이어주기
        for i in range(len(stack)):
            current.next = ListNode(stack[i])
            current = current.next

        return top


'''
runtime : 48ms 상위 49%!!!
memory : 19.5 mb # 하위 95% 그대로 .........
런타임은 아주 많이 개선!
'''
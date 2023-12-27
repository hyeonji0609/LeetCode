# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # prev를 None으로 초기화
        prev = None
        # head가 None이 아닐 때까지 루프
        while head is not None:
            # current에 head 할당
            current = head
            # head를 다음 노드로 업데이트
            head = head.next
            # current의 next를 prev로 지정하여 뒤집기
            current.next = prev
            # 이전 노드를 현재 노드로 업데이트
            prev = current
            
        return prev
    
    
'''
Runtime 48ms - Beats 19.06%
Memory 18.46MB - Beats 24.96%
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        base = ListNode(None)
        
        if head is None: # head가 비었는지 검사
            return None
        
        else :
            base.val = head.val # base의 val 값을 head의 val 값과 동일하게

            while head.next : # next가 None값이 아닐 때까지 반복
                NextNode = ListNode(head.next.val) # NextNode를 head의 next 값으로 지정
                NextNode.next = base # NextNode의 next 값을 현재 base(=head) 값으로 지정
                base = NextNode # base 값을 NextNode로 재할당
                head = head.next # head 값을 head.next로 재갱신

            return base

"""
Runtime: 38 ms
Memory Usage: 19 MB
"""
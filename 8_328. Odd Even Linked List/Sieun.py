# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # linked list의 길이가 0,1인 경우
        if head == None or head.next == None:
            return head

        odd = head
        even = head.next
        temp = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        
        odd.next = temp
        
        return head

"""
Runtime 36 ms
Memory 19.2 MB
"""
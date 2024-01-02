# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        len_head = 0
        temp = head

        # 전체 개수 세기
        while temp:
            len_head += 1
            temp = temp.next
        
        # 길이가 1개인 경우
        if len_head == 1:
            return None
        
        count = 0
        prev = None
        curr = head
        middle_idx = len_head // 2

        while count < middle_idx:
            count += 1
            prev = curr
            curr = curr.next

        if prev != None:
            prev.next = curr.next

        return head

"""
Runtime 1432 ms
Memory 52.2 MB
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # head가 비어있으면 None을 return
        if head is None:
            return None
        # head의 첫번째 값을 odd로 할당
        odd = head
        # even의 head와 even을 odd의 next로 할당
        even_head, even = odd.next, odd.next
        # even이 비어있지 않고, even의 next가 None이 아닐 때까지 루프(head의 끝)
        while even and even.next:
            # odd의 next는 odd의 다다음번(홀수만)
            odd.next = odd.next.next
            # odd를 odd.next로 업데이트
            odd = odd.next
            # even의 next는 even의 다다음번(짝수만)
            even.next = even.next.next
            # even을 even.next로 업데이트
            even = even.next
        # 루프가 끝난 후, odd의 next를 even의 head로 할당시켜 둘을 연결
        odd.next = even_head
        return head
'''
Runtime 34ms - Beats 97.98%
Memory 19.27MB - Beats 20.97%
'''
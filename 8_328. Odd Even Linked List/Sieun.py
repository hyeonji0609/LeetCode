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
        
        # 표 상에서 두 값이 None일 때 학습이 종료되어야 함 -> 표는 그림으로 설명
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        
        odd.next = # 짝수 값의 포인터를 가르쳐야 하는데 새로운 linked list 생성없이 어떻게 하는지 모르겠음
        return head

"""
못품
"""
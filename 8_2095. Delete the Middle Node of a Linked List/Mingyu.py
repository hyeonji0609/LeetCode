# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Linked List 길이 반환 함수
        def len(head):
            count = 0
            current = head
            while current:
                count += 1
                current = current.next
            return count

        # 연결리스트 길이 계산
        length = len(head)
        # 연결리스트 길이 절반 확인
        half_length = length // 2
        # current에 head 할당
        current = head
        # current가 None이거나 리스트의 길이가 1이면 None을 return
        if current is None or current.next is None:
            return None

        # current를 절반 직전까지 순회
        for _ in range(half_length-1):
            current = current.next
        # 절반 직전의 next는 절반의 다음번으로 할당(절반 위치 skip)
        current.next = current.next.next
        # current를 next로 업데이트
        current = current.next
        # current 순회 재개
        while current:
            current = current.next
        return head
    
    '''
    Runtime 1192ms - Beats 85.40%
    Memory 51.19MB - Beats 98.62%
    '''
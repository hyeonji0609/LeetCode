# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        # current에 head 할당(초기화)
        current = head
        # result 0으로 초기화
        result = 0
        # 연결리스트 순회
        while current:
            # 2진수를 10진수로 바꾸기 위해서
            # 현재까지의 result * 2에 현재 값을 더해줌
            result = result * 2 + current.val
            # current를 next로 업데이트
            current = current.next
        
        return result
'''
Runtime 45ms - Beats 15.20%
Memory 16.21MB - Beats 51.60%
'''
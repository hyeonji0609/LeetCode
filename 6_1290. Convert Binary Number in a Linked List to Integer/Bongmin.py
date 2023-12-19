# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:

        result = 0

        while head:
            result = result * 2 + head.val  # 
            head = head.next  # 다음 노드로 이동

        return result
# 100이라면 0 + 0이 되므로 반영되지 않음
# 101이라면 처음 result는 0이므로 0 * 2 + 1이 된다

# runtime : 25ms
# memory : 16.35mb
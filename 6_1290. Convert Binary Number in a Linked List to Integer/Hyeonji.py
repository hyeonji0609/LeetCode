class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        value = []
        base = ListNode(None)
        base.next = head
        
        while head :
            value.append(head.val)
            head = head.next
        
        binary = '0b' + ''.join(str(s) for s in value) # 2진수로 값을 나타냄
        
        return int(binary, 2) # int를 사용하여 2진수를 10진수로 변경

"""
Runtime: 43 ms
Memory Usage: 16.4 MB
"""
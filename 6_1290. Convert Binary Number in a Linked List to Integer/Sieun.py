# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        result = 0
        
        def convertToDecimal(head, result):
            if head == None:
                return result

            result = (result << 1) + head.val # 비트 연산에서 결과값을 2배(<<)
            return convertToDecimal(head.next, result)
        return convertToDecimal(head, result)
    
"""
Runtime 38 ms
Memory 16.2 MB 
"""
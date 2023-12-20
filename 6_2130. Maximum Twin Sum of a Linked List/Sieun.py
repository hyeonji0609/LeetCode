# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        nums = []
        len_nums = 0
        curr = head

        while curr != None: # 전체 연결리스트의 길이
            len_nums += 1
            curr = curr.next

        idx = (len_nums // 2) - 1

        while head != None:
            if idx >= 0: # (len_nums//2)-1 ~ 0
                nums.append(head.val)
            else: # -1 ~
                nums[idx] += head.val
            idx -= 1
            head = head.next

        return max(nums)
    
"""
Runtime 710 ms
Memory 56.67 MB
"""
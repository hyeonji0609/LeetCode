'''
idea
temp를 사용하여 얘를 한 칸씩 미는 것
1이 저장되어 있다면 얘를 넥스트로 설정함으로써 
(1) -> 2(1) -> 3(2(1)) -> 4(3(2(1))) .. 
이런 방식
'''

from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 비어있는 경우를 제외
        if not head:
            return head

        result = None # 한칸씩 밀릴 변수

        while head:

            temp = head # 헤드를 임시 저장 # "처음에는 (((1)))이 저장"
            head = head.next # 원래 헤드를 다음 것으로 옮김 ex) 1 -> 2

            temp.next = result # 임시 저장한 헤드의 다음 자체를 결과 변수로 지정
            # 이 부분이 (1) -> 2(1)이 되는 과정
            # "처음에는 None이 저장되어있으므로 1(None)이 될 것"
            result = temp # 결과 변수에 임시 저장되어있는 것 자체를 저장

        return result
'''
Runtime : 36ms
memory : 18.5mb
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        linked_ls = [] # 빈 링크드 리스트
        current = head # 현재 노드를 헤드로 초기화

        while current:
            linked_ls.append(current.val)  # 현재 값을 링크드 리스트에 넣기
            current = current.next # 다음 것에 연결하기

        # 합 계산하기
        n = len(linked_ls)
        max_num = 0 # 최종 결과
        for i in range(n // 2):
            count = linked_ls[i] + linked_ls[n - 1 - i]
            if count > max_num: # 새로 계산한 것이 크다면
                max_num = count # 담아주기

        return max_num # 최대 합 반환하기


# runtime : 628ms
# memory : 56.7mb
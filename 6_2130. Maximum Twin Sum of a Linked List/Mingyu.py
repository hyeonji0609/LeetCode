# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # 연결리스트 길이 조회 함수
        def get_len(head):
            count = 0
            current = head
            while current:
                count += 1
                current = current.next
            return count

        # 연결리스트 길이 할당
        length = get_len(head)
        # 입력값이 짝수개이므로 무조건 반 나눠서 대칭되는게 쌍둥이 노드임
        # 따라서 연결리스트를 중간까지만 순회하기 위해 길이의 절반을 계산
        half_length = length // 2
        # 중간까지 순회한 값을 저장할 스택 생성
        stack = []
        # current에 head 할당(초기화)
        current = head
        # 연결리스트의 중간까지만 순회
        for _ in range(half_length):
            # 순회하면서 stack에 값 할당
            stack.append(current.val)
            # current를 next로 업데이트
            current = current.next
        # 최대 twin_sum 초기화
        max_twin_sum = 0
        # 연결리스트의 중간 이후를 순회
        while current: # 이때, current는 연결리스트의 중간값임
            # current.val과 stack의 마지막 값을 더해서 twin_sum 계산
            twin_sum = current.val + stack.pop()
            # 둘 중에 큰 값으로 max_twin_sum 업데이트
            max_twin_sum = max(max_twin_sum, twin_sum)
            # current를 next로 업데이트
            current = current.next

        return max_twin_sum
'''
Runtime 717ms - Beats 20.13%
Memory 58.13MB - Beats 14.04%
'''
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd = odd_head = ListNode(None) # 홀수를 새로 담을 ListNode 생성
        even = even_head = ListNode(None) # 짝수를 새로 담을 ListNode 생성
        current = head

        idx = 0 # 인덱스 역할

        while current:
            if idx % 2 == 0: # 만약 인덱스가 짝수라면
                odd_head.next = ListNode(current.val) # 홀수 값을 odd_head.next에 담아줌
                odd_head = odd_head.next # head 이동
            else :
                even_head.next = ListNode(current.val) # 짝수 값을 even_head.next에 담아줌
                even_head = even_head.next

            current = current.next # 현재 값은 계속 변경됨
            idx += 1

        odd = odd.next # 맨 앞의 노드가 None(dummy)이므로, odd의 head를 그 다음 노드부터 지정
        even = even.next
        odd_head.next = even # odd_head의 next에 even을 연결
        
        return odd
    
# 만약 1,2,3,4,5로 값이 들어온다면 코드가 다 끝난 시점에서는
# odd_head는 5를 가리키고 있고, odd는 1을 가리키고 있다.
# odd_head의 next로 even을 한다면 5 뒤에 2,4가 다음으로 지정된다.
# 그리고 odd를 return해주면 1, 3, 5, 2, 4가 된다.

"""
Runtime: 95 ms
Memory Usage: 19.8 MB
"""
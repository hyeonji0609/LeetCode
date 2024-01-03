class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        middlenode = head
        
        while middlenode:
            length += 1 # node의 길이 저장
            middlenode = middlenode.next
        
        middle = length // 2 # node의 길이의 반을 middle이라고 저장
        
        if length == 1 : # 만약 node가 하나밖에 없으면
            return None # []을 return
        
        idx = 0 # 노드에서 인덱스 역할을 하는 변수
        current = head
        
        while idx < middle : 
            if idx == middle-1 : # 만약 middle 전까지 current가 이동했다면
                current.next = current.next.next # currnet의 next를 middle의 next로 변경
            
            idx += 1
            current = current.next
        
        return head
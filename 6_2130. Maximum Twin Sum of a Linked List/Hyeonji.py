class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        value = {}
        idx = 0
        
        base = ListNode(None)
        base.next = head
        
        
        while head :
            value[idx] = head.val # 딕셔너리에 index와 value 값 저장
            idx += 1
            head = head.next
        
        d1 = dict(list(value.items())[len(value)//2:]) # 딕셔너리를 list화 해서 반으로 잘라냄
        d2 = dict(list(value.items())[:len(value)//2][::-1]) # 반으로 잘라낸 리스트(뒷부분)는 역순으로
        
        max_sum = 0
        
        for (key1, value1), (key2, value2) in zip(d1.items(), d2.items()): # zip을 사용하여 dict 두개를 한번에 불러옴
            twin_sum = value1 + value2 # value 값만 더하기
            
            if twin_sum > max_sum : # max값보다 클 경우 그 값을 max_sum으로 대체
                max_sum = twin_sum
        
        return max_sum

"""
Runtime: 864 ms
Memory Usage: 64.3 MB
"""
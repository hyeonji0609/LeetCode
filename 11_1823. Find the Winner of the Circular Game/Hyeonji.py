class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = [i for i in range(1, n+1)]
        
        while len(friends) != 1 : # friend가 한명 남을 때 까지 반복
            if len(friends) >= k : # 만약 friend 수가 k개보다 크면
                idx = friends.index(friends[k-1]) # k-1번째 친구의 인덱스를 찾음
            else : # 만약 friend 수가 k개보다 작으면
                idx = friends.index(friends[k % len(friends)-1]) # friend 수를 k만큼 나눈 나머지 값 - 1 
    
            friends.pop(idx) # 친구 찾아서 끌어내기
            friends = friends[idx:] + friends[:idx] # 새로 리스트 재정의
        
        return friends[0]

"""
Runtime: 48 ms
Memory Usage: 16.7 MB
"""

"""
만약에 1, 2, 3, 4 친구가 남았고 k = 6이라고 하면 2번째 친구가 out되어야 함
그러면 6 % 4의 나머지가 2이기 때문에 2번째 친구를 끌어내야함
-> 인덱스로 접근해야하기 때문에 -1 해줌
그리고 나간 친구 기준으로 인덱스를 다시 재정의 해줌
[1,2,3,4] -> [3, 4, 1]
"""
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        n = list(range(1,n+1)) # 1부터 시작하는 n 리스트화

        # n이 하나만 남을때 까지 돌릴건데
        for i in range(len(n)-1): 
            # 길이가 k보다 크다면
            if len(n)>=k:
                n.pop(k-1) # 그대로 n에서 k-1을 팝하기
                # 팝 하고 난 후 큐 형식을 순서를 바꿔주기
                n = n[k-1:] + n[:k-1]
                print(len(n),n)
            else:
                # 길이가 k보다 작을 땐
                temp = (k%len(n)) - 1 # k % n => 나머지에서 1빼주기
                n.pop(temp)
                # 순서를 바꿔줘야하는데 -1 일때 위 식으로 하면 문제 발생
                if temp == -1: # 나누고 1 빼준 것이 -1 이라면
                    continue # 그대로 두고
                else: # 아닐 때만 위 식으로 해주기
                    n = n[temp:] + n[:temp]
                print(n)
                
                
        return n[0]
    
'''
Runtime : 150ms : beats : 20.68%
memory : 16.92mb : beats : 54.80%
'''
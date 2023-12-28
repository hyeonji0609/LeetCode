class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack = []
        stack.append(asteroids[0])
        
        # 지금 방향 정의 
        if stack[0] > 0:
            dis = "R"
        else:
            dis = "L"
            
        # 두 번째부터 시작
        for i in asteroids[1:]:
            # 방향 정의
            if i > 0:
                temp = "R"
            else:
                temp = "L"
            
            # 방향이 같으면 어펜드
            if dis == temp:
                stack.append(i)
                
            # 다르다면 스택을 거꾸로 돌리기
            else:
                for j in stack[::-1]:
                    # 절대값이 같으면 
                    if abs(j) == abs(i):
                        # 팝
                        stack.pop()
                        break
                    # 앞에 들어온게 더 크면    
                    elif abs(j) < abs(i):
                        # 팝
                        stack.pop()
                    # 둘 다 아니라면 
                    else:
                        break # 멈추기
                    
        return stack

'''
나머지는 잘 되는데 [-2,-1,1,2]인 경우가 이해가 안됩니다.
-2와 -1이 있고 1을 만나면 -1과1이 폭발하고, 
남은 -2와 2가 만나 폭발해서 빈 리스트를 반환해야하는 게 아닌가요 ?
'''


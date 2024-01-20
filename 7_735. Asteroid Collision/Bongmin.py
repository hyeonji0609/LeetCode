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

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            # 스택이 존재하고, 들어오는 애는 왼쪽인데, 스택에 마지막은 오른쪽으로 이동중에
            while stack and a < 0 < stack[-1]:
                # 크기 비교하기
                if stack[-1] < abs(a): # 들어오는애가 더 크다면
                    stack.pop()  # 스택 마지막을 pop
                elif stack[-1] == abs(a): # 같다면
                    stack.pop()  # 둘 다 폭발.
                    break  
                else: # 스택에 남아있는 친구가 더 크다면
                    break # 그냥 머추기

            else:
                # 폭발 조건에 맞지 않는 친구들은 그냥 어펜드
                stack.append(a)

        return stack

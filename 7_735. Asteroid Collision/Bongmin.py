class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack = []
        stack.append(asteroids[0])
        
        if stack[0] > 0:
            dis = "R"
        else:
            dis = "L"
        print("지금방향",dis)
        
        for i in asteroids[1:]:
            print("지금 스택",stack)
            if i > 0:
                temp = "R"
            else:
                temp = "L"
            print("들어온 애 방향 ",temp)
            if dis == temp:
                stack.append(i)
                
            else:
                for j in stack[::-1]:
                    if abs(j) == abs(i):
                        stack.pop()
                        break
                        
                    elif abs(j) < abs(i):
                        stack.pop()

                    else:
                        break
                    
        return stack

'''
나머지는 잘 되는데 [-2,-1,1,2]인 경우가 이해가 안됩니다.
-2와 -1이 있고 1을 만나면 -1과1이 폭발하고, 
남은 -2와 2가 만나 폭발해서 빈 리스트를 반환해야하는 게 아닌가요 ?
'''


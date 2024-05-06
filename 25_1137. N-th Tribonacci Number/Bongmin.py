class Solution:
    def tribonacci(self, n: int) -> int:
        t0,t1,t2 = 0,1,1
        for i in range(n):            
            if i % 3 == 0 : # 3의 배수 : t0에 값 업데이트
                t0 = t0+t1+t2
            elif i % 3 == 1: # t1에 업데이트
                t1 = t0+t1+t2
            elif i % 3 == 2: # t2에 업데이트
                t2 = t0+t1+t2


        if n % 3 == 0:
            return t0
        elif n % 3 == 1:
            return t1
        elif n % 3 == 2:
            return t2
        
'''
runtime : 30ms beats 82.83
memory : 16.70 beats : 5.48
'''
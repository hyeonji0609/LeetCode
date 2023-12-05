# number1
class Solution:
    def countBits(self, num: int) -> List[int]:
        result = []
        for j in range(num+1): # range 정의 (num이 5라면)
            i = 0 # 최대 2의 제곱을 구하기 위한 초기 값
            # 5라면 2**2까지 올라간다 -> i = 2가 된다.
            while True:
                if j // 2**i < 2: # 2의 제곱으로 나눈 것이 2보다 작다면 => 더이상 2의 제곱으로 나눌 수 없으므로
                    break # 탈출 
                else:
                    i+=1
            cnt = 0
            for i in range(i,-1,-1): # 
                if j//(2**i) >= 1:
                    cnt +=1
                    j-=(2**i)
            result.append(cnt)
        return result
'''
runtime : 885
memory : 23.2
'''    
    
# number 2
class Solution:
    def countBits(self, num: int) -> List[int]:
        twos = [2**x for x in range(16,-1,-1)] # n은 10**5 라고 했으므로 뺄 값을 미리 지정한다.
        # twos = [65536,32768,16384,8192,4096,2048,1024,512,256,128,64,32,16,8,4,2,1]
        ls = []
        for j in range(num+1):
            cnt = 0
            for i in twos: # twos를 돌면서
                if j - i < 0: # j - tows가 0보다 작으면 세지 않고
                    pass
                else: # 0보다 크다면 더 뺄수 있다는 뜻이므로 cnt의 값을 1 높인다.
                    cnt+=1 
                    j -= i # 
            ls.append(cnt)
        return ls
'''
runtime : 127
memory : 23.2
'''    
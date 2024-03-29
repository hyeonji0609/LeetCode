# 행벡터와 열벡터가 같은 것이 있는 지를 검사하는 문제

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        # ===================
        # 행 벡터들을 가져와서 1차원으로 만들어야하는데
        temp = [] # [a,b,c,d,e,f,g]와 같이 1자로 담을 공간 마련해주기
        for i in grid: # 2중 루프로 모두 꺼내와서 [a,b,c,d,e…] 처럼 만들기
            for j in i:
                temp.append(j) 
        # ===================        
        # 열벡터 뽑아오기
        columns = {} # dict를 만들건데
        for idx, i in enumerate(temp): # 1차원으로 편 temp([a,b,c,d,e..])를 enumerate로 temp의 index와 값을 같이 가져오기
            index = idx % len(grid) # grid의 길이로(예제에선 3) 나눠주면 열벡터의 인덱스가 나옴! 열의 인덱스
            if index not in columns.keys(): # 딕셔너리에 없다면 새로 생성
                columns[index] = [temp[idx]]
            else: # 있다면 append로 추가만 해주기
                columns[index].append(temp[idx])
        # ===================       
        # dict에서 list로 만들어진 values만 뽑아와서
        value_ls = list(columns.values())
        cnt = 0
        # ===================
        # 원래의 행벡터와 열벡터를 비교해서 같으면 +=1
        for i in grid:
            for j in value_ls:
                if i==j:
                    print(i, j)
                    cnt +=1
        return cnt
            

'''
Runtime : 544ms : beats : 24.49%
Memory : 22.28 : beats : 24.79%
''' 

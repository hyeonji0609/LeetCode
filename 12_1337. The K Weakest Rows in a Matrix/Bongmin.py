class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        counts = [] # 각 row의 1을 세서 넣어주기
        for i in mat:
            cnt = 0
            for j in i:
                if j == 1:
                    cnt+=1
            counts.append(cnt)
        # k번째까지만 찾아주면 되므로
        ls = sorted(counts)[:k] # ls는 k까지만 sort해서 가져온 리스트
        result = [] # 결과 리스트
        for i in ls: # 0~k까지 있는데 022 같은 경우는 같은 index를 가져오므로
            result.append(counts.index(i)) # result에 counts에 있는 인덱스를 담아주기
            counts[counts.index(i)] = None # 가져오고 나서는 None으로 바꿔주기
        return result
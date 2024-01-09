class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # 전체 후보를 담을 리스트 생성
        candidate = list(senate)
        # Radiant 큐와 Dire 큐 생성
        R_candidate, D_candidate = [] , []

        # candidate의 요소가 각각 R or D 이면 그 인덱스를 각각의 큐에 할당
        for i in range(len(candidate)):
            if candidate[i] == "R":
                R_candidate.append(i)
            else:
                D_candidate.append(i)

        # 둘 중 하나의 큐가 완전히 빌 때까지 루프
        while (len(R_candidate) > 0) and (len(D_candidate) > 0):
            # R 큐의 첫번째 요소(인덱스)가 D 큐의 첫번째 요소(인덱스) 보다 작으면,
            # R이 권리 행사할 차례
            if R_candidate[0] < D_candidate[0]:
                # D 큐의 첫번째 의원 제거 후 
                D_candidate.pop(0)
                # R 큐의 첫번째 의원(인덱스)을 pop하여 전체 후보의 수를 더한 후, 큐의 맨뒤로 재할당
                # R과 D가 번갈아가면서 권한을 수행하기 위함
                R_candidate.append(R_candidate.pop(0) + len(candidate))
                
            # D 큐의 첫번째 요소(인덱스)가 R 큐의 첫번째 요소(인덱스) 보다 작으면, (D 차례)
            elif D_candidate[0] < R_candidate[0]:
                # R 큐의 첫번째 의원 제거 후
                R_candidate.pop(0)
                # D 큐의 첫번째 의원(인덱스)을 pop하여 전체 후보의 수를 더한 후, 큐의 맨뒤로 재할당
                # R과 D가 번갈아가면서 권한을 수행하기 위함
                D_candidate.append(D_candidate.pop(0) + len(candidate))
        
        # while 루프 종료 후 R 큐의 길이가 0보다 크면 R이 승리
        if len(R_candidate) > 0:
            return "Radiant"
        # 그렇지 않으면 D가 승리
        else:
            return "Dire"
        
'''
Runtime 100ms - Beats 34.44%
Memory 18.00MB - Beats 7.28%
'''
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        row_strength = []
        for idx, row in enumerate(mat):
            soldier_count = 0  # 현재 행의 병사 수를 세기 위한 카운터
            for num in row:
                if num == 1:
                    soldier_count += 1
                else:
                    # 0을 만나면 나머지는 모두 0이므로 더 이상 병사를 세지 않고 반복을 종료
                    break
            row_strength.append((soldier_count, idx))

        # row_strength 오름차순 정렬
        row_strength.sort()

        # 병사 수가 적은 행의 인덱스를 저장하기 위한 리스트 초기화
        weakest_rows = []
        for i in range(k):
        # 정렬된 리스트에서 상위 k개 요소의 인덱스를 추출하여 weakest_rows 리스트에 추가
            weakest_rows.append(row_strength[i][1])

        return weakest_rows
    
    '''
    Runtime 87 ms - Beats 96.69%
    Memory 16.89 MB - Beats 72.13%
    '''
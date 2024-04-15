class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()  # 포션 정렬
        result = []
        
        for spell in spells:
            start, end = 0, len(potions) # start와 end 초기 설정
            while start < end:  # 이진 탐색 구현
                mid = (start + end) // 2
                # spells의 값과 정렬된 포션의 중앙값의 곱이 success 이상이면,
                if spell * potions[mid] >= success:
                    # end를 mid로 업데이트하여 재탐색(end 인덱스가 최솟값이 될때까지 !)
                    end = mid
                else: # 그렇지 않으면, start 재설정하여 우측 서브리스트에서 재탐색
                    start = mid + 1

            # 성공적인 pair의 개수 추가
            result.append(len(potions) - end)
        
        return result
    '''
    Runtime 1150 ms - Beats 67.14%
    Memory 39.37 MB - Beats 92.83%
    '''
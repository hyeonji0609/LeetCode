class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        len_flowerbed = len(flowerbed) # 꽃밭 총 길이
        possible_count = 0 # 심은 꽃의 개수
        
        for i in range(len_flowerbed):
            #현재 위치에 꽃이 없으면, True
            if flowerbed[i] == 0: 
                # 현재 위치가 0번 인덱스 or 이전 위치에 꽃이 없으면, True
                prev_empty = (i==0) or (flowerbed[i-1] == 0)
                # 현재 위치가 마지막 인덱스 or 다음 위치에 꽃이 없으면, True
                next_empty = (i == len_flowerbed-1) or (flowerbed[i+1] == 0) 
                # 현재, 이전, 다음 위치 모두에 꽃이 없으면, True
                if prev_empty and next_empty:
                    # 꽃심기
                    flowerbed[i] = 1
                    # 심은 꽃의 갯수
                    possible_count += 1
                    
        return possible_count >= n # n이 심은 꽃의 갯수이하이면 True
    
    
'''
Runtime 153ms - Beats 40.79%
Memory 16.70MB - Beats 63.63%
'''
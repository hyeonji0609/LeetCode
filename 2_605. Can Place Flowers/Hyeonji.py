class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # 꽃밭 좌우에 0을 추가해줌
        flowerbed_0 = [0] + flowerbed + [0]
        
        flower = 0
        
        for i in range(1, len(flowerbed_0)-1):
            front = flowerbed_0[i-1]
            center = flowerbed_0[i]
            back = flowerbed_0[i+1]

            # center 양쪽으로 공간이 비어있는 지(0인지) 확인 후, 비어있다면 1로 변경
            if (front == 0) and (back == 0) and (center != 1):
                flowerbed_0[i] = 1
                flower += 1
        
        # return 값은 max값이 아니어도 되므로, range에 있는지만 확인
        return n in range(flower+1)

"""
Runtime: 147 ms
Memory Usage: 16.9 MB
"""
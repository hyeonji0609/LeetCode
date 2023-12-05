class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed = [0] + flowerbed + [0]

        for i in range(1, len(flowerbed)-1):
            if [flowerbed[i-1], flowerbed[i], flowerbed[i+1]] == [0, 0, 0]:
                n = n - 1
                flowerbed[i] = 1

        result = False if n > 0 else True

        return result
    
    """
    Runtime 141ms
    Memory 16.67MB
    """
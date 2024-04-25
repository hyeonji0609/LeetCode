
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        left, right = 1, piles[-1]

        while left <= right:
            hours = 0
            mid = (left + right) // 2
            for i in piles: # piles를 돌면서
                hours += (i - 1) // mid + 1 # 이건 하다가 얻어걸림..ㅠ

            if hours > h:
                left = mid + 1
            elif hours <= h:
                right = mid - 1

        return left
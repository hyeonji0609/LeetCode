from itertools import combinations
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        idx_ls = [x for x in range(len(nums1))] 
        comb_ls = list(combinations(idx_ls, r=k))
        res = 0
        for comb in comb_ls:
            sum_nums1 = sum([nums1[x] for x in comb])
            min_nums2 = min([nums2[x] for x in comb])
            total = sum_nums1 * min_nums2
            if total > res:
                res = total
        return res
# 메모리 에러
# 아직 못풀었습니다 ㅠ

import heapq
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        res = 0
        for comb in list(combinations([x for x in range(len(nums1))], r=k)):
            sum_nums1 = 0 
            temp = []
            for i in comb:
                sum_nums1 += nums1[i]
                heapq.heappush(temp, nums2[i])
            min_nums2 = temp[0]
            total = sum_nums1 * min_nums2

            if total > res:
                res = total
        return res


from itertools import combinations
import heapq

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        nums2, nums1 = map(list, zip(*sorted(zip(nums2, nums1))))
        
        max_score = 0
        
        if k == 1 :
            for idx, val in enumerate(nums2):
                score = val * nums1[idx]
                max_score = max(max_score, score)

        else :
            cum_sum = []
            
            for idx, val in enumerate(nums2[:-k+1]):
                heapq.heapify(nums1[idx+1:])
                sort_num1 = heapq.nlargest(k-1, nums1[idx+1:])
                cum_sum.append(sum(sort_num1)) 
            
            for idx, val in enumerate(nums2[:-k+1]):
                # max_comb = nums1[idx] + sum(heapq.nlargest(k-1, nums1[idx+1:]))
                # sort_num1 = sorted(nums1[idx+1:], reverse=True)
                # max_comb = nums1[idx] + sum(sort_num1[:k-1])
                max_comb = nums1[idx] + cum_sum.pop(0)
                score = val * max_comb
                max_score = max(max_score, score)
                    
        return max_score

"""
Time Limit Exceed로 실패 ㅠㅠ
"""
from queue import PriorityQueue

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        rank_list = []
        for row_idx in range(len(mat)):
            rank_list.append((mat[row_idx].count(1), row_idx))

        rank_list.sort()

        return [x[1] for x in rank_list[:k]]

"""
Runtime 91 ms
Memory 17.10 MB
"""


# Ver.1
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count = 0
        cols = []
        len_grid = len(grid)

        for i in range(len_grid):
            cols.append([grid[j][i] for j in range(len_grid)]) 

        for row in grid:
            for col in cols:
                if row == col:
                    count += 1

        return count

"""
Runtime 517 ms
Memory 21.45 MB
"""

# Ver.2
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count = 0
        hashgrid = dict()
        len_grid = len(grid)

        for i in range(len_grid):
            hashgrid['row_'+str(i)] = grid[i]
            hashgrid['col_'+str(i)] = [grid[j][i] for j in range(len_grid)]

        for row in range(len_grid):
            for col in range(len_grid):
                if hashgrid['row_'+str(row)] == hashgrid['col_'+str(col)]:
                    count += 1

        return count


"""
Runtime 602 ms
Memory 21.34 MB
"""

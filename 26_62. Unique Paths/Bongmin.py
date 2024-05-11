class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        mat = [[0] * m for _ in range(n)] # 0 매트릭스
        # 빈칸 채워주기
        for y in range(n):
            for x in range(m):
                # 끝 테두리는 1로 맞춰주기
                if y == 0 or x == 0:
                    mat[y][x] = 1
                # 그 외는 위쪽 왼쪽의 합으로 만들어주기
                else:
                    mat[y][x] = mat[y][x-1] + mat[y-1][x]
        return mat[y][x]
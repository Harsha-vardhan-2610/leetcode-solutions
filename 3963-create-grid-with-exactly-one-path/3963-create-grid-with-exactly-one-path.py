class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        mat = [['#' for _ in range(n)] for _ in range(m)]

        for j in range(n):
            mat[0][j] = '.'

        for i in range(m):
            mat[i][n - 1] = '.'

        return ["".join(row) for row in mat]
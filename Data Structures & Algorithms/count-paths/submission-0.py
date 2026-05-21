class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        table = [[0]*n for _ in range(m)]
        table[m-1][n-1] = 1

        for row in range (m-1,-1,-1):
            for col in range (n-1,-1,-1):
                if row == m-1 and col == n-1:
                    continue

                down = 0
                right = 0

                if row +1 < m:
                    down = table[row+1][col]
                if col +1 < n:
                    right = table[row][col+1]
                table[row][col] = down + right
        return table[0][0]
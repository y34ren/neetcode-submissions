class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[1] * n for _ in range(m)]

        for i in range (1,m):
            for j in range (1,n):
                if i == 0 and j == 0:
                    continue
                top = 0
                left = 0

                if i-1 >= 0:
                    top = grid[i-1][j]
                if j - 1 >= 0:
                    left = grid[i][j-1]
                grid[i][j] = top + left
        
        return grid[m-1][n-1]
        # table = [[0]*n for _ in range(m)]
        # table[m-1][n-1] = 1

        # for row in range (m-1,-1,-1):
        #     for col in range (n-1,-1,-1):
        #         if row == m-1 and col == n-1:
        #             continue

        #         down = 0
        #         right = 0

        #         if row +1 < m:
        #             down = table[row+1][col]
        #         if col +1 < n:
        #             right = table[row][col+1]
        #         table[row][col] = down + right
        #return table[0][0]
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        arr = [[0 for _ in range(n)] for _ in range(m)] # N cols, M Rows
        for row in range(m):
            for col in range(n):
                if row == 0 or col == 0:
                    arr[row][col] = 1
                    continue
                arr[row][col] = arr[row - 1][col] + arr[row][col - 1]
        return arr[m-1][n-1]


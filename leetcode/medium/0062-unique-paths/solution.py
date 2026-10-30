# Time	O(m × n)
# Space	O(m × n) for DP
# Recursion stack	O(m + n)

class Solution:
    def solve(self, i: int, j: int, m: int, n: int) -> int:
        if(i == m - 1 and j == n - 1):
            return 1
        
        if(i >= m or j >= n):
            return 0
        
        if self.dp[i][j] is not None:
            return self.dp[i][j]
        
        right = self.solve(i + 1, j, m, n)
        down = self.solve(i, j + 1, m, n)

        self.dp[i][j] = right + down

        return self.dp[i][j]

    def uniquePaths(self, m: int, n: int) -> int:
        self.dp = [[None] * n for _ in range(m)]
        return self.solve(0, 0, m, n)
        
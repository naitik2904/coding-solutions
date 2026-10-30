# Unique Paths

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

There is a robot on an `m x n` grid. The robot is initially located at the  **top-left corner**  (i.e., `grid[0][0]`). The robot tries to move to the  **bottom-right corner**  (i.e., `grid[m - 1][n - 1]`). The robot can only move either down or right at any point in time.

Given the two integers `m` and `n`, return  *the number of possible unique paths that the robot can take to reach the bottom-right corner*.

The test cases are generated so that the answer will be less than or equal to `2 * 109`.

 

 **Example 1:** 

```
Input: m = 3, n = 7
Output: 28

```

 **Example 2:** 

```
Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down

```

 

 **Constraints:** 

- 1 <= m, n <= 100

## Solution

**Language:** Python  
**Runtime:** 1 ms (beats 30.13%)  
**Memory:** 19.1 MB (beats 89.87%)  
**Submitted:** 2026-10-30T11:08:37.579Z  

```py
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
        
```

---

[View on LeetCode](https://leetcode.com/problems/unique-paths/)
# Unique Paths III

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

You are given an `m x n` integer array `grid` where `grid[i][j]` could be:

- 1 representing the starting square. There is exactly one starting square.
- 2 representing the ending square. There is exactly one ending square.
- 0 representing empty squares we can walk over.
- -1 representing obstacles that we cannot walk over.

Return  *the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once*.

 

 **Example 1:** 

```
Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
Output: 2
Explanation: We have the following two paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)

```

 **Example 2:** 

```
Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
Output: 4
Explanation: We have the following four paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)

```

 **Example 3:** 

```
Input: grid = [[0,1],[2,0]]
Output: 0
Explanation: There is no path that walks over every empty square exactly once.
Note that the starting and ending square can be anywhere in the grid.

```

 

 **Constraints:** 

- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 20
- 1 <= m * n <= 20
- -1 <= grid[i][j] <= 2
- There is exactly one starting cell and one ending cell.

## Solution

**Language:** Python  
**Runtime:** 7 ms (beats 95.76%)  
**Memory:** 19.1 MB (beats 98.51%)  
**Submitted:** 2026-10-30T15:35:02.794Z  

```py
# TC: O(3^K)
# SC: O(K) (recursion stack).

class Solution:
    def solve(self, i: int, j: int, count: int, grid: list[list[int]]):
        if(i < 0 or i >= self.m or j < 0 or j >= self.n or grid[i][j] == -1):
            return 0

        if(grid[i][j] == 2):
            if(count == self.nonObstacle):
                return 1
            else:
                return 0
        
        grid[i][j] = -1

        right = self.solve(i + 1, j, count + 1, grid)
        left = self.solve(i - 1, j, count + 1, grid)
        up = self.solve(i, j + 1, count + 1, grid)
        down = self.solve(i, j - 1, count + 1, grid)

        grid[i][j] = 0

        return right + left + up + down

    def uniquePathsIII(self, grid: list[list[int]]) -> int:
        self.m = len(grid)
        self.n = len(grid[0])

        start_i = start_y = 0
        self.nonObstacle = 0

        for i in range(0, self.m):
            for j in range(0, self.n):

                if(grid[i][j] == 0):
                    self.nonObstacle += 1

                if(grid[i][j] == 1):
                    start_i = i
                    start_j = j
        
        self.nonObstacle += 1
        count = 0

        return self.solve(start_i, start_j, count, grid)
```

---

[View on LeetCode](https://leetcode.com/problems/unique-paths-iii/)
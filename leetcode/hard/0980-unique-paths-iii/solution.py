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
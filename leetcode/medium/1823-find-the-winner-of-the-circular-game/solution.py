# TC: O(n)

class Solution:
    def solve(self, n: int, k: int):
        if(n == 1):
            return 0

        idx = self.solve(n - 1, k)
        idx = (idx + k) % n

        return idx

    def findTheWinner(self, n: int, k: int) -> int:
        return self.solve(n, k) + 1
        
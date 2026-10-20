# Time Complexity: O(n)
# Space Complexity: O(n) — recursion stack.

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if(n == 1 and k == 1):
            return 0
        
        length = pow(2, n - 1)
        mid = length // 2

        if(k <= mid):
            return self.kthGrammar(n - 1, k)
        
        return 1 - self.kthGrammar(n - 1, k - mid)
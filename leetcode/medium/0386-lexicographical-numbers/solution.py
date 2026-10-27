# TC: O(n)
# SC: O(no. of digits) = O(logn)

class Solution:
    def solve(self, num: int, n: int):
        if(num > n):
            return
        
        self.ans.append(num)

        for i in range(0, 10):

            newNum = num * 10 + i
            if(newNum > n):
                return
            
            self.solve(newNum, n)
        
    def lexicalOrder(self, n: int) -> list[int]:
        self.ans = []

        for i in range(1, 10):
            self.solve(i, n)
        
        return self.ans
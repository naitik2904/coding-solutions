# TC: O(n)

class Solution:
    def solve(self, s: str, k: int, flag: str)-> int:
        n = len(s)
        count = 0
        ans = 0
        j = 0

        for i in range(0, n):
            ch = s[i]

            if(ch == flag):
                count += 1
            
            while(count > k):

                prevCh = s[j]
                if(prevCh == flag):
                    count -= 1
                
                j += 1
            
            ans = max(ans, i - j + 1)
        
        return ans

    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        true = self.solve(answerKey, k, 'T')
        false = self.solve(answerKey, k, 'F')

        return max(true, false)
        
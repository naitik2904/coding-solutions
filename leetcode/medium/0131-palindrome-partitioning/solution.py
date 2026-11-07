# TC = O(n · 2ⁿ) × O(n) = O(n² · 2ⁿ)​
# Auxiliary Space: O(n) for recursion and the current partition, excluding output.

class Solution:
    def partition(self, s: str) -> list[list[str]]:
        n = len(s)

        currList = []
        resultList = []


        
        def solve(idx, s):
            
            if (idx == n):
                resultList.append(currList.copy())
            
            for i in range(idx, n):

                if(isPalindrom(s[idx : i + 1])):

                    currList.append(s[idx : i + 1])

                    solve(i + 1, s)

                    currList.pop()
        
        

        def isPalindrom(s)-> bool:

            start = 0
            end = len(s) - 1

            while(start < end):

                if(s[start] != s[end]):
                    return False
                
                start += 1
                end -= 1
            
            return True


    
        solve(0, s)

        return resultList
        
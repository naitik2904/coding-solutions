# TC: O(n)

class Solution:
    def isVowel(self, ch: char):
        if(ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'):
            return True
        
        return False

    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)

        maxCount = float('-inf')
        count = 0
        i = j = 0

        while(j < n):

            ch = s[j]

            if(self.isVowel(ch)):
                count += 1
            
            if(j - i + 1 == k):

                maxCount = max(maxCount, count)

                prevCh = s[i]
                if(self.isVowel(prevCh)):
                    count -= 1
                
                i += 1
            
            j += 1

        return maxCount

        
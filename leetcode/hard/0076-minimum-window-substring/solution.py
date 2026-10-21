# Time complexity: O(m + n)
# Space complexity: O(1) because the frequency array has a fixed size of 128.

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m = len(s)
        n = len(t)

        freq = [0] * 128
        for ch in t:
            freq[ord(ch)] += 1
        
        i = j = 0
        start = 0
        required = n
        minWindow = float('inf')

        while(j < m):

            ch = s[j]
            if(freq[ord(ch)] > 0):
                required -= 1

            freq[ord(ch)] -= 1

            while required == 0:

                currWindow = j - i + 1
                if(currWindow < minWindow):
                    minWindow = currWindow
                    start = i

                prevCh = s[i]
                freq[ord(prevCh)] += 1

                if(freq[ord(prevCh)] > 0):
                    required += 1
                
                i += 1
            
            j += 1
        
        if(minWindow == float('inf')):
            return ""

        return s[start : start + minWindow]
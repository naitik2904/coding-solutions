# TC: O(n)

class Solution:
    def minWindow(self, s, p):
        # code here
        m = len(s)
        n = len(p)
        
        freq = [0] * 128
        for ch in p:
            freq[ord(ch)] += 1
        
        i = j = 0
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
            
        return "" if minWindow == float('inf') else s[start : start + minWindow]
                
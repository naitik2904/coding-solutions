# Smallest Window with All

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

Given two strings  **s**  and  **p**, find the smallest substring in s consisting of all the characters (including duplicates) of the string p.

- Return empty string in case no such substring is present. 
- If there are multiple such substring of the same length found, return the one with the least starting index.

 **Examples:** 

```
Input: s = "timetopractice", p = "toc"
Output: "toprac"
Explanation: "toprac" is the smallest substring in which "toc" can be found.

```

```
Input: s = "zoomlazapzo", p = "oza"
Output: "apzo"
Explanation: "apzo" is the smallest substring in which "oza" can be found.

```

```
Input: s = "zoom", p = "zooe"
Output: ""
Explanation: No substring is present containing all characters of p.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-21T12:34:17.636Z  

```py
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
                
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/smallest-window-in-a-string-containing-all-the-characters-of-another-string-1587115621/1)
# Minimum Window Substring

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

Given two strings `s` and `t` of lengths `m` and `n` respectively, return  *the  **minimum window***   ***substring**  **of  *`s`*  such that every character in  *`t`*  (** including duplicates**) is included in the window *. If there is no such substring, return* the empty string *`""`.

The testcases will be generated such that the answer is  **unique**.

 

 **Example 1:** 

```
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

```

 **Example 2:** 

```
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

```

 **Example 3:** 

```
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.

```

 

 **Constraints:** 

- m == s.length
- n == t.length
- 1 <= m, n <= 105
- s and t consist of uppercase and lowercase English letters.

 

 **Follow up:**  Could you find an algorithm that runs in `O(m + n)` time?

## Solution

**Language:** Python  
**Runtime:** 43 ms (beats 96.82%)  
**Memory:** 19.5 MB (beats 98.60%)  
**Submitted:** 2026-10-21T08:38:40.862Z  

```py
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
```

---

[View on LeetCode](https://leetcode.com/problems/minimum-window-substring/)
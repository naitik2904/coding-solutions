# Maximum Number of Vowels in a Substring of Given Length

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a string `s` and an integer `k`, return  *the maximum number of vowel letters in any substring of* `s` *with length* `k`.

 **Vowel letters**  in English are `'a'`, `'e'`, `'i'`, `'o'`, and `'u'`.

 

 **Example 1:** 

```
Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.

```

 **Example 2:** 

```
Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.

```

 **Example 3:** 

```
Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.

```

 

 **Constraints:** 

- 1 <= s.length <= 105
- s consists of lowercase English letters.
- 1 <= k <= s.length

## Solution

**Language:** Python  
**Runtime:** 132 ms (beats 5.01%)  
**Memory:** 19.7 MB (beats 65.24%)  
**Submitted:** 2026-10-23T07:57:52.213Z  

```py
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

        
```

---

[View on LeetCode](https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/)
# Maximize the Confusion of an Exam

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

A teacher is writing a test with `n` true/false questions, with `'T'` denoting true and `'F'` denoting false. He wants to confuse the students by  **maximizing**  the number of  **consecutive**  questions with the  **same**  answer (multiple trues or multiple falses in a row).

You are given a string `answerKey`, where `answerKey[i]` is the original answer to the `ith` question. In addition, you are given an integer `k`, the maximum number of times you may perform the following operation:

- Change the answer key for any question to 'T' or 'F' (i.e., set answerKey[i] to 'T' or 'F').

Return  *the  **maximum**  number of consecutive*  `'T'`s or `'F'`s  *in the answer key after performing the operation at most*  `k`  *times*.

 

 **Example 1:** 

```
Input: answerKey = "TTFF", k = 2
Output: 4
Explanation: We can replace both the 'F's with 'T's to make answerKey = "TTTT".
There are four consecutive 'T's.

```

 **Example 2:** 

```
Input: answerKey = "TFFT", k = 1
Output: 3
Explanation: We can replace the first 'T' with an 'F' to make answerKey = "FFFT".
Alternatively, we can replace the second 'T' with an 'F' to make answerKey = "TFFF".
In both cases, there are three consecutive 'F's.

```

 **Example 3:** 

```
Input: answerKey = "TTFTTFTT", k = 1
Output: 5
Explanation: We can replace the first 'F' to make answerKey = "TTTTTFTT"
Alternatively, we can replace the second 'F' to make answerKey = "TTFTTTTT". 
In both cases, there are five consecutive 'T's.

```

 

 **Constraints:** 

- n == answerKey.length
- 1 <= n <= 5 * 104
- answerKey[i] is either 'T' or 'F'
- 1 <= k <= n

## Solution

**Language:** Python  
**Runtime:** 175 ms (beats 44.91%)  
**Memory:** 19.3 MB (beats 98.51%)  
**Submitted:** 2026-10-26T17:18:40.501Z  

```py
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
        
```

---

[View on LeetCode](https://leetcode.com/problems/maximize-the-confusion-of-an-exam/)
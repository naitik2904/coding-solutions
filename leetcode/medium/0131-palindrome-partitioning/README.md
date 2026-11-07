# Palindrome Partitioning

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a string `s`, partition `s` such that every substring of the partition is a  **palindrome**. Return  *all possible palindrome partitioning of* `s`.

 

 **Example 1:** 

```
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

```

 **Example 2:** 

```
Input: s = "a"
Output: [["a"]]

```

 

 **Constraints:** 

- 1 <= s.length <= 16
- s contains only lowercase English letters.

## Solution

**Language:** Python  
**Runtime:** 49 ms (beats 28.38%)  
**Memory:** 34.4 MB (beats 17.26%)  
**Submitted:** 2026-11-07T08:03:01.588Z  

```py
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
        
```

---

[View on LeetCode](https://leetcode.com/problems/palindrome-partitioning/)
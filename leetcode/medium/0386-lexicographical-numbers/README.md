# Lexicographical Numbers

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an integer `n`, return all the numbers in the range `[1, n]` sorted in lexicographical order.

You must write an algorithm that runs in `O(n)` time and uses `O(1)` extra space. 

 

 **Example 1:** 

```
Input: n = 13
Output: [1,10,11,12,13,2,3,4,5,6,7,8,9]

```

 **Example 2:** 

```
Input: n = 2
Output: [1,2]

```

 

 **Constraints:** 

- 1 <= n <= 5 * 104

## Solution

**Language:** Python  
**Runtime:** 0 ms  
**Memory:** 19.4 MB  
**Submitted:** 2026-10-27T16:57:58.697Z  

```py
# TC: O(n)
# SC: O(no. of digits) = O(logn)

class Solution:
    def solve(self, num: int, n: int):
        if(num > n):
            return
        
        self.ans.append(num)

        for i in range(0, 10):

            newNum = num * 10 + i
            if(newNum > n):
                return
            
            self.solve(newNum, n)
        
    def lexicalOrder(self, n: int) -> list[int]:
        self.ans = []

        for i in range(1, 10):
            self.solve(i, n)
        
        return self.ans
```

---

[View on LeetCode](https://leetcode.com/problems/lexicographical-numbers/)
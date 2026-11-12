# Combinations

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given two integers `n` and `k`, return  *all possible combinations of*  `k`  *numbers chosen from the range*  `[1, n]`.

You may return the answer in  **any order**.

 

Original
Python3
 **Example 1:** 

```
Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.

```

 **Example 2:** 

```
Input: n = 1, k = 1
Output: [[1]]
Explanation: There is 1 choose 1 = 1 total combination.

```

 

 **Constraints:** 

- 1 <= n <= 20
- 1 <= k <= n

## Solution

**Language:** Python  
**Runtime:** 199 ms (beats 5.99%)  
**Memory:** 61.1 MB (beats 95.08%)  
**Submitted:** 2026-11-12T13:54:09.415Z  

```py
# Time Complexity: O(k * C(n, k))

# Space Complexity:
# - Auxiliary Space: O(k)
# - Output Space: O(k * C(n, k))
# - Total Space: O(k * C(n, k))


class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        currList = []
        resultList = []


        def solve(idx: int):
            nonlocal currList
            nonlocal resultList

            if(len(currList) == k):
                resultList.append(currList.copy())
            
            for i in range(idx, n + 1):

                currList.append(i)

                solve(i + 1)

                currList.pop()

        
        solve(1)
        return resultList
        
```

---

[View on LeetCode](https://leetcode.com/problems/combinations/)
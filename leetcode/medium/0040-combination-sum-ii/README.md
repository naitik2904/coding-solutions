# Combination Sum II

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a collection of candidate numbers (`candidates`) and a target number (`target`), find all unique combinations in `candidates` where the candidate numbers sum to `target`.

Each number in `candidates` may only be used  **once**  in the combination.

 **Note:**  The solution set must not contain duplicate combinations.

 

Original
Python3
 **Example 1:** 

```
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

```

 **Example 2:** 

```
Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]

```

 

 **Constraints:** 

- 1 <= candidates.length <= 100
- 1 <= candidates[i] <= 50
- 1 <= target <= 30

## Solution

**Language:** Python  
**Runtime:** 21 ms (beats 39.82%)  
**Memory:** 19.6 MB (beats 33.54%)  
**Submitted:** 2026-11-15T16:54:11.309Z  

```py
class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        n = len(candidates)

        currList = []
        resultList = []

        candidates.sort()
        
        def solve(idx: int, sum: int):
            nonlocal currList
            nonlocal resultList

            if sum == target:
                resultList.append(currList.copy())
                return
            
            if sum > target:
                return
            
            for i in range(idx, n):

                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                
                currList.append(candidates[i])

                solve(i + 1, sum + candidates[i])

                currList.pop()

        solve(0, 0)
        return resultList
        
```

---

[View on LeetCode](https://leetcode.com/problems/combination-sum-ii/)
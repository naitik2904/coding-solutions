# Permutations

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an array `nums` of distinct integers, return all the possible permutations. You can return the answer in  **any order**.

 

Original
Python3
 **Example 1:** 

```
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

```

 **Example 2:** 

```
Input: nums = [0,1]
Output: [[0,1],[1,0]]

```

 **Example 3:** 

```
Input: nums = [1]
Output: [[1]]

```

 

 **Constraints:** 

- 1 <= nums.length <= 6
- -10 <= nums[i] <= 10
- All the integers of nums are unique.

## Solution

**Language:** Python  
**Runtime:** 2 ms (beats 29.41%)  
**Memory:** 19.6 MB (beats 28.13%)  
**Submitted:** 2026-11-13T08:21:35.718Z  

```py
# TC: O(N * N!)
# Auxiliary SC: O(N)
# Total SC including output: O(N * N!).

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)

        seen = set()
        currList = []
        resultList = []

        def solve():
            nonlocal currList
            nonlocal resultList

            if(len(currList) == n):
                resultList.append(currList.copy())
            
            for i in range(0, n):

                if nums[i] in seen:
                    continue
                
                seen.add(nums[i])
                currList.append(nums[i])

                solve()

                seen.remove(nums[i])
                currList.pop()

        solve()
        return resultList
        
```

---

[View on LeetCode](https://leetcode.com/problems/permutations/)
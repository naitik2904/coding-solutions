# Non-decreasing Subsequences

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an integer array `nums`, return  *all the different possible non-decreasing subsequences of the given array with at least two elements*. You may return the answer in  **any order**.

 

 **Example 1:** 

```
Input: nums = [4,6,7,7]
Output: [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]

```

 **Example 2:** 

```
Input: nums = [4,4,3,2,1]
Output: [[4,4]]

```

 

 **Constraints:** 

- 1 <= nums.length <= 15
- -100 <= nums[i] <= 100

## Solution

**Language:** Python  
**Runtime:** 20 ms (beats 41.67%)  
**Memory:** 25.3 MB (beats 51.97%)  
**Submitted:** 2026-11-06T16:49:28.810Z  

```py
# Time: O(n * 2^n) upper bound.
# Auxiliary space: O(n), excluding output.

class Solution:

    def solve(self, i: int, nums: list[int]):

        if(len(self.currList) > 1):
            self.resultList.append(self.currList.copy())
        
        Set = set()

        for j in range(i, self.n):

            if nums[j] in Set:
                continue
            
            if(len(self.currList) == 0 or self.currList[len(self.currList) - 1] <= nums[j]):

                Set.add(nums[j])
                self.currList.append(nums[j])

                self.solve(j + 1, nums)

                self.currList.pop()


    def findSubsequences(self, nums: list[int]) -> list[list[int]]:
        self.n = len(nums)
        self.currList = []
        self.resultList = []

        self.solve(0, nums)

        return self.resultList
        
```

---

[View on LeetCode](https://leetcode.com/problems/non-decreasing-subsequences/)
# The Number of Beautiful Subsets

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given an array `nums` of positive integers and a  **positive**  integer `k`.

A subset of `nums` is  **beautiful**  if it does not contain two integers with an absolute difference equal to `k`.

Return  *the number of  **non-empty beautiful** subsets of the array*  `nums`.

A  **subset**  of `nums` is an array that can be obtained by deleting some (possibly none) elements from `nums`. Two subsets are different if and only if the chosen indices to delete are different.

 

Original
Python3
 **Example 1:** 

```
Input: nums = [2,4,6], k = 2
Output: 4
Explanation: The beautiful subsets of the array nums are: [2], [4], [6], [2, 6].
It can be proved that there are only 4 beautiful subsets in the array [2,4,6].

```

 **Example 2:** 

```
Input: nums = [1], k = 1
Output: 1
Explanation: The beautiful subset of the array nums is [1].
It can be proved that there is only 1 beautiful subset in the array [1].

```

 

 **Constraints:** 

- 1 <= nums.length <= 18
- 1 <= nums[i], k <= 1000

## Solution

**Language:** Python  
**Runtime:** 2044 ms (beats 24.20%)  
**Memory:** 19.7 MB (beats 78.23%)  
**Submitted:** 2026-11-17T08:25:46.928Z  

```py
# Time Complexity: O(n * 2ⁿ)
# Space Complexity: O(n)

class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        n = len(nums)
        result = 0
        list = []

        def solve(idx: int):
            nonlocal result

            if(idx >= n):
                result += 1
                return
            
            # Skip
            solve(idx + 1)

            # Take
            isPresent = True

            for num in list:
                
                if((nums[idx] + k == num) or (nums[idx] - k == num)):
                    isPresent = False
                    break
            
            if(isPresent):

                list.append(nums[idx])

                solve(idx + 1)

                list.pop()

        solve(0)
        return result - 1   # Remove Empty Subset
```

---

[View on LeetCode](https://leetcode.com/problems/the-number-of-beautiful-subsets/)
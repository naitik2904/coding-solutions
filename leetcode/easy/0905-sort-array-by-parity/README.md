# Sort Array By Parity

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given an integer array `nums`, move all the even integers at the beginning of the array followed by all the odd integers.

Return  ***any array**  that satisfies this condition*.

 

 **Example 1:** 

```
Input: nums = [3,1,2,4]
Output: [2,4,3,1]
Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

```

 **Example 2:** 

```
Input: nums = [0]
Output: [0]

```

 

 **Constraints:** 

- 1 <= nums.length <= 5000
- 0 <= nums[i] <= 5000

## Solution

**Language:** Python  
**Runtime:** 2 ms (beats 55.75%)  
**Memory:** 19.8 MB (beats 54.77%)  
**Submitted:** 2026-10-21T14:24:49.455Z  

```py
class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        n = len(nums)
        idx = 0

        for i in range(0, n):

            if(nums[i] % 2 == 0):
                nums[idx], nums[i] = nums[i], nums[idx]
                idx += 1

        return nums
```

---

[View on LeetCode](https://leetcode.com/problems/sort-array-by-parity/)
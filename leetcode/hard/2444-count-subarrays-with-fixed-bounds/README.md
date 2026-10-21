# Count Subarrays With Fixed Bounds

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

You are given an integer array `nums` and two integers `minK` and `maxK`.

A  **fixed-bound subarray**  of `nums` is a subarray that satisfies the following conditions:

- The minimum value in the subarray is equal to minK.
- The maximum value in the subarray is equal to maxK.

Return  *the  **number**  of fixed-bound subarrays*.

A  **subarray**  is a  **contiguous**  part of an array.

 

 **Example 1:** 

```
Input: nums = [1,3,5,2,7,5], minK = 1, maxK = 5
Output: 2
Explanation: The fixed-bound subarrays are [1,3,5] and [1,3,5,2].

```

 **Example 2:** 

```
Input: nums = [1,1,1,1], minK = 1, maxK = 1
Output: 10
Explanation: Every subarray of nums is a fixed-bound subarray. There are 10 possible subarrays.

```

 

 **Constraints:** 

- 2 <= nums.length <= 105
- 1 <= nums[i], minK, maxK <= 106

## Solution

**Language:** Python  
**Runtime:** 99 ms (beats 49.42%)  
**Memory:** 31.4 MB (beats 34.68%)  
**Submitted:** 2026-10-21T12:18:51.700Z  

```py
# TC: O(n)

class Solution:
    def countSubarrays(self, nums: list[int], minK: int, maxK: int) -> int:
        n = len(nums)

        minKPosition = -1
        maxKPosition = -1
        culpritPosition = -1
        ans = 0

        for i in range(0, n):

            if(nums[i] > maxK or nums[i] < minK):
                culpritPosition = i
            
            if(nums[i] == minK):
                minKPosition = i
            
            if(nums[i] == maxK):
                maxKPosition = i

            smaller = min(maxKPosition, minKPosition)

            temp = smaller - culpritPosition

            ans += 0 if temp < 0 else temp
        
        return ans
        
```

---

[View on LeetCode](https://leetcode.com/problems/count-subarrays-with-fixed-bounds/)
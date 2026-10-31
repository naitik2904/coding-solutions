# Subarrays with K Different Integers

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

Given an integer array `nums` and an integer `k`, return  *the number of  **good subarrays**  of* `nums`.

A  **good array**  is an array where the number of different integers in that array is exactly `k`.

- For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.

A  **subarray**  is a  **contiguous**  part of an array.

 

 **Example 1:** 

```
Input: nums = [1,2,1,2,3], k = 2
Output: 7
Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]

```

 **Example 2:** 

```
Input: nums = [1,2,1,3,4], k = 3
Output: 3
Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].

```

 

 **Constraints:** 

- 1 <= nums.length <= 2 * 104
- 1 <= nums[i], k <= nums.length

## Solution

**Language:** Python  
**Runtime:** 138 ms (beats 47.78%)  
**Memory:** 22 MB (beats 40.04%)  
**Submitted:** 2026-10-31T16:34:31.139Z  

```py
# TC: O(n)
# SC: O(K)

class Solution:
    def solve(self, nums: list[int], k: int) -> int:
        n = len(nums)

        i = j = 0
        count = 0
        map = {}

        while(j < n):

            curr = nums[j]
            map[curr] = map.get(curr, 0) + 1

            while(len(map) > k):

                prev = nums[i]
                map[prev] = map.get(prev) - 1

                if(map.get(prev) == 0):
                    map.pop(prev)
                
                i += 1
            
            count += (j - i + 1)
            j += 1
        
        return count

    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        # Exactly K distinct → AtMost(K) - AtMost(K-1)

        atMost_K = self.solve(nums, k)
        atMost_k_minus_one = self.solve(nums, k - 1)

        exactlyK = atMost_K - atMost_k_minus_one

        return exactlyK
        
```

---

[View on LeetCode](https://leetcode.com/problems/subarrays-with-k-different-integers/)
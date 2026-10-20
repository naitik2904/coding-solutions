# Contains Duplicate II

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given an integer array `nums` and an integer `k`, return `true`  *if there are two  **distinct indices*** `i` *and* `j` *in the array such that* `nums[i] == nums[j]` *and* `abs(i - j) <= k`.

 

 **Example 1:** 

```
Input: nums = [1,2,3,1], k = 3
Output: true

```

 **Example 2:** 

```
Input: nums = [1,0,1,1], k = 1
Output: true

```

 **Example 3:** 

```
Input: nums = [1,2,3,1,2,3], k = 2
Output: false

```

 

 **Constraints:** 

- 1 <= nums.length <= 105
- -109 <= nums[i] <= 109
- 0 <= k <= 105

## Solution

**Language:** Python  
**Runtime:** 81 ms (beats 9.51%)  
**Memory:** 36.4 MB (beats 73.12%)  
**Submitted:** 2026-10-20T15:22:39.718Z  

```py
# Sliding Window
# TC: O(n)
# SC: O(n)

class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        n = len(nums)

        s = set()
        i = j = 0

        while(j < n):

            if(abs(i - j) > k) :

                prevNum = nums[i]
                s.remove(prevNum)
                i += 1
            
            currNum = nums[j]

            if(currNum in s):
                return True
            
            s.add(currNum)
            j += 1
        
        return False


```

---

[View on LeetCode](https://leetcode.com/problems/contains-duplicate-ii/)
# Longest Subarray of 1's After Deleting One Element

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given a binary array `nums`, you should delete  **one**  element from it.

Return the size of the  **longest non-empty subarray**  containing only 1's in the resulting array. Return 0 if there is no such  **subarray**.

 

 **Example 1:** 

```
Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.

```

 **Example 2:** 

```
Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].

```

 **Example 3:** 

```
Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.

```

 

 **Constraints:** 

- 1 <= nums.length <= 105
- nums[i] is either 0 or 1.

## Solution

**Language:** Python  
**Runtime:** 42 ms (beats 72.66%)  
**Memory:** 24.6 MB (beats 7.99%)  
**Submitted:** 2026-10-25T12:51:46.800Z  

```py
# TC: O(n)

class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        n = len(nums)

        last_zero_idx = -1
        ans = float('-inf')
        i = j = 0

        while(j < n):

            if(nums[j] == 0):
                i = last_zero_idx + 1
                last_zero_idx = j
            

            ans = max(ans, j - i)
            j += 1
        
        return ans

        
```

---

[View on LeetCode](https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/)
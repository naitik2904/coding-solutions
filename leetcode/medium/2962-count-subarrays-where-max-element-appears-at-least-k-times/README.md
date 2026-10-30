# Count Subarrays Where Max Element Appears at Least K Times

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given an integer array `nums` and a  **positive**  integer `k`.

Return  *the number of subarrays where the  **maximum**  element of* `nums` *appears  **at least*** `k` *times in that subarray.* 

A  **subarray**  is a contiguous sequence of elements within an array.

 

 **Example 1:** 

```
Input: nums = [1,3,2,3,3], k = 2
Output: 6
Explanation: The subarrays that contain the element 3 at least 2 times are: [1,3,2,3], [1,3,2,3,3], [3,2,3], [3,2,3,3], [2,3,3] and [3,3].

```

 **Example 2:** 

```
Input: nums = [1,4,2,1], k = 3
Output: 0
Explanation: No subarray contains the element 4 at least 3 times.

```

 

 **Constraints:** 

- 1 <= nums.length <= 105
- 1 <= nums[i] <= 106
- 1 <= k <= 105

## Solution

**Language:** Python  
**Runtime:** 127 ms (beats 15.97%)  
**Memory:** 32.1 MB (beats 30.94%)  
**Submitted:** 2026-10-30T10:19:33.140Z  

```py
# TC: O(n)

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)

        maxNum = float(-inf)
        for num in nums:
            maxNum = max(maxNum, num)
        
        i = j = 0
        count = 0
        ans = 0

        while(j < n):

            curr = nums[j]
            if(curr == maxNum):
                count += 1
            
            while(count >= k):

                ans += (n - j)

                prev = nums[i]
                if(prev == maxNum):
                    count -= 1
                
                i += 1
            
            j += 1
        
        return ans
        
```

---

[View on LeetCode](https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/)
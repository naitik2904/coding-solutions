# Maximum Subarray

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an integer array `nums`, find the subarray with the largest sum, and return  *its sum*.

 

 **Example 1:** 

```
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

```

 **Example 2:** 

```
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

```

 **Example 3:** 

```
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

```

 

 **Constraints:** 

- 1 <= nums.length <= 105
- -104 <= nums[i] <= 104

 

 **Follow up:**  If you have figured out the `O(n)` solution, try coding another solution using the  **divide and conquer**  approach, which is more subtle.

## Solution

**Language:** Python  
**Runtime:** 33 ms (beats 67.65%)  
**Memory:** 31.5 MB (beats 44.08%)  
**Submitted:** 2026-10-21T14:30:27.757Z  

```py
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        n = len(nums)
        maxSum = float('-inf')
        sum = 0

        for i in range(0, n):

            sum += nums[i]
            maxSum = max(sum, maxSum)
            
            if(sum < 0):
                sum = 0

        return maxSum
        
```

---

[View on LeetCode](https://leetcode.com/problems/maximum-subarray/)
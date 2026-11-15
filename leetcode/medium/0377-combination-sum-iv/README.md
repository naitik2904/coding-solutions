# Combination Sum IV

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an array of  **distinct**  integers `nums` and a target integer `target`, return  *the number of possible combinations that add up to*  `target`.

The test cases are generated so that the answer can fit in a  **32-bit**  integer.

 

Original
Python3
 **Example 1:** 

```
Input: nums = [1,2,3], target = 4
Output: 7
Explanation:
The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
Note that different sequences are counted as different combinations.

```

 **Example 2:** 

```
Input: nums = [9], target = 3
Output: 0

```

 

 **Constraints:** 

- 1 <= nums.length <= 200
- 1 <= nums[i] <= 1000
- All the elements of nums are unique.
- 1 <= target <= 1000

 

 **Follow up:**  What if negative numbers are allowed in the given array? How does it change the problem? What limitation we need to add to the question to allow negative numbers?

## Solution

**Language:** Python  
**Runtime:** 0 ms  
**Memory:** 19.3 MB  
**Submitted:** 2026-11-15T11:05:37.902Z  

```py
# TC: O(N * Target)
# SC: O(Target)

class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        n = len(nums)
        dp = {}
        

        def solve(sum: int)-> int:

            if(sum == target):
                return 1
            
            if(sum > target):
                return 0
            
            if sum in dp:
                return dp[sum]

            count = 0
            for i in range(0, n):

                sum += nums[i]

                count += solve(sum)

                sum -= nums[i]
            
            dp[sum] = count
            return count

        return solve(0)        
```

---

[View on LeetCode](https://leetcode.com/problems/combination-sum-iv/)
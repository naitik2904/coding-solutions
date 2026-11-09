# Fair Distribution of Cookies

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given an integer array `cookies`, where `cookies[i]` denotes the number of cookies in the `ith` bag. You are also given an integer `k` that denotes the number of children to distribute  **all**  the bags of cookies to. All the cookies in the same bag must go to the same child and cannot be split up.

The  **unfairness**  of a distribution is defined as the  **maximum**   **total**  cookies obtained by a single child in the distribution.

Return  *the  **minimum**  unfairness of all distributions*.

 

 **Example 1:** 

```
Input: cookies = [8,15,10,20,8], k = 2
Output: 31
Explanation: One optimal distribution is [8,15,8] and [10,20]
- The 1st child receives [8,15,8] which has a total of 8 + 15 + 8 = 31 cookies.
- The 2nd child receives [10,20] which has a total of 10 + 20 = 30 cookies.
The unfairness of the distribution is max(31,30) = 31.
It can be shown that there is no distribution with an unfairness less than 31.

```

 **Example 2:** 

```
Input: cookies = [6,1,3,2,2,4,1,2], k = 3
Output: 7
Explanation: One optimal distribution is [6,1], [3,2,2], and [4,1,2]
- The 1st child receives [6,1] which has a total of 6 + 1 = 7 cookies.
- The 2nd child receives [3,2,2] which has a total of 3 + 2 + 2 = 7 cookies.
- The 3rd child receives [4,1,2] which has a total of 4 + 1 + 2 = 7 cookies.
The unfairness of the distribution is max(7,7,7) = 7.
It can be shown that there is no distribution with an unfairness less than 7.

```

 

 **Constraints:** 

- 2 <= cookies.length <= 8
- 1 <= cookies[i] <= 105
- 2 <= k <= cookies.length

## Solution

**Language:** Python  
**Runtime:** 8 ms (beats 57.51%)  
**Memory:** 19.2 MB (beats 61.02%)  
**Submitted:** 2026-11-09T15:06:01.655Z  

```py
# Complexity	Value
# Time:  O(kⁿ * k)
# Space: O(n + k)

class Solution:
    def distributeCookies(self, cookies: list[int], k: int) -> int:
        n = len(cookies)
        result = float('inf')
        children = [0] * k

        cookies.sort(reverse=True)

        def solve(idx: int):
            nonlocal result

            if(idx >= n):
                maxChild = max(children)
                result = min(result, maxChild)
                return
            
            cookie = cookies[idx]
            seen = set()

            for i in range(0, k):

                if children[i] in seen:
                    continue

                seen.add(children[i])

                children[i] += cookie

                solve(idx + 1)

                children[i] -= cookie
               

        solve(0)

        return result
        
```

---

[View on LeetCode](https://leetcode.com/problems/fair-distribution-of-cookies/)
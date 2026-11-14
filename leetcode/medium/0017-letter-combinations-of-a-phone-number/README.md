# Letter Combinations of a Phone Number

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a string containing digits from `2-9` inclusive, return all possible letter combinations that the number could represent. Return the answer in  **any order**.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

 

Original
Python3
 **Example 1:** 

```
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

```

 **Example 2:** 

```
Input: digits = "2"
Output: ["a","b","c"]

```

 

 **Constraints:** 

- 1 <= digits.length <= 4
- digits[i] is a digit in the range ['2', '9'].

## Solution

**Language:** Python  
**Runtime:** 0 ms (beats 100.00%)  
**Memory:** 19 MB (beats 94.80%)  
**Submitted:** 2026-11-14T09:11:38.431Z  

```py
# Time Complexity: O(n * 4ⁿ)
# Space Complexity: O(n * 4ⁿ) - including output
# Auxiliary Space: O(n)

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        n = len(digits)

        str = ""
        result = []

        map = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }

        if n == 0:
            return result
        
        def solve(idx: int):
            nonlocal str
            nonlocal result

            if idx >= n:
                result.append(str)
                return
            
            digit = digits[idx]
            temp  = map.get(digit)

            for i in range(0, len(temp)):

                str += temp[i]

                solve(idx + 1)

                str = str[: -1]

        solve(0)
        return result
        
```

---

[View on LeetCode](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)
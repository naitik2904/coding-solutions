# Different Ways to Add Parentheses

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a string `expression` of numbers and operators, return  *all possible results from computing all the different possible ways to group numbers and operators*. You may return the answer in  **any order**.

The test cases are generated such that the output values fit in a 32-bit integer and the number of different results does not exceed `104`.

 

 **Example 1:** 

```
Input: expression = "2-1-1"
Output: [0,2]
Explanation:
((2-1)-1) = 0 
(2-(1-1)) = 2

```

 **Example 2:** 

```
Input: expression = "2 *3-4* 5"
Output: [-34,-14,-10,-10,10]
Explanation:
(2 *(3-(4* 5))) = -34 
((2 *3)-(4* 5)) = -14 
((2 *(3-4))* 5) = -10 
(2 *((3-4)* 5)) = -10 
(((2 *3)-4)* 5) = 10

```

 

 **Constraints:** 

- 1 <= expression.length <= 20
- expression consists of digits and the operator '+', '-', and '*'.
- All the integer values in the input expression are in the range [0, 99].
- The integer values in the input expression do not have a leading '-' or '+' denoting the sign.

## Solution

**Language:** Python  
**Runtime:** 3 ms (beats 32.76%)  
**Memory:** 19.3 MB (beats 86.95%)  
**Submitted:** 2026-10-26T15:33:25.489Z  

```py
# T.C : O(n*2^n)
# S.C : O(2^n) The result vector stores all possible outcomes. The number of results is at most exponential in terms of the number of operators, so the space required to store the results is O(2^n).

class Solution:
    def solve(self, expression: str)-> list[int]:
        n = len(expression)
        result = []

        for i in range(0, n):
            ch = expression[i]

            if(ch == '+' or ch == '-' or ch == '*'):

                leftList = self.solve(expression[0: i])
                rightList = self.solve(expression[i + 1:])

                for x in leftList:
                    for y in rightList:

                        if(ch == '+'):
                            result.append(x + y)
                        elif(ch == '-'):
                            result.append(x - y)
                        else: 
                            result.append(x * y)

        if not result:
            result.append(int(expression))
        
        return result

    def diffWaysToCompute(self, expression: str) -> list[int]:
        return self.solve(expression)
        
```

---

[View on LeetCode](https://leetcode.com/problems/different-ways-to-add-parentheses/)
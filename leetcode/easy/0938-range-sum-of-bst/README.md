# Range Sum of BST

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given the `root` node of a binary search tree and two integers `low` and `high`, return  *the sum of values of all nodes with a value in the  **inclusive**  range* `[low, high]`.

 

 **Example 1:** 

```
Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32
Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.

```

 **Example 2:** 

```
Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
Output: 23
Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.

```

 

 **Constraints:** 

- The number of nodes in the tree is in the range [1, 2 * 104].
- 1 <= Node.val <= 105
- 1 <= low <= high <= 105
- All Node.val are unique.

## Solution

**Language:** Python  
**Runtime:** 2 ms (beats 69.26%)  
**Memory:** 26.2 MB (beats 44.61%)  
**Submitted:** 2026-10-31T15:40:32.382Z  

```py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time: O(N) worst case.
# Space: O(H), recursion stack.
class Solution:
    def solve(self, root: TreeNode | None, low: int, high: int):
        if(root == None):
            return
        
        if(root.val < low):
            self.solve(root.right, low, high)
        
        elif(root.val > high):
            self.solve(root.left, low, high)
        
        else:
            self.ans += root.val

            self.solve(root.left, low, high)
            self.solve(root.right, low, high)

    def rangeSumBST(self, root: TreeNode | None, low: int, high: int) -> int:
        self.ans = 0
        self.solve(root, low, high)

        return self.ans
```

---

[View on LeetCode](https://leetcode.com/problems/range-sum-of-bst/)
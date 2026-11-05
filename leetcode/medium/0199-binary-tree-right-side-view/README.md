# Binary Tree Right Side View

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given the `root` of a binary tree, imagine yourself standing on the  **right side**  of it, return  *the values of the nodes you can see ordered from top to bottom*.

 

 **Example 1:** 

 **Input:**  root = [1,2,3,null,5,null,4]

 **Output:**  [1,3,4]

 **Explanation:** 

 **Example 2:** 

 **Input:**  root = [1,2,3,4,null,null,null,5]

 **Output:**  [1,3,4,5]

 **Explanation:** 

 **Example 3:** 

 **Input:**  root = [1,null,3]

 **Output:**  [1,3]

 **Example 4:** 

 **Input:**  root = []

 **Output:**  []

 

 **Constraints:** 

- The number of nodes in the tree is in the range [0, 100].
- -100 <= Node.val <= 100

## Solution

**Language:** Python  
**Runtime:** 0 ms (beats 100.00%)  
**Memory:** 19.3 MB (beats 60.70%)  
**Submitted:** 2026-11-05T12:43:26.020Z  

```py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# DFS
# TC: O(N) — visits every node once.
# SC: O(H) recursion stack, excluding output. Worst case O(N).

class Solution:
    def solve(self, root, level: int):
        if(root == None):
            return
        
        if len(self.list) < level:
            self.list.append(root.val)
        
        self.solve(root.right, level + 1)
        self.solve(root.left, level + 1)

    def rightSideView(self, root: TreeNode | None) -> list[int]:
        self.list = []

        self.solve(root, 1)     # root, level

        return self.list
        
```

---

[View on LeetCode](https://leetcode.com/problems/binary-tree-right-side-view/)
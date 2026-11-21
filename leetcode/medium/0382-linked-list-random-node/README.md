# Linked List Random Node

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a singly linked list, return a random node's value from the linked list. Each node must have the  **same probability**  of being chosen.

Implement the `Solution` class:

- Solution(ListNode head) Initializes the object with the head of the singly-linked list head.
- int getRandom() Chooses a node randomly from the list and returns its value. All the nodes of the list should be equally likely to be chosen.

 

 **Example 1:** 

```
Input
["Solution", "getRandom", "getRandom", "getRandom", "getRandom", "getRandom"]
[[[1, 2, 3]], [], [], [], [], []]
Output
[null, 1, 3, 2, 2, 3]

Explanation
Solution solution = new Solution([1, 2, 3]);
solution.getRandom(); // return 1
solution.getRandom(); // return 3
solution.getRandom(); // return 2
solution.getRandom(); // return 2
solution.getRandom(); // return 3
// getRandom() should return either 1, 2, or 3 randomly. Each element should have equal probability of returning.

```

 

 **Constraints:** 

- The number of nodes in the linked list will be in the range [1, 104].
- -104 <= Node.val <= 104
- At most 104 calls will be made to getRandom.

 

 **Follow up:** 

- What if the linked list is extremely large and its length is unknown to you?
- Could you solve this efficiently without using extra space?

## Solution

**Language:** Python  
**Runtime:** 20 ms (beats 71.80%)  
**Memory:** 23.1 MB (beats 75.05%)  
**Submitted:** 2026-11-21T15:12:43.562Z  

```py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: ListNode | None):
        self.list = []
        temp = head

        while(temp != None):

            self.list.append(temp.val)
            temp = temp.next

    def getRandom(self) -> int:
        n = len(self.list)
        idx = random.randrange(n)

        return self.list[idx]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
```

---

[View on LeetCode](https://leetcode.com/problems/linked-list-random-node/)
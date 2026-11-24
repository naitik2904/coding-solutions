# Merge k Sorted Lists

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

You are given an array of `k` linked-lists `lists`, each linked-list is sorted in ascending order.

 *Merge all the linked-lists into one sorted linked-list and return it.* 

 

 **Example 1:** 

```
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted linked list:
1->1->2->3->4->4->5->6

```

 **Example 2:** 

```
Input: lists = []
Output: []

```

 **Example 3:** 

```
Input: lists = [[]]
Output: []

```

 

 **Constraints:** 

- k == lists.length
- 0 <= k <= 104
- 0 <= lists[i].length <= 500
- -104 <= lists[i][j] <= 104
- lists[i] is sorted in ascending order.
- The sum of lists[i].length will not exceed 104.

## Solution

**Language:** Python  
**Runtime:** 28 ms (beats 14.85%)  
**Memory:** 23.2 MB (beats 22.38%)  
**Submitted:** 2026-11-24T16:01:48.694Z  

```py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Time Complexity: O(N * log K)
# Space Complexity: O(N + log K)

# N = Total number of nodes
# K = Number of linked lists

class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        n = len(lists)

        if(n == 0):
            return None
        

        def mergeTwoSortedLists(l1: ListNode | None, l2: ListNode | None) -> ListNode | None:            
            if(l1 == None):
                return l2
            
            if(l2 == None):
                return l1
            
            if(l1.val <= l2.val):
                l1.next = mergeTwoSortedLists(l1.next, l2)

                return l1
            
            else:
                l2.next = mergeTwoSortedLists(l1, l2.next)

                return l2
            

        def partitionAndMerge(start: int, end: int)-> ListNode | None:
            if(start == end):
                return lists[start]
            
            if(start > end):
                return None
            
            mid = start + (end - start) // 2

            l1 = partitionAndMerge(start, mid)
            l2 = partitionAndMerge(mid + 1, end)
            
            return mergeTwoSortedLists(l1, l2)


        return partitionAndMerge(0, n - 1)
        
```

---

[View on LeetCode](https://leetcode.com/problems/merge-k-sorted-lists/)
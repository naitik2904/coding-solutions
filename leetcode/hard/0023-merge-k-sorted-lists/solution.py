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
        
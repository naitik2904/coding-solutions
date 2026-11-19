# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# TC: O(n)
# SC: O(1)

class Solution:
    def oddEvenList(self, head: ListNode | None) -> ListNode | None:
        if(head == None or head.next == None):
            return head
        
        odd = head
        even = head.next
        evenHead = even

        while(even != None and even.next != None):

            odd.next  = odd.next.next
            even.next = even.next.next

            odd  = odd.next
            even = even.next
        
        odd.next = evenHead
        return head
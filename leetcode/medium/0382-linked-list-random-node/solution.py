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
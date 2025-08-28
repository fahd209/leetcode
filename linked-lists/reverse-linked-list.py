# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
            understanding:
            input: given a linked 
            output: reverese and return the new linked list

            approach:
                1 -> 2 -> 3 -> 4 -> 5


        """

        cur = head
        prev = None
        

        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next

        return prev

        
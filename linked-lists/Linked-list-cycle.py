# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """

        1 -> 2 -> 3 -> 4 -> 5

        return true or false if the same node can be visited twice

        approach:
            fast pointer slow pointer
            1. the fast pointer will skip two nodes
            2. the slow pointer will skill 1
            3. if the fast pointer gets to the slow then we can return true

        """


        # simple version
        visited = set()
        cur = head

        if head == None:
            return False

        while cur:
            if cur in visited:
                return True
            else:
                visited.add(cur)
            cur = cur.next

        return False


        # if head == None:
        #     return False

        # slow = head
        # fast = head.next

        # while fast and fast.next != None:
        #     if fast == slow:
        #         return True 
            
        #     fast = fast.next.next
        #     slow = slow.next

        # return False
        
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
            1 -> 2 -> 
                 s 
            3 -> 4
            s    n
            p


            Time: O(n)
            Space: O(1)

        """

        # found the middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # split, then reverse the second half
        second = slow.next
        slow.next = None
        prev = None

        while second:
            next = second.next
            second.next = prev
            prev = second
            second = next

        first, second = head, prev 
        while first and second:
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp1
            second = tmp2
            first = tmp1




        # brute force
        # """
        # 1, 2, 3, 4
        #          k

        # Time: o(n)
        # space: o(1)
        # """
        # nodes = [] 
        # cur = head

        # while cur:
        #     nodes.append(cur.val)
        #     cur = cur.next

        # i = 0
        # j = len(nodes) - 1

        # while i <= j:
        #     if i == j:
        #         head.val = nodes[i]
        #         head = head.next
        #     else:
        #         head.val = nodes[i]
        #         head = head.next
        #         head.val = nodes[j]
        #         head = head.next

        #     i += 1
        #     j -= 1
        
        
        
        
        
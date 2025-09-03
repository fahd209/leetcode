"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
            understanding:
                1. given linked list with next and random pointers
                2. the random pointers can point to any nodes in the list
                3. create a copy of the list
            
            approach:
                1. create a copy of each node in the list
                2. store them in hashmap with key being the node.val and value is the node
                3. assign the next and random pointers based on the original list but I'll get the copies from the hash

            {
                7: Node(7)
                13: Node(13)
                11: Node(11)
                10: Node(10)
                1: Node(1)
            }

            dummy = Node(None)
            dummy.next = map[orginal.next.val]

            Time: O(n)
            space: O(n)
        """

        dummyNode = Node(0)
        tail = dummyNode
        cur1 = head
        cur2 = head
        copies = {None: None}

        while cur1:
            copies[cur1] = Node(cur1.val)
            cur1 = cur1.next

        while cur2:
            copy = copies[cur2]
            next = None
            random = None
            if cur2.next:
                next = copies[cur2.next]
            
            if cur2.random:
                random = copies[cur2.random]
            copy.next = next
            copy.random = random
            copy = copy.next
            cur2 = cur2.next

        return copies[head]
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
            understanding:
                1. given two list in reverse order
                2. add them together and return the summed list

            requirements:
                there might be numbers we'll have to carry
                one list might be greater then another list

            approach:
                1. use two pointer 
                2. add the values in those pointers
                3. if the sum value is greater or equeal to 10 then we have a carry to sum up for the next notes

            Time: O(n)
            Space: O(max(m,n))
        """

        node1 = l1
        node2 = l2
        carry = 0
        sum_list = ListNode(None)
        tail = sum_list

        while node1 or node2:
            num1 = 0 if not node1 else node1.val
            num2 = 0 if not node2 else node2.val
            sum = num1 + num2 + carry

            if sum >= 10:
                carry = 1
                sum -= 10
            else:
                carry = 0

            tail.next = ListNode(sum)
        
            node1 = None if not node1 else node1.next
            node2 = None if not node2 else node2.next
            tail = tail.next
            
        if carry == 1:
            tail.next = ListNode(carry)


        return sum_list.next

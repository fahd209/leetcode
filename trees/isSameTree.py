# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        understanding:

        given two binary tree return true or false if they have the same nodes in the same order

        approach:
            1. dfs on both trees (p.left, q.left) and (p.right, q.right)
            2. check if both are null then return true
            3. if one is null and the other is not then return false
            4. if both are the same continue the dfs and until we get to the root node

            [1, 2, 3] [1, 2, 3]
        """

        if p == None and q == None:
            return True

        if p == None or q == None:
            return False
        
        if p.val != q.val:
            return False

        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right) 

        return left and right
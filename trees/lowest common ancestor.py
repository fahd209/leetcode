# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        understanding:

        I'm given two nodes and BST I'm supposed to find the lowest parent of those two nodes
        if one p is a parent of q then p is the LCA and vice versa    

        approach:

        I'll be doing a dfs while keep tracking of the lowest parent
        if a node is equal to p and q return we'll return [parent, True]
        """
        cur = root

        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur

        
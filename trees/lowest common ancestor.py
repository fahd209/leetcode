# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#
# O(log(n))
# o(1)
# iterative
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

        # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# recursive
# O(log(n))
# o(log(n)) because of the call stack
# iterative version is more optimal because the space is o(1) since we're only maintaining only variables
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        understanding:

        I'm given two nodes and BST I'm supposed to find the lowest parent of those two nodes
        if one p is a parent of q then p is the LCA and vice versa    

        approach:
            iterative & recursive:
            use a while loop while cur != None 
            if both values are greater then the root then go to the right because there won't be any values that match. Values.left < p and q
            if both values are less then the root then go to the left because all values in the right won't match because they would be greater
            if  
        """

        LCA = None
        # go to the right because all the values in the left would be less then p and q
        if p.val > root.val and q.val > root.val:
            LCA = self.lowestCommonAncestor(root.right, p, q)

        # go to the left because all the values in the right would be greater then p and q
        elif p.val < root.val and q.val < root.val:
            LCA = self.lowestCommonAncestor(root.left, p, q)
        
        # return the root because either there is split and if there is split that mean LCA must be the cur root 
        # or one of the values might equal the cur root wich would make the LCA
        else:
            return root

        return LCA
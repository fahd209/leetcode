# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode, max_parent=None) -> int:
        """
            given a binary tree count all the good nodes
            a good node is a node in the tree that does not have a parent from the root to the cur node
            that's greater then the current node

            approach:
                keep tree of the parent in a dfs
                if there is cur that is not less then a previous parent then 
                the new parent will cur for the childern
        """

        if root == None:
            return 0

        if max_parent == None:
            max_parent = root

        if root.val > max_parent.val:
            max_parent = root 

        left = self.goodNodes(root.left, max_parent)
        right = self.goodNodes(root.right, max_parent)

        return left + right + 1 if root.val >= max_parent.val else left + right
        
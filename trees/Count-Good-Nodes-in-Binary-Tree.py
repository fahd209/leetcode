# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        understanding:
            given a tree count all the childern nodes
            that are greater then or equal to its parent

        approach:
            1. dfs while keeping track of the parent
            2. if the cur node is greater then or equal to the parent we can increment the count by one
        """

        return self.dfs(root, root)

    def dfs(self, node, parent):

        if node == None:
            return 0
        
        left = None
        right = None
        
        if node.val >= parent.val:
            left = self.dfs(node.left, node)
        else:
            left = self.dfs(node.left, parent)

        if node.val >= parent.val:
            right = self.dfs(node.right, node)
        else:
            right = self.dfs(node.right, parent)

        return left + right + 1 if node.val >= parent.val else left + right
        
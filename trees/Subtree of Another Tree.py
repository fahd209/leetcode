# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        given a tree and substree
        return true if the tree has the subtree in of its childern nodes id doesn't have to be in its childern nodes
        if there is substree in the tree return false
        Time: O(2^n)
        """

        if root == None and subRoot == None:
            return False

        if root == None or subRoot == None:
            return False 

        isSame = None
        if root.val == subRoot.val:
            if self.sameTree(root, subRoot):
                return True
        
        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)

        return left or right

    def sameTree(self, root1, root2):
        # return true because all the other nodes must be the same if we got to the leaf nodes
        if root1 == None and root2 == None:
            return True
        
        # checking with a or statement because one root might be None and the other wont
        if root1 == None or root2 == None:
            return False
        
        if root1.val != root2.val:
            return False
        
        left = self.sameTree(root1.left, root2.left)
        right = self.sameTree(root1.right, root2.right)
        return left and right

        
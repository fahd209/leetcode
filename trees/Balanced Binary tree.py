# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        understanding:
            given a binary tree return True if
            every nodes left and right childern levels
            only differ by one or less other wise return
            false

        approach:
            1. have a global boolean set to True
            2. the boolean will not change to false
                unless there is a node that has childern
                height the differ by more then 1
        """

        self.isbalanced = True

        def dfs(cur):

            if cur == None:
                return 0

            left = dfs(cur.left)
            right = dfs(cur.right)

            if abs(left - right) > 1:
                self.isbalanced = False

            return max(right, left) + 1

        dfs(root)
        return self.isbalanced
        
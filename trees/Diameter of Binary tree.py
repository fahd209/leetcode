# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        given a binary tree return the path with most edges in the tree

        A path is a number of edges that connects two nodes together

        approach:
            1. have a globel max path variable
            2. get the max path from the left and right
            3. add them together and compare it with the global max path variable 
                if its greater then set the max path varaible to the added left and right
        """
        self.max = float('-inf')

        def dfs(cur):
            
            if cur == None:
                return 0

            left = dfs(cur.left)
            right = dfs(cur.right)

            self.max = max(self.max, left + right)

            return max(left, right) + 1

        dfs(root)
        return self.max
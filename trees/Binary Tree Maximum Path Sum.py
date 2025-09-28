# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        understanding:
        given tree return the maximum path in the tree
        requirments:
            1. a path must not have two splits 
            2. each node must be adjecent to each other
            3. there must be only one path connecting all fo the nodes that
                are summed up
        
        approach:
            for each root in the tree
            get the max path of the left and the right
            then added the root 

            if the path sum is greater then the max path sum 
            then set the max path sum to the current path sum
        """
        self.result = float('-inf')

        def dfs(cur):

            if cur == None:
                return

            # getting the left max path and right max path
            left_max = self.getMax(cur.left)
            right_max = self.getMax(cur.right)

            # comparing it with the results if its greater then the result 
            # then set the result to current path sum
            self.result = max(self.result, left_max + right_max + cur.val)

            dfs(cur.left)
            dfs(cur.right)

        dfs(root)
        return self.result

    def getMax(self, root):
        
        if root == None:
            return 0
        

        left = self.getMax(root.left)
        right = self.getMax(root.right)

        max_path = root.val + max(left, right)
        return max(max_path, 0)


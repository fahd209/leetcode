# first try: watched the video 

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



# review: solved



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
            given two binary trees return a boolean indicating if they are the same or not

            requirments:
                they have to be the same in structure and values

            approach:
                1. iterate through both trees
                2. if we iterate through the whole tree 
                    and all nodes are the same then I'll return
                    true
                3. else return false
        """

        # if both are null then all the values above are the same since we got
        # to the leaf node without touching any of the base cases
        if p == None and q == None:
            return True

        # if one of them is null and the other one is not then they are not the same
        if p == None or q == None:
            return False

        
        if p.val != q.val:
            return False

        left = self.isSameTree(p.left, q.left) 
        right = self.isSameTree(p.right, q.right)
        
        return left and right
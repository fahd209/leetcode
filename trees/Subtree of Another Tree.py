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

        
# review

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        understanding:

            root: tree1
            subRoot: tree2

            I am given two trees tree1 and tree2

            i'm supposed to return true or false if tree2 is a sub tree of tree1

            meaning if there is a root in tree1 that has the same childern as tree2 in the same structure 

            approach:
                1. BSF 
                2. check if root in tree1 is the same as tree2 
                3. if it is call dfs function to search both trees from root to leaf nodes to check if they are the same
                4. if the dfs function returns true then tree2 is a subRoot of tree1 so we can stop and return True
                5. if we don't get true fromt he dfs function after iterating through the whole tree then we can return false
        """

        queue = deque([root])

        while queue:
            cur = queue.pop()

            if cur.val == subRoot.val:
                if self.dfs(cur, subRoot):
                    return True

            if cur.left:
                queue.append(cur.left)

            if cur.right:
                queue.append(cur.right)    
        return False

    # checks if both subroots are exactly the same
    def dfs(self, cur1, cur2):

        if cur1 == None and cur2 == None:
            return True

        # if one is null and the other is not return False 
        # because it means the one tree has more levels then the other one
        if cur1 == None or cur2 == None:
            return False

        if cur1.val != cur2.val:
            return False
            
        left = self.dfs(cur1.left, cur2.left)
        right = self.dfs(cur1.right, cur2.right)

        return left and right

        
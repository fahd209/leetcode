# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        understanding:

        given a binary tree return true or false if each node to the left of each root 
        is less then the root and the right nodes of each root is greater then the root

        approach:

        bfs search through the tree while having a left boundry and a right boundry
        each node has to be between that boundry if not return false
        """

        queue = deque([(root, float('-inf'), float('inf'))])
        while queue:
            cur, left, right = queue.popleft()
            if not left < cur.val < right:
                return False

            if cur.left:
                queue.append((cur.left, left, cur.val))
            
            if cur.right:
                queue.append((cur.right, cur.val, right))

        return True
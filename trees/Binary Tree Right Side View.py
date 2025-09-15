# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        understanding:
            given a binary tree return the nodes that you can see from the right
            side if you were standing in the right side

        approach:
            dfs search through the tree
            append each node childern in a array for each level then append the array in a queue
            then I'll pop from the queue and search for the element thats at the end of the array and the will be
            the right most element
        """
        queue = deque([[root]])
        result = []

        if root == None:
            return []

        while queue:
            nodes = queue.popleft()

            result.append(nodes[-1].val)

            childern_nodes = []
            for n in nodes:
                if n.left:
                    childern_nodes.append(n.left)

                if n.right:
                    childern_nodes.append(n.right)
            if len(childern_nodes) > 0:
                queue.append(childern_nodes)
        return result
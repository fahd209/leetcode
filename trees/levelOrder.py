# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        understanding:
            given a binary tree return an that contains all of it's values
            in the same order of the level of the tree

        approach:
            dfs search
            append to the queue every node in every level in an array 
            example node 4 and 5 are childern of one node then append[4, 5]
            then get childern each node and do the same thing -> append its childern in an array
        """


        queue = deque([(root, 0)])
        tree_traversal_array = []

        if not root:
            return []

        while queue:
            node, level = queue.popleft()

            if level >= len(tree_traversal_array):
                tree_traversal_array.append([node.val])
            else:
                tree_traversal_array[level].append(node.val)

            if node.left:
                queue.append((node.left, level + 1))
            
            if node.right:
                queue.append((node.right, level + 1))

        return tree_traversal_array
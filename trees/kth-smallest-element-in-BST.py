# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq
from collections import deque
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        given binary search tree and I'm supposed to return 
        the most kth smallest element
        [1, 2, 3, 4]

        approach:
            dfs through tree and append each node values 
            to an array inorder

            at the end return inorder[k - 1]
        """
        inorder_values = []

        def dfs(cur):

            if cur == None:
                return

            dfs(cur.left)
            inorder_values.append(cur.val)
            dfs(cur.right)

        dfs(root)
        return inorder_values[k - 1]


            


# brute force

# import heapq
# from collections import deque
# class Solution:
#     def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
#         queue = deque([root])
#         heap = []
#         result = None

#         while queue:
#             node = queue.popleft()
#             heapq.heappush(heap, node.val)

#             if node.left:
#                 queue.append(node.left)

#             if node.right:
#                 queue.append(node.right)
        
#         for i in range(k):
#             result = heapq.heappop(heap)
#         return result
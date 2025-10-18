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


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time: O(n)
# Space: O(H) H = height of the tree
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        understanding: 
            given a tree return true if the tree is BST else return False

            rules:
                every nodes left childern have to be strictly less then the node
                every nodes right childern have tobe strictly greater then the node

        approach:
            1. DFS while checking the range or every node
            2. Range: the root node can be anything from negative inf or postive inf
               the left childern of that node can be anything from negative inf to any number that 
               not equal to or greater then its parent. Every node to the right of the root
               has to be between the value of its parent up to postive inf or the max number in the subtree.

            3. if that condition false then we can stop iterating and return False

        Complexsity:
            Time: O(n)
            Space: O(n)
        """


        def dfs(cur, left_range, right_range):

            # return true because we got to a leaf node with out its parents failing
            # the condition
            if cur == None:
                return True

            if not left_range < cur.val < right_range:
                return False 
            
            left = dfs(cur.left, left_range, cur.val)
            right = dfs(cur.right, cur.val, right_range)

            return left and right
        return dfs(root, float('-inf'), float('inf'))
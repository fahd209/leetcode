# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
            understanding:
                given a preorder and inorder array of a tree
                construct the tree

            question:
                will there be duplicate nodes?

            approach:

        """

        if preorder == [] or inorder == []:
            return None

        root = preorder[0]
        preorder = preorder[1:]

        mid = inorder.index(root)
        left_inorder = inorder[:mid]
        right_inorder = inorder[mid+1:]
        left_pre = preorder[:len(left_inorder)] 
        right_pre = preorder[len(left_pre):] 

        node = TreeNode(root)

        node.left = self.buildTree(left_pre, left_inorder)
        node.right = self.buildTree(right_pre, right_inorder)

        return node



# review

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        if preorder == [] or inorder == []:
            return None
        
        # contruct the root
        root = TreeNode(preorder[0])
        preorder = preorder[1:]

        # get the inorder and preorder for the left and right subtrees
        root_index = inorder.index(root.val)
        left_inorder = inorder[:root_index]
        right_inorder = inorder[root_index + 1:]
        left_pre = preorder[:len(left_inorder)]
        right_pre = preorder[len(left_pre):]

        # contruct the root left and right childer
        root.left = self.buildTree(left_pre, left_inorder)
        root.right = self.buildTree(right_pre, right_inorder)

        return root
        
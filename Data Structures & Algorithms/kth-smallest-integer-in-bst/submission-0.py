# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = []
        def inOrderTransversal(node):
            if not node:
                return
            inOrderTransversal(node.left)
            result.append(node.val)
            inOrderTransversal(node.right)

        inOrderTransversal(root)
        return result[k-1]

            

        
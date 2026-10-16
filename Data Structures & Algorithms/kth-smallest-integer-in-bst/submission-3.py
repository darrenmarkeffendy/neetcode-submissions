# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        ans = None
        def inOrderTransversal(node):
            nonlocal count, ans
            if not node:
                return
            inOrderTransversal(node.left)
            if count == k:
                return
            count += 1
            if count == k:
                ans = node.val
                return
            inOrderTransversal(node.right)

        inOrderTransversal(root)
        return ans

            

        
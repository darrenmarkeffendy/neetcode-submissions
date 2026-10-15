# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if not root:
            return False

        if root.val == subRoot.val:
            self_same = self.isSameTree(root, subRoot)
            if self_same:
                return True
        else:
            self_same = False

        left_root = self.isSubtree(root.left, subRoot)
        right_root = self.isSubtree(root.right, subRoot)

        return self_same or left_root or right_root

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
             
        if p and not q:
            return False

        if q and not p:
            return False
        
        if not p and not q:
            return True
        
        if p.val == q.val:
            self_same = True
            left = self.isSameTree(p.left, q.left)
            right = self.isSameTree(p.right, q.right)
        else:
            return False
            
        return left and right and self_same
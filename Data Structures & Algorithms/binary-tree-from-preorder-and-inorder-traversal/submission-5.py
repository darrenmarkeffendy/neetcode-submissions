# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        dictionary = {}
        for index, node in enumerate(inorder):
            dictionary[node] = index

        counter = 0

        def depthFirstSearch(left, right):
            nonlocal counter

            if left > right:
                return None

            root = preorder[counter]
            node = TreeNode(root)
            counter += 1

            middle = dictionary[root]

            node.left = depthFirstSearch(left, middle-1)
            node.right = depthFirstSearch(middle + 1, right)
            return node


        return depthFirstSearch(0, len(inorder) -1)


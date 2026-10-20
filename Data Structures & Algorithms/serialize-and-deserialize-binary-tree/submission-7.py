# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    

# instead of using non local string which required += 1 we should use a list since += string recreates the string so that is o(n^2) worst case

    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        preoder_list = []

        def preoder(node):
            if not node:
                preoder_list.append("N")
            else:
                preoder_list.append(str(node.val))
                preoder(node.left)
                preoder(node.right)
        
        preoder(root)

        res = ",".join(preoder_list)

        return res

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        preoder_list = data.split(",")
        index = 0
        

        def rebuild( ):
            nonlocal index

            node = TreeNode()
            value = preoder_list[index]
            index += 1

            if value == "N":
                return None
            else:
                node.val = int(value)
                node.left = rebuild( )
                node.right = rebuild( )

                return node

        

        return rebuild( )

        




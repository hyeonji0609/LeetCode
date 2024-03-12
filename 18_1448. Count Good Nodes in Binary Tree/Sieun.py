# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def preorder(node, max_nodes):
            if not node:
                return 0

            if node.val >= max_nodes:
                count = 1
            else:
                count = 0

            max_nodes = max(max_nodes, node.val)

            count += preorder(node.left, max_nodes)
            count += preorder(node.right, max_nodes)
            
            return count

        return preorder(root, root.val)
    
"""
Runtime 153 ms
Memory 31.48 MB
"""
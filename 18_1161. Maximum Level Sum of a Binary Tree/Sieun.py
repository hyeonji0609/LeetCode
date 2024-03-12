# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = [(root, 1)]
        result = []
        
        while queue:
            current_node, level = queue.pop(0)
            if level > len(result):
                result.append(0)
            result[level - 1] += current_node.val
            
            if current_node.left is not None:
                queue.append((current_node.left, level + 1))
            if current_node.right is not None:
                queue.append((current_node.right, level + 1))
            
        return result.index(max(result)) + 1
    
"""
Runtime 189 ms
Memory 19.86 MB
"""
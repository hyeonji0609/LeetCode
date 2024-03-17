class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def _preorder(node, count, now):
            nonlocal max_count
            if not node:
                return
            max_count = max(max_count, count)
            if node.left:
                if now == "R":
                    _preorder(node.left, count + 1, "L")
                else:
                    _preorder(node.left, 1, "L")
                    
            if node.right:
                if now == "L":
                    _preorder(node.right, count + 1, "R")
                else:
                    _preorder(node.right, 1, "R")
                    
        max_count = 0
        _preorder(root, 0, None)
        return max_count
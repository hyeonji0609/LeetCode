class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        while root:
            if root.val == val:
                return root
            elif  root.val > val:
                root = root.left
            else:
                root = root.right

"""
Runtime: 49 ms
Memory Usage: 18.3 MB
"""
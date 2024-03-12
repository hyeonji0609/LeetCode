class Solution:
    def get_leftmost(self, root: Optional[TreeNode]):
        while root.left:
            root = root.left
        return root
    
    def delete(self, root: Optional[TreeNode], key: int):
        if root is None:
            return
        
        if root.val > key:
            root.left = self.delete(root.left, key)
        elif root.val < key:
            root.right = self.delete(root.right, key)
        else:
            if root.left and root.right:
                leftmost = self.get_leftmost(root.right)
                root.val = leftmost.val
                root.right = self.delete(root.right, leftmost.val)
                return root
            
            if root.left:
                return root.left
            else:
                return root.right
        
        return root
    
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        return self.delete(root, key)

"""
Runtime: 58 ms
Memory Usage: 19.8 MB
"""
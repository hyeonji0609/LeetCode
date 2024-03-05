class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaf1 = []
        leaf2 = []

        def preorder(root, leaf):
            if root is None:
                return 
            
            if (root.right is None) and (root.left is None):
                return leaf.append(root.val)
            
            preorder(root.left, leaf)
            preorder(root.right, leaf)

        preorder(root1, leaf1)
        preorder(root2, leaf2)
        
        return leaf1 == leaf2
    
"""
Runtime: 34 ms
Memory Usage: 16.5 MB
"""
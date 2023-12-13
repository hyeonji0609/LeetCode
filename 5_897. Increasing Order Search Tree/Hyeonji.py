# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inorder(root): # 중위 순회 구현
            inorder_val = []
            def _inorder(node):
                if node :
                    _inorder(node.left) # 재귀함수로 계속 left까지 탐색
                    inorder_val.append(node.val)
                    _inorder(node.right)
                return inorder_val
            _inorder(root)
            return inorder_val
        
        def make_tree(root):
            base = TreeNode(root[0])
            current = base
            
            for i in range(1,len(root)) :
                current.right = TreeNode(root[i]) # TreeNode의 오른쪽에만 값을 할당
                current = current.right # 오른쪽을 현재 TreeNode로 지정
            
            return base
        
        root = inorder(root)
        
        return make_tree(root)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 노드가 없거나
        # root가 p이거나
        # root가 q이면
        # 그 root를 고대로 반환한다.
        if not root or (root == p) or (root == q):
            return root
        
        # left와 right를 도는 동안
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)
				
				
        # left가 없으면 right가 LCA이고 right가 없으면 left가 LCA라는 말
        if not left:
            return right
        elif not right:
            return left
        # 둘 다 아니라면 그 조상은 root 그 자체
        else:
            return root 


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # root가 없거나 p나 q와 같으면, root 자체를 반환
        if not root or root == p or root == q:
            return root
        # 왼쪽 서브트리에서 p와 q를 재귀적으로 찾기
        left = self.lowestCommonAncestor(root.left, p, q)
        # 오른쪽 서브트리에서 p와 q를 재귀적으로 찾기
        right = self.lowestCommonAncestor(root.right, p, q)
        # 두 노드가 서로 다른 서브트리에 있는 경우, root가 최소 공통 부모
        if left and right:
            return root
        # 그렇지 않고, 왼쪽에만 p와 q가 있으면, 해당 노드를 반환
        elif left:
            return left
        # 그렇지 않고, 오른쪽에만 p와 q가 있으면, 해당 노드를 반환
        else:
            return right
        
        '''
        Runtime 42 ms - Beats 92.70%
        Memory 20.95 MB - Beats 78.69%
        '''
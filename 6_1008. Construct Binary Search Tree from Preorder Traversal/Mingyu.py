# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        # preorder List가 비어있으면 None 반환
        if not preorder:
            return None
        
        # output_root를 preorder의 첫번째 요소로 지정
        output_root = TreeNode(preorder[0])

        # 전위 순회 함수 구현
        def _preorder(node, value):
            # node가 비어있으면 value를 node로 할당
            if not node:
                return TreeNode(value)
            # value가 node.val보다 작은 경우
            if value < node.val:
                # node의 left가 없는 경우에 value를 node.left로 업데이트
                if not node.left:
                    node.left = TreeNode(value)
                # 그렇지 않고, left가 있는 경우 함수 재귀 호출
                else:
                    _preorder(node.left, value)
            # value가 node.val보다 큰 경우
            else:
                # node의 right가 없는 경우에 value를 node.right로 업데이트
                if not node.right:
                    node.right = TreeNode(value)
                # 그렇지 않고, right가 있는 경우 함수 재귀 호출
                else:
                    _preorder(node.right, value)

        # preorder의 첫번째 요소 이후만큼 반복
        for value in preorder[1:]:
            _preorder(output_root, value)

        return output_root
    
    
'''
Runtime 46ms - Beats 43.88%
Memory 16.29MB - Beats 84.09%
'''
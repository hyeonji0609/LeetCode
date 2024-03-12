# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        # 삭제할 노드의 위치 찾기
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        # 현재 노드가 삭제할 노드일 때
        else:
            # 리프 노드 또는 하나의 자식만 있는 경우
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            
            # 두 개의 자식을 가진 경우
            # 현재 노드의 오른쪽에서 가장 작은 값의 트리를 찾음
            min_node = root.right
            while min_node.left:
                min_node = min_node.left
            
            # 찾은 가장 작은 값을 현재 노드의 값으로 대체
            root.val = min_node.val
            # 대체된 값이 위치한 원래 노드를 삭제
            root.right = self.deleteNode(root.right, min_node.val)

        return root
    
"""
Runtime 51 ms
Memory 19.89 MB
"""
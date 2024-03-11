# 이진 트리 노드의 정의
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        # 왼쪽에 노드가 있다면 계속 옮겨주기
        def get_leftmost(node):
            while node.left:
                node = node.left
            return node
        
        # 본격 삭제 메소드
        def _delete(node, data):
            # 노드가 없다면 None 반환
            if node is None:
                return None  
            
            # 들어온 data보다 현재 값이 더 크다면 왼쪽으로
            if node.val > data:
                node.left = _delete(node.left, data)
            # 아니라면 오른쪽으로 
            elif node.val < data:
                node.right = _delete(node.right, data)
            # 삭제할 노드를 찾았으면
            else:
                # 노드가 두 개의 자식을 가지고 있는 경우
                if node.left and node.right:
                    # 오른쪽 자식의 왼쪽 node를 바꿔주기
                    leftmost = get_leftmost(node.right)
                    # 현재 노드를 leftmost의 값으로 대체해주고
                    node.val = leftmost.val
                    # leftmost의 값을 삭제하고 반환
                    node.right = _delete(node.right, leftmost.val)
                elif node.left:
                    # 노드가 왼쪽 자식만 가지고 있는 경우
                    return node.left
                else:
                    # 노드가 오른쪽 자식만 가지고 있는 경우 또는 리프 노드인 경우
                    return node.right

            return node

        # 삭제 후 루트를 업데이트
        return _delete(root, key)
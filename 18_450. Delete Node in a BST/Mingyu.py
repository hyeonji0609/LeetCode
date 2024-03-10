class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # 가장 왼쪽에 있는 노드를 찾는 함수
        def get_leftmost(node):
            while node.left:
                node = node.left
            return node
        # 재귀적으로 BST에서 key를 삭제하는 함수
        def _delete(node, key):
            # node가 없으면 None을 리턴
            if not node:
                return None
            #삭제할 노드가 현재 노드보다 작으면 왼쪽에서 찾아서 삭제
            if key < node.val:
                node.left = _delete(node.left, key)
            #삭제할 노드가 현재 노드보다 크면 오른쪽에서 찾아서 삭제
            elif key > node.val:
                node.right = _delete(node.right, key)
            else:
            #삭제할 노드를 찾았고, 자식노드가 둘이면
                if node.left and node.right:
                    #삭제할 노드의 오른쪽에서 가장 작은(왼쪽) 노드를 찾는다.
                    leftmost = get_leftmost(node.right)
                    #삭제할 노드의 값을 가장 왼쪽 노드의 값으로 대체한다.
                    node.val = leftmost.val
                    #가장 왼쪽 노드를 삭제한다.
                    node.right = _delete(node.right, leftmost.val)
                #자식이 하나이거나 리프 노드이면 해당 자식을 반환
                elif node.left:
                    return node.left
                else:
                    return node.right
            # 삭제 후 업데이트 된 노드를 리턴
            return node
        # root와 key로 _delete함수 실행한 값을 리턴 
        return _delete(root, key)
    
    '''
    Runtime 51 ms - Beats 85.82%
    Memory 19.88 MB - Beats 72.26%
    '''